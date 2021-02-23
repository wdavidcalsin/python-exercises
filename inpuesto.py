def inpuesto():
    age = input('Su edad es: ')
    age = int(age)

    sueldo = input('Sus ingresos mensuales es: ')
    sueldo = int(sueldo)

    if age > 16 and sueldo > 1000:
        print('Si puede dar sus inpuestos.')
    else:
        print('No cumple con los requisitos para dar sus inpuestos.\nQuiere ver los requisitos?')