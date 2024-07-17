"""
Crear un diccionario de 5 registros de tiendas comerciales
y crear las siguientes funciones para el procesamiento de su informacion
1. funcion que me permita editar el nombre de una las tiendas comerciales
2. funcion que me permita actualizar el horario de atencion.
3. funcion que me permita eliminar una tienda comercial.
"""
# Definición del diccionario de tiendas comerciales
tiendas = {
    1: {
        "nombre": "Librería El Saber",
        "ubicacion": "Calle 123, Ciudad A",
        "horario_atencion": "9:00 - 18:00",
        "telefono": "123-456-789"
    },
    2: {
        "nombre": "Electrodomésticos Mega",
        "ubicacion": "Avenida 456, Ciudad B",
        "horario_atencion": "10:00 - 20:00",
        "telefono": "987-654-321"
    },
    3: {
        "nombre": "Ropa y Moda Trendy",
        "ubicacion": "Boulevard 789, Ciudad C",
        "horario_atencion": "11:00 - 19:00",
        "telefono": "456-789-123"
    },
    4: {
        "nombre": "Deportes y Fitness",
        "ubicacion": "Calle 321, Ciudad D",
        "horario_atencion": "8:00 - 17:00",
        "telefono": "654-321-987"
    },
    5: {
        "nombre": "Juguetes y Diversión",
        "ubicacion": "Avenida 654, Ciudad E",
        "horario_atencion": "10:00 - 22:00",
        "telefono": "321-654-987"
    }
}

# Función para editar el nombre de una tienda
def editar_nombre_tienda(id_tienda, nuevo_nombre):
    """
    Edita el nombre de una tienda comercial.

    Parámetros:
    id_tienda (int): El ID de la tienda a editar.
    nuevo_nombre (str): El nuevo nombre para la tienda.

    Retorna:
    str: Mensaje de éxito o error.
    """
    if id_tienda in tiendas:
        tiendas[id_tienda]["nombre"] = nuevo_nombre
        return f"Nombre de la tienda con ID {id_tienda} actualizado a '{nuevo_nombre}'."
    else:
        return f"Tienda con ID {id_tienda} no encontrada."

# Función para actualizar el horario de atención de una tienda
def actualizar_horario_atencion(id_tienda, nuevo_horario):
    """
    Actualiza el horario de atención de una tienda comercial.

    Parámetros:
    id_tienda (int): El ID de la tienda a actualizar.
    nuevo_horario (str): El nuevo horario de atención para la tienda.

    Retorna:
    str: Mensaje de éxito o error.
    """
    if id_tienda in tiendas:
        tiendas[id_tienda]["horario_atencion"] = nuevo_horario
        return f"Horario de atención de la tienda con ID {id_tienda} actualizado a '{nuevo_horario}'."
    else:
        return f"Tienda con ID {id_tienda} no encontrada."

# Función para eliminar una tienda comercial
def eliminar_tienda(id_tienda):
    """
    Elimina una tienda comercial.

    Parámetros:
    id_tienda (int): El ID de la tienda a eliminar.

    Retorna:
    str: Mensaje de éxito o error.
    """
    if id_tienda in tiendas:
        del tiendas[id_tienda]
        return f"Tienda con ID {id_tienda} eliminada exitosamente."
    else:
        return f"Tienda con ID {id_tienda} no encontrada."

# Ejemplos de uso
print(editar_nombre_tienda(1, "Librería Conocimiento"))
print(actualizar_horario_atencion(2, "9:00 - 21:00"))
print(eliminar_tienda(3))

# Verificar el estado actual del diccionario
print(tiendas)
