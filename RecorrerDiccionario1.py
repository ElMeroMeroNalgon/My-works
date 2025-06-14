Ejemplo = [1, 2, 3, 4, 5,6,4,3,2,5,23,4,23,1,2,5,23,4,7,]
diccinario = {} 
for i in Ejemplo:
    a = Ejemplo.count(i)
    diccinario.update({i: a})
print(diccinario)