#practica de while

print("*****MENÚ*****")
print("1. Ingresar saldo")
print("2. Mostrar saldo")
print("3. Salir")


opcion = int(input("Elige una opción: "))

saldo = 0

while opcion != 3:  
    match opcion: 
        case 1: 
            saldo= float(input("Monto: "))
        case 2: 
            print(f"Su saldo es: ${saldo}")
        case 3: 
            print("¡Vuelva pronto!")
        case _ :
            print("Opción no válida")
    opcion = int(input("Elige una opción: "))
