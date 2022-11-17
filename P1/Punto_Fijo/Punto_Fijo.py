def xnew(x):
    return (2*x**2+3)/5
X0 = 0
X1 = 0
itera = 0
for i in range(100):
    X1 = xnew(X0)
    if abs(X1-X0) < 0.000000001:
       break
    X0 = X1
    itera += 1
print("La raiz es %.5f"%X1)                             #%.5f = 5 decimales typo float para el resultado
print("Usando %i iteraciones"%itera)                    #los porcentajes sirven para definir el tipo de resultado y el ultimo = variable
