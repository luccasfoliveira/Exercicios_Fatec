from unidecode import unidecode
from string import ascii_lowercase, ascii_uppercase

maiusculo = ascii_uppercase
minusculo = ascii_lowercase
senha = ''

texto = unidecode(input("Texto: "))
for i in texto:
    if i in maiusculo:
        senha += maiusculo[(maiusculo.index(i) + 3) % 26]
    elif i in minusculo:
        senha += maiusculo[(minusculo.index(i) + 3) % 26]
    else:
        senha += i

print(f'Nova senha: {senha}')