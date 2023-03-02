texto = input("É Polindromo? --> ")
textoMaiusculo = texto[::-1].upper()
if texto.upper() == textoMaiusculo:
    print("Polindromo")
else:
    print("Não é Palíndromo")
