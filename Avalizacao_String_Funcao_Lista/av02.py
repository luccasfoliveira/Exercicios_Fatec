from random import randint, sample


palavras = ['python', 'java', 'javascript', 'cobol', 'ruby', 'scala', 'pascal', 'kotlin', 'elixir', 'haskell']

def embaralhar(palavra):
    return ''.join(sample(palavra, len(palavra)))

palavraSecreta = palavras[randint(0, len(palavras))]
palavraSortida = embaralhar(palavraSecreta)


print("Advinhe a linguagem de Programação... [6 tentativas]")
for i in range(1, 7):
    print(palavraSortida)
    opcao = input(f"Tentativa {i} - Decodifique a palavra acima: ").lower()
    if palavraSecreta == opcao:
        print("Parabens vc acertou")
        break
    print(f'Vc errou e tem {6 - i} tentativas')
