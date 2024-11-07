import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta

# Configuración del bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='@', intents=intents)

# Diccionario para almacenar las tareas
tasks_list = {}

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    check_reminders.start()  # Iniciar la tarea de recordatorio

@bot.command(name='add_task')
async def add_task(ctx, task_name: str, due_time: str):
    """
    Hola querido estudiante añade una tarea con un nombre y una fecha límite.
    Formato de fecha: 'YYYY-MM-DD HH:MM'
    """
    try:
        due_date = datetime.strptime(due_time, '%Y-%m-%d %H:%M')
        tasks_list[task_name] = due_date
        await ctx.send(f'Tarea "{task_name}" añadida para {due_date.strftime("%Y-%m-%d %H:%M")}')
    except ValueError:
        await ctx.send('Formato de fecha no válido. Usa "YYYY-MM-DD HH:MM".')

@bot.command(name='remove_task')
async def remove_task(ctx, task_name: str):
    """Elimina una tarea por su nombre."""
    if task_name in tasks_list:
        del tasks_list[task_name]
        await ctx.send(f'Tarea "{task_name}" eliminada.')
    else:
        await ctx.send(f'No se encontró la tarea "{task_name}".')

@bot.command(name='list_tasks')
async def list_tasks(ctx):
    """Muestra la lista de tareas pendientes."""
    if not tasks_list:
        await ctx.send('No hay tareas pendientes.')
    else:
        response = 'Tareas pendientes:\n'
        for task, due_date in tasks_list.items():
            response += f'- {task}: {due_date.strftime("%Y-%m-%d %H:%M")}\n'
        await ctx.send(response)

@tasks.loop(minutes=1)
async def check_reminders():
    """Verifica si hay tareas con fecha límite cercana para enviar recordatorios."""
    now = datetime.now()
    for task, due_date in list(tasks_list.items()):
        if now >= due_date:
            # Enviar recordatorio y eliminar la tarea
            for channel in bot.get_all_channels():
                if isinstance(channel, discord.TextChannel):
                    await channel.send(f'⚠️ ¡Recordatorio! La tarea "{task}" está vencida.')
            del tasks_list[task]

@check_reminders.before_loop
async def before_check_reminders():
    """Esperar hasta que el bot esté listo antes de iniciar el loop."""
    await bot.wait_until_ready()

# Aquí debes reemplazar 'TU_TOKEN' con el token de tu bot de Discord
bot.run('MTMwMDQ5NDA5NTAxNzMxNj-eQs4.KhMjMnLwdeY573vMUoVgwZaoSzZ5gu8A')
