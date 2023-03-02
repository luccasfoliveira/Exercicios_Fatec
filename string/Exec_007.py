from unidecode import unidecode

texto = input("Texto: ")
f = unidecode(texto.upper())
f = f.replace(" ", "")
vogais = int()
for vogal in 'AEIOU':
    vogais += f.count(vogal)

print(f'Código: {((len(f) - vogais) * 10) + vogais * 5}')
