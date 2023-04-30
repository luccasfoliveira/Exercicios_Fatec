def letraRepetida(texto):
    palavra = []
    for i in texto.lower():
        count = 0
        for j in texto.lower():
            if j == i:
                count += 1
            if count > 1:
                palavra += j
                break
    return palavra


print(*letraRepetida(input()))
