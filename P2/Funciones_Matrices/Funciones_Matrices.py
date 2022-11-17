def createMatriz(m,n,v):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(v)
    return C

def getDimensiones(A):
    return (len(A), len(A[0]))

def sumaMatrices(A,B):
    Am,An = getDimensiones(A)
    Bm,Bn = getDimensiones(B)
    if Am != Bm or An != Bn:
        print("Las dimensiones son diferentes")
        return[]
    C = createMatriz(Am,An,0)
    for i in range(Am):
        for j in range(An):
            C[i][j]= A[i][j] + B[i][j]

    return C

def mulMatrices(A,B):
    Am,An = getDimensiones(A)
    Bm,Bn = getDimensiones(B)
    if An != Bm: 
        print("Las matrices no son conformables")
        return[]
    C = createMatriz(Am,Bn, 0)
    for i in range(Am):
        for j in range(Bn):
            for k in range(An):
                C [i][j] += A[i][k] * B[k][j]
    return C

A = createMatriz(2,1,2)
B = createMatriz(1,2,1)

print(mulMatrices(A,B))
