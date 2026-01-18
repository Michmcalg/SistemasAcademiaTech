# variables, input, casting, if, operadores lógicos, bucles, formato, matemáticas, pensamiento algorítmico
ahorro_inicial = input("Ingrese su ahorro inicial: ")
ahorro_mensual = input("Ingrese su ahorro mensual: ")
tasa_interes_anual = input("Ingrese la tasa de interés anual: ")
meses = input("Ingrese el número de meses por el/los que plane ahorrar: ")

x=float(tasa_interes_anual)
tasa_interes_mensual= x/12

num_meses=int(meses)
inicial=float(ahorro_inicial)
mensual=float(ahorro_mensual)

for i in range(1, num_meses):
    nuevo_saldo=inicial + mensual + tasa_interes_mensual
    print(f"Mes {i}: {nuevo_saldo}")
    inicial= mensual
    b= nuevo_saldo