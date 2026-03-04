#loops, listas, diccionarios, funciones, random

gastos = [] # lista vacía
total = 0

while True: #loops
    nombre = input("Ingrese el nombre de su gasto: ")

    if nombre.lower() ==  "salir":
        break 

    valor = float(input("Ingrese el valor del gasto: "))
    gasto = {"Nombre": nombre, #diccionario 
             "Valor": valor}
    
    gastos.append(gasto)


for gasto in gastos: #loops
    print(gasto["Nombre"], ":", gasto["Valor"])
    total += gasto["Valor"]

print("Total:", total)


