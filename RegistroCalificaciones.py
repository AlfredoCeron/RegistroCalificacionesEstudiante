#  ---  REGISTRO DE CALIFICACIONES  ---  #

"""
. Registrar cantidad de rubros (Examenes, Tarea, Proyecto, Asistencia, PtsExtra, etc)
. Registrar calificacion en cada rubro - Examen, Tarea, Proyecto
    . tema - calif , Fecha-calif  :  [27/02/2024 - 10]
. Mostrar historial de calificaciones de X rubro
    .Borrar calif por indice/numero en la lista del historial de calificaciones
"""    

def registrar_rubros():
    cantidadRubros= int(input("¿Cuántos rubros desea registrar? "))
    if cantidadRubros <= 0:
        return "\tLa cantidad de rubros debe ser mayor a cero."
    rubrosNombre= {}
    for i in range(cantidadRubros):
        rubro= input("Ingrese el nombre del rubro: ")
        rubrosNombre[rubro]= []
    return rubrosNombre

def registrar_calificacion(rubros):
    rubro= input("Ingrese el nombre del rubro para registrar la calificación: ")
    if rubro not in rubros:
        return f"\tEl rubro '{rubro}' no existe. Por favor, regístrelo primero."
    tema= input("Ingrese el tema de la calificación: ")
    calificacion= float(input("Ingrese la calificación: "))
    fecha= input("Ingrese la fecha de la calificación (dd/mm/yyyy): ")
    rubros[rubro].append({"tema": tema, "calificacion": calificacion, "fecha": fecha})
    return f"\tCalificación registrada en el rubro '{rubro}'."


print(registrar_rubros())























"""
{Español: {Tareas: [10,9,8,7], Proyectos: [8,7,10,9], Examenes: [9,10,8,7]},
Matematicas: {Tareas: [10,9,8,7], Proyectos: [8,7,10,9], Examenes: [9,10,8,7]},}

[Español [Tareas[10,9,8,7], Proyectos[8,7,10,9], Examenes[9,10,8,7]],
Matematicas]


{Tareas: [10,9,8,7], Proyectos: [8,7,10,9], Examenes: [9,10,8,7]}

"""    
    
escuela= [["Español", ["Tareas", [10,9,8,7]]  ],
          "Matematicas"]
print()
print("\n---------------------")
print(escuela[0][1])

if "Español" in escuela[0][0]:
    print("Tareas: ", escuela[0][1][1])


