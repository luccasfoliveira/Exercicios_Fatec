codificada = input("Mensagem Codificada: ").split()
decodificada = ''
espaco = 0
for i in codificada:
    for j in i[1::2]:
        decodificada += j
    espaco += 1
    if espaco < len(codificada):
        decodificada += ' '
print("Mensagem decodificada:", decodificada)
