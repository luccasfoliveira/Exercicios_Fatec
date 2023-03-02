def primo(valor):
    if (valor % 2 == 0 and valor != 2) or valor == 1:
        return False
    for i in range(3, int(valor**.5) + 1):
        if valor % i == 0:
            return False
    return True


inicio = int(input('Digite o Início: '))
fim = int(input('Digite o Fim: '))

for i in range(inicio, fim+1):
    if primo(i):
        print(f'O número {i} é primo...')
