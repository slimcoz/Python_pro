# Bot de Discord para Gestión de Tareas

## Descripción
Este bot de Discord permite a los usuarios gestionar tareas, añadir recordatorios y mostrar la lista de tareas pendientes.

### Funcionalidades
- Añadir una tarea con fecha límite (`@add_task <nombre_de_tarea> <YYYY-MM-DD HH:MM>`)
- Eliminar una tarea (`@remove_task <nombre_de_tarea>`)
- Mostrar la lista de tareas pendientes (`@list_tasks`)
- Recordatorios automáticos cuando una tarea alcanza su fecha límite

## Instalación
1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener Python 3.6+ y `discord.py` instalado.
   ```bash
   pip install -r requerimientos.txt
3. para usar en DC debes configurar y con el URL asignarlo a tu canal.

## inportante
- Quisiera aclarar que no incluí el token completo en el código, ya que es un dato privado. Para probar el bot, 
deberán reemplazar el token con uno personal del evaluador o de la persona que revise el proyecto.
