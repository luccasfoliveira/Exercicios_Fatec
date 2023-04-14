from random import randint


def novaLista(lista, inicial, fim):
    listaNova = list()
    for i in lista:
        if i > fim:
            break
        if inicial <= i <= fim:
            listaNova.append(i)
    return listaNova


def validar(n1, n2):
    if n2 > n1:
        return True
    return False


L = list()
for i in range(15):
    L.append(randint(1, 50))
L.sort()

inicial = int(input('Inicial: '))
fim = int(input('Fim: '))

print(*L)
if validar(inicial, fim):
    print(*novaLista(L, inicial, fim))
else:
    inicial, fim = fim, inicial
    print(*novaLista(L, inicial, fim))
