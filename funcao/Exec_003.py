def inverter(valor):
    if valor < 10:
        return valor
    else:
        inverte = int()
        while valor != 0:
            inverte = (inverte * 10) + (valor % 10)
            valor //= 10
        return inverte
