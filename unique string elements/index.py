cadena = "asdfg#*¨qkm 1"
diccionario = {}

def unique(cadena):
    # Utilizando otra estructura de dato adicional.
    for c in cadena:
        if c not in diccionario.keys():
            diccionario[c] = 1
        else:
            return False

    return True

print(unique(cadena))

var1 = ""

def unique_v2(cadena):
    # Orden de ejecucion = n**2. Pero sin usar otra estructura de dato. Solo una variable adicional
    for c in range(0, len(cadena)):

        var1 = cadena[c + 1:]

        for i in var1:
            if cadena[c] == i:
                return False

    return True

print(unique_v2(cadena))