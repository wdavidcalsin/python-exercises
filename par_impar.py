from colorama import Fore, Style


def par_impar():
    number = input('Ingrese un numero: ')
    number = int(number)

    if number % 2 == 0:
        print(Fore.GREEN+'El numero es par')
    else:
        print(Fore.RED+'El numero es impar')
