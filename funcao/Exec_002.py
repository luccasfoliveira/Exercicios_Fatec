def potencia(base, expoente):
    valor = 1
    for i in range(1, expoente + 1):
        valor *= base
    return valor
