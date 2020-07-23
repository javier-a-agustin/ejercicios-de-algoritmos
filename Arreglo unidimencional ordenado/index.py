lista = [0, 1, 3, 1, 4]

def ascendente(lista):
    for i in range(0, len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

print(ascendente(lista))