def division():
    firts = input('Primer numero: ')
    firts = int(firts)

    second = input('Segundo numero: ')
    second = int(second)

    divisible = firts % second

    if divisible == 0:
        print('Error')
    else:
        print('La division es', firts//second)
