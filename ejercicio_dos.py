"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def es_primo(n):
    """Determina si un número n es primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filtrar_primos(lista):
    """Filtra los números primos de la lista usando filter."""
    return list(filter(es_primo, lista))

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primos = filtrar_primos(numeros)
print(primos)