numvalor = int(input("digite un numero maximo:"))
par = range(0, numvalor, 2)
for i in par:
    suma = sum(par)
print(f"La suma de todos los numeros pares de 0 hasta {numvalor}, es igual a {suma}") 