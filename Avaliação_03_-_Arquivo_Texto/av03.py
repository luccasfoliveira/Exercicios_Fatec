def limpar() -> None:
    from os import system


    system('cls') or None

def validar_usuario(usarname: str) -> bool:
    if len(usarname) > 8:
        especial = letra = numero = False
        for caracter in usarname:
            if caracter in ['_', '.']:
                especial = True
            elif caracter.isalpha():
                letra = True
            elif caracter.isdigit():
                numero = True
            if especial and letra and numero:
                return True
    return False

def validar_senha(password: str) -> bool:
    if len(password) > 8:
        maiuscula = numero = letra = especial = False
        for caracter in password:
            if caracter.isupper():
                maiuscula = True
            elif caracter in ['_', '.']:
                especial = True
            elif caracter.isalpha():
                letra = True
            elif caracter.isdigit():
                numero = True
            if especial and letra and numero and maiuscula:
                return True
    return False

def consultar_usuario(usarname: str) -> bool:
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                usuario = linha.split(";")
                if usuario[0] == usarname:
                    return True
    except FileNotFoundError:
        with open("usuarios.txt", "a+") as arquivo:
            for linha in arquivo:
                usuario = linha.split(";")
                if usuario[0] == usarname:
                    return True
    return False

def consultar_senha(password: str) -> bool:
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            senha = linha.split(";")
            senha = senha[1][:-1]
            if criptografar_senha(password) == senha:
                return True
    return False

def cadastrar_usuario_senha(usarname: str, password: str) -> None:
    with open("usuarios.txt", "a+") as arquivo:
        arquivo.write(f"{usarname};{password}\n")
        
def criptografar_senha(password: str) -> str:
    newSenha = ''
    for caracter in password:
        newCaracter = ord(caracter)
        newSenha += chr(newCaracter+1) + chr(newCaracter+2)
    return newSenha

def tela(frase: str, caracter: str, tamanho: int) -> None:
    print(frase.center(tamanho, caracter))


def menu() -> None:
    tela(" TELA DE LOGIN " ,"=", 50)
    opcao = input("JÁ POSSUI CADASTRO [SIM/NÃO]: ").strip().upper()[0]
    if opcao == 'S':
        for i in range(3):
            limpar()
            tela(" DIGITE SEU USUÁRIO: ", "*", 50)
            usuario = input("Usuário -> ")
            if validar_usuario(usuario) and consultar_usuario(usuario):
                break
        if i == 2:
            tela(" (3x) ACESSO NEGADO ", "*", 50)
            return

        for i in range(3):
            limpar()
            print(F"Usuário -> {usuario}")
            tela(" DIGITE SUA SENHA: ", "*", 50)
            senha = input("Senha -> ")
            if validar_senha(senha) and consultar_senha(senha):
                limpar()
                tela(" ACESSO LIBERADO ", "*", 50)
                return
        if i == 2:
            tela(" (3x) ACESSO NEGADO ", "*", 50)
            return

    elif opcao == 'N':
        titulo = " TELA DE CADASTRO "
        while True:
            limpar()
            tela(titulo, "*", 50)
            print('DIGITE O USUÁRIO: \n'
                '1. Maior que 8 caracteres\n'
                '2. Conter letra e número\n'
                '3. Conter um "_" ou "."\n')
            usuario = input("Usuário -> ")
            if validar_usuario(usuario) and not consultar_usuario(usuario):
                break
            titulo = " USUÁRIO INVÁLIDO OU JÁ CADASTRADO "
        
        titulo = " USUÁRIO VÁLIDO "
        while True:
            limpar()
            tela(titulo, "=", 50)
            print('DIGITE A SENHA: \n'
                    '1. Maior que 8 caracteres\n'
                    '2. Conter letra Maiúscula e número\n'
                    '3. Conter um "_" ou "."\n')
            print(F"Usuário -> {usuario}")
            senha = input("Senha -> ")
            if senha == usuario:
                limpar()
                titulo = " USUÁRIO E SENHA IGUAIS :( "
            elif validar_senha(senha):
                senha = criptografar_senha(senha)
                break 

        cadastrar_usuario_senha(usuario, senha)
        limpar()
        tela(" USUÁRIO E SENHA CADASTRADOS ", "*", 50)

    else:
        limpar()
        tela(" OPÇÃO INVÁLIDA ", "=", 50)
        tela(" OBRIGADO PELA VISITA ", "=", 50)

menu()
