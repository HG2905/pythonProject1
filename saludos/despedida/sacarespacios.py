texto = input("Ingresa un texto...: ")
unico = []
may = []
min = []
for i in texto:
    if i.isnumeric():
        if i not in unico:
            unico.append(i)
            unico.sort()

    elif i.isspace():
        continue

    elif isinstance(i, str):
        if i not in may and i.isupper():
            may.append(i)
            may.sort()
        elif i not in min and i.islower():
            min.append(i)
            min.sort()
print(min)
print(may)
print(unico)
print("Hola mundo")