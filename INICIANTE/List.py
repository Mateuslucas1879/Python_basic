lista = [10,20,10,20,150,205,269,452,620,120,158]
lista[1]= 20
lista[2]= 30
lista[3] = 40
lista [4] = 50
lista [5] = 60
print(lista)
del lista[6]
print(lista)
lista.append(70)
print(lista)
lista.pop()
print(lista)
lista.append(740)
lista.insert(6,70)
print(lista)

print()
lista02 = ["Maria","Luiza","Yasmin"]
indice = range(len(lista02))

for indices in indice:
    print(indices,lista02[indices])
print()
for lista01, value in enumerate(lista02):
    print(lista01,value)