from random import randint


def maiorEleColuna(lista, coluna):
    maior = lista[0][coluna - 1]
    for i in range(1, len(lista)):
        if lista[i][coluna - 1] > maior:
            maior = lista[i][coluna - 1]
    return maior


def menorEleLinha(lista, linha):
    menor = lista[linha - 1][0]
    for i in lista[linha - 1][1::]:
        if menor > i:
            menor = i
    return menor


L = [0] * 10
for linha in range(10):
    L[linha] = [0] * 5
    for coluna in range(5):
        L[linha][coluna] = randint(10, 90)
    print(*L[linha])


print(maiorEleColuna(L, 5))
print(menorEleLinha(L, 5))
