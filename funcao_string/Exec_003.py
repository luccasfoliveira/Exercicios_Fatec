def decimalBase(numero, destino):
    B = "01"
    if destino == 8:
        B = "01234567"
    elif destino == 16:
        B = "0123456789ABCDEF"
    conversor = ''
    while numero != 0:
        conversor += B[numero % destino]
        numero //= destino
    return int(conversor[::-1]) if conversor.isdigit() else conversor[::-1]


def baseDecimal(destino, numero):
    B = "01"
    if destino == 8:
        B = "01234567"
    elif destino == 16:
        B = "0123456789ABCDEF"

    conversor = 0
    x = 1
    for i in numero[::-1]:
        conversor += x * int(i)
        x *= destino
    return conversor


base = int(input("Digite a Base: "))
numero = input("Digite o número: ")
conversao = int(input("Conversão: "))

if base != 10 and conversao != 10:
    print(decimalBase(baseDecimal(base, numero), conversao))
elif base == 10 and conversao != 10:
    print(decimalBase(int(numero), conversao))
else:
    print(baseDecimal(base, numero))
