# variables, input, casting, if, operadores lógicos, bucles, formato, matemáticas, pensamiento algorítmico
opcion = input("1. ¿Desea simular sus ahorros? (Presione S para continuar, N para salir).")

while opcion == "S": 
    ahorro_inicial = input("Ingrese su ahorro inicial: ")
    ahorro_mensual = input("Ingrese su aporte mensual: ")
    tasa_interes_anual = input("Ingrese la tasa de interés anual: ")
    meses = input("Ingrese el número de meses por el/los que plane ahorrar: ")

    x=float(tasa_interes_anual) # CONVERSIONES
    tasa_interes_mensual= x/12
    num_meses=int(meses)
    inicial=float(ahorro_inicial)
    mensual=float(ahorro_mensual)

    for i in range(1, num_meses + 1):
        interés_del_mes = inicial * (x / 100 / 12)
        nuevo_saldo=inicial + mensual + tasa_interes_mensual
        print(f"Mes {i}: ${nuevo_saldo:,}")
        inicial= nuevo_saldo

    if nuevo_saldo >= 10000000:
        texto= "¡Felicidades, casi cumples tu meta!"
        print(texto.upper())
    opcion = input("1. ¿Desea simular sus ahorros? (Presione S para continuar, N para salir).")
    if opcion== "N": 
        print ("¡Hasta pronto!")