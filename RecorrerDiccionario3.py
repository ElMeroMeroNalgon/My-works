usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

for i in range(3):
    NombreUsuario = input("Ingrese su nombre de usuario: ")
    if NombreUsuario in usuarios:
        Contraseña = input("Ingrese su contraseña: ")
        # Aquí puedes comprobar la contraseña si quieres
        if Contraseña == usuarios[NombreUsuario]["password"]:
            print("Acceso concedido. Bienvenido {} {}.".format(
                usuarios[NombreUsuario]["nombre"],
                usuarios[NombreUsuario]["apellido"]
            ))
        else:
            print("Contraseña incorrecta.")
    else:
        print("El usuario no existe.")
