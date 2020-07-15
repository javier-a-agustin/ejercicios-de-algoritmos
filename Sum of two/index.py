A = [5, 0, 11, -4, 0]
B = [1, -1, 0, 44]
N = 10

# Primer opcion

def sum_of_two(A, B, N):
    # Esta opcion tiene orden de ejecucion de n**2.
    for a in A:
        for b in B:
            if a + b == N:
                return True
    return False

print(sum_of_two(A, B, N))

# Segunda opcion
contenedor = set()

def sum_of_two_v2(A, B, N):
    # Como esta funcion no tiene bucles anidados, el orden de ejecucion es n.
    for a in A:
        contenedor.add(N - a)
    
    for b in B:
        if b in contenedor:
            return True
    
    return False

print(sum_of_two_v2(A, B, N))