palavra = input("Palavra: ")
metade = len(palavra) // 2
if len(palavra) % 2 == 0:
    print(palavra[metade-1:metade+1])
else:
    print(palavra[metade:metade+1])
