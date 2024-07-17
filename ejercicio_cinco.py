"""
Crear una funcion que me me retorne un diccionario con los datos personales de un alumno
ejm:
entrada: ("jose","alvarez","30","APSTI","III")
salida: {nombre:"jose",apellido:"alvarez",edad:"30",programa_estudio:"APSTI",semestre:"III"}
"""
def crear_diccionario_alumno(nombre, apellido, edad, programa_estudio, semestre):
    """
    Retorna un diccionario con los datos personales de un alumno.

    Parámetros:
    nombre (str): El nombre del alumno.
    apellido (str): El apellido del alumno.
    edad (str): La edad del alumno.
    programa_estudio (str): El programa de estudio del alumno.
    semestre (str): El semestre del alumno.

    Retorna:
    dict: Un diccionario con los datos personales del alumno.
    """
    datos_alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "programa_estudio": programa_estudio,
        "semestre": semestre
    }
    return datos_alumno

# Ejemplo de uso
datos = crear_diccionario_alumno("jose", "alvarez", "30", "APSTI", "III")
print(datos)
