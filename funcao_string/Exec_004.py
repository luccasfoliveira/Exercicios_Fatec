def embaralhar(texto):
    from random import shuffle


    novoTexto = ''
    for i in texto:
        if len(i) > 3:
            novoTexto += texto[0] + shuffle(i[1::len(texto)]) + texto[len(texto)]
        else:
            novoTexto += i
    return novoTexto


texto = input("Digite um texto: ")
print(texto[0] + embaralhar(texto) + texto[len(texto) - 1])
