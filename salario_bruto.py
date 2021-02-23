def salario():
    horas = input('Introdusca horas: ')
    tarifa = input('Tarifa por hora: ')

    salario = int(horas) * float(tarifa)

    print('Su sallario es', salario)
