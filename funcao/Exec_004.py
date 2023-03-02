def primo(valor):
    if (valor % 2 == 0 and valor != 2) or valor == 1:
        return False
    for i in range(3, int(valor**.5) + 1):
        if valor % i == 0:
            return False
    return True
