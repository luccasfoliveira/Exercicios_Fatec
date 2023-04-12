def embaralhar(palavra):
    if len(palavra) > 3:
        primeiraLetra = palavra[0]
        ultimaLetra = palavra[len(palavra) - 1]
        palavra = list(palavra[1:len(palavra) - 1])

        x = 1
        while x < len(palavra):
            aux = palavra[x - 1]
            palavra[x - 1] = palavra[x]
            palavra[x] = aux
            x += 2
        return primeiraLetra + ''.join(palavra) + ultimaLetra
    return palavra


texto = input("Digite o texto: ").split()
for i in texto:
<<<<<<< HEAD
    print(embaralhar(i), end=' ')
=======
    if not i[-1].isalnum():
        print(embaralhar(i[:-1]) + i[-1], end=' ')
    else:
        print(embaralhar(i), end=' ')

>>>>>>> 979f2baa4be45bb03390ff71152bde019a2f1968
