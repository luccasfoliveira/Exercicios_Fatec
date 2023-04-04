def validasenha(senha):
    if len(senha) == 8:
        caracter = maiuscula = numero = False
        for i in senha:
            if not i.isspace():
                if i.isdigit():
                    numero = True
                elif i.isupper():
                    maiuscula = True
                elif not i.isalnum():
                    caracter = True

                if caracter and maiuscula and numero:
                    return True
            else:
                return False
    return False


def gerarSenhaAleatoria():
    from random import sample

    pontuacao = '''!\#$%&'()*+,-./:";<=>?@[]^_`{|}~'''
    maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscula = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"

    senha = sample(pontuacao, 1) + sample(maiuscula, 3) + sample(numeros, 1) + sample(minuscula, 3)
    return ''.join(sample(senha, 8))


if validasenha(input("Digite a Senha: ")):
    print('Válida\nObrigado...')
else:
    print('Não é válida... :(')
    while True:
        resp = input("Deseja criar uma senha Aleatória? [S/N]: ")[0].upper().strip()
        if resp == "S" or resp == "N":
            if resp == 'S':
                print(gerarSenhaAleatoria())
            print("Obrigado...")
            break
        print("\nDigite S ou N [S/N]\n")
