cpf = input("Digite seu CPF: ").strip()
string = str()

for numero in cpf:
    if numero.isdigit():
        string += numero

if len(string) != 11:
    print("CPF ERRADO")
else:
    penDigito = int(string[9])
    segDigito = int(string[10])

    calculoUm = calculoDois = int()
    for i, e in enumerate(string[:9]):
        calculoUm += (i+1) * int(e)
        calculoDois += (9-i) * int(e)

    calculoUm %= 11
    calculoDois %= 11

    if calculoUm == 10:
        calculoUm = 0
    if calculoDois == 10:
        calculoDois = 0

    if str(calculoUm) == string[9] and str(calculoDois) == string[10]:
        print('CPF VÁLIDO')
    else:
        print('CPF NÃO É VÁLIDO')
