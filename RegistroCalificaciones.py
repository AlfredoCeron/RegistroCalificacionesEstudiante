#  ---  REGISTRO DE CALIFICACIONES  ---  #

"""
. Registrar cantidad de rubros (Examenes, Tarea, Proyecto, Asistencia, PtsExtra, etc)
. Registrar calificacion en cada rubro - Examen, Tarea, Proyecto
    .EJEMPLO: { Tareas: {"tema1": 10}, Proyectos: {"tema1": 8, "tema2": 7}, Examenes: {"tema1": 9, "tema2": 10, "tema3": 8} }

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
        rubrosNombre[rubro]= {}
    return rubrosNombre


def registrar_calificacion(rubros):
    print("Rubros registrados:")
    for i in range(len(rubros)):
        print(f"\t{i+1}. {list(rubros.keys())[i]}") #Diccionario a lista para aprovechar el indice
    rubroSeleccionado= int(input("Seleccione el número del rubro para registrar la calificación: ")) - 1
    tema= input("Identificador de la asignación: ")
    calificacion= float(input("Calificación obtenida: "))
    #  rubros [Tareas] [Tarea1] = 10 
    rubros[list(rubros.keys())[rubroSeleccionado]] [tema]= calificacion
    return rubros

def mostrar_calificaciones(rubros):
    print("Rubros registrados:")
    for i in range(len(rubros)):
        print(f"\t{i+1}. {list(rubros.keys())[i]}") #Diccionario a lista para aprovechar el indice
    rubroSeleccionado= int(input("Seleccione el número del rubro para mostrar sus calificaciones: ")) - 1
    print(f"   ===Calificaciones del rubro '{list(rubros.keys())[rubroSeleccionado]}'===")
    for tema, calif in rubros[list(rubros.keys())[rubroSeleccionado]].items():  #items (tema, calif) en diccionario [2D]
        print(f"\t{tema}  -  {calif}")




rubros=registrar_rubros()
print("")
registrar_calificacion(rubros)
print("")
print(rubros)
print("")
registrar_calificacion(rubros)
print("")
mostrar_calificaciones(rubros)
print("")






