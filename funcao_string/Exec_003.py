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


def baseNumero(destino, numero):
    B = "01"
    if destino == 8:
        B = "01234567"
    elif destino == 16:
        B = "0123456789ABCDEF"

    conversor = 0
    x = len(numero)-1
    for i in numero:
        conversor += destino ** x * B.index(i)
        x -= 1
    return conversor


def validacaoBase(base, numero):
    B = "01"
    if base == 8:
        B = "01234567"
    elif base == 16:
        B = "0123456789ABCDEF"
    elif base == 10:
        B = "0123456789"

    for i in numero:
        if i not in B:
            return False
    return True


print("*" * 30 + " CONVERSÃO DE BASES " + "*" * 30)
base = int(input("\nDigite a Base de Origem: "))
while True:
    numero = input("Digite um número da Base acima: ").upper()
    if validacaoBase(base, numero):
        break
    print("Digite um número válido para a Base....\n")

conversao = int(input("Digite a Base que deseja Converter: "))
if base != 10 and conversao != 10:
    resultado = decimalBase(baseNumero(base, numero), conversao)
elif base == 10 and conversao != 10:
    resultado = decimalBase(int(numero), conversao)
else:
    resultado = baseNumero(base, numero)

print()
print("*" * 30 + " RESULTADO " + "*" * 30)
print(f"Número {numero} da base {base} corresponde a {resultado} da base {conversao}")
print("*" * 30 + " OBRIGADO " + "*" * 30)
