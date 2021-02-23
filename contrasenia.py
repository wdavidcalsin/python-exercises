def contrasenia():
    key = 'david'

    password = input('Introdusca la contrasena para validar: ')

    if key == password.lower():
        print('La contrasenia es correcta.')
    else:
        print('La contrasenia no coencide.')
