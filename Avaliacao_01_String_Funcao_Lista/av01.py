def contador(string):
    contador = 0
    for c in range(2, -1, -1):
        if string[2-c] == '*':
            contador += 2**c
    return contador


countGrito = countPiscada = 0
while True:
    grito = input()
    if grito == 'caw caw':
        print(countPiscada)
        countGrito += 1
        countPiscada = 0
        if countGrito == 3:
            break
    else:
        countPiscada += contador(grito)
