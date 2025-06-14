diccionario = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}
lista = []
for value in diccionario.values():
    if value not in lista:
        lista.append(value)
    else:
        continue

print("Lista de valores del diccionario:", lista)
