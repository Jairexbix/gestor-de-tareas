import json
import time # Unicamente con fines ilustrativos

with open ('datos.json') as file:
    data = json.load(file)

tareas = data

def menu ():
    print('')
    print('Selelciona una opcion')
    print('---------------------')
    print('1- Agregar Tarea, 2- Marcar como completada, 3-Eliminar Tarea, 4-Mostrar las tareas, 5- Eliminar todas las tareas, 6-Salir')
    print('')

def agregar_tarea ():
    nombre = input('Ingresa el nombre de la tarea: ')
    tarea = {'nombre' : nombre, 'completada' : False}
    tareas.append(tarea)
    print('Se agrego correctamente la tarea')

def mostrar_tareas ():
    for tarea in enumerate(tareas):
        nombre = tarea[1].get('nombre')
        completada = tarea[1].get('completada')
        if completada == True:
            pendiente = 'esta completada'
        else:
            pendiente = 'esta pendiente'
        print(f'{tarea[0] + 1}- El nombre de la tarea es: {nombre} y la tarea {pendiente}')

def marcar_completada ():
    mostrar_tareas()
    opcion = int(input('Ingresa el numero de la tarea a marcar como completada: '))
    
    if opcion >= 1 and opcion <= len(tareas):
        tarea_seleccionada = tareas[opcion - 1]
        tarea_seleccionada['completada'] = True
        nombre = tarea_seleccionada['nombre']
        print(f'La tarea seleccionada: {nombre}. Fue marcada como completada')

def eliminar_tarea ():
    mostrar_tareas()
    opcion = int(input('Escribe le numero de la tarea que quieres eliminar: '))
    if opcion >= 1 and opcion <= len(tareas):
        tarea = tareas[opcion - 1]
        nombre = tarea['nombre']
        tareas.pop(opcion - 1)
        print(f'Se elimino correctamente: {nombre}')

def eliminar_todas_las_tareas (tareas):
    tareas = []
    print('Se eliminaron con exito todas las tareas')
    return tareas

def guardar_tareas ():
    with open ('datos.json', 'w') as file:
        json.dump(tareas,file)


print('----- BIENVENIDO -----')
print('-- Gestor de tareas --')    
print('')
while True:
    menu()
    choose = input('Escribe el numero de la opcion para selecionarla: ')
    print('')
    print('----------')
    print('')
    if choose == '1':
        agregar_tarea()
        pass
    elif choose == '2':
        marcar_completada()
        pass
    elif choose == '3':
        eliminar_tarea()
        pass
    elif choose == '4':
        mostrar_tareas()
        pass
    elif choose == '5':
        tareas = eliminar_todas_las_tareas(tareas)
        pass
    elif choose == '6':
        guardar_tareas()
        print('Guardando las tareas . . .')
        time.sleep(3.0)
        print(' . . .')
        time.sleep(2.0)
        print(' . . .')
        time.sleep(2.0)
        print(' . . .')
        time.sleep(2.0)
        print('Se guardo con exito. Hasta la proxima')
        print('')
        break
    else:
        print('Escriba una opcion valida')
        pass