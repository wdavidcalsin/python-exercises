def cuenta_subcadenas_ax(cadena):
    As_hasta_i = 0
    total_hasta_i = 0
    for i in cadena:
        if i == "A":
            As_hasta_i += 1
        if i == "X":
            total_hasta_i += As_hasta_i
    return total_hasta_i


cuenta_subcadenas_ax('david')
