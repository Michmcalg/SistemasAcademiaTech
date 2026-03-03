#practica de if y string methods

while True:
    user = input("Ingrese su usuario, porfavor: ")

    if len(user) > 12:
        print("Su usuario no debe contener más de 12 caracteres.")
    elif " " in user:
        print("Su usuario no debe contener espacios.")
    elif any(char.isdigit() for char in user): 
        print("Su usuario no debe contener números.")
    else:
        print("Su usuario fue guardada con éxito.")
        break