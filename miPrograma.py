print("Inicio del programa")

miLista = [2, 1, 5, 4, 3] #1,2,3,4,5
print(miLista[0:5])

miLista.append(0)
miLista.append(19)
miLista.append(7)

miLista.sort()
print("Ordenado")

print(miLista[0:5])

miLista.reverse()

print("Invertido")

for element in miLista:
    print(element)

print("Fin del programa")