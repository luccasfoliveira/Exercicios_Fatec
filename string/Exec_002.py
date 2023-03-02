from unidecode import unidecode

count = 0
texto = input("Texto: ")
f = unidecode(texto.upper())
for letra in "AEIOU":
    count += f.count(letra)

print(f'Há {count} vogais')
