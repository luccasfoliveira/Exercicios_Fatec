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


texto = input("Digite o texto: ")
for i in texto:
    print(embaralhar(i), end=' ')
