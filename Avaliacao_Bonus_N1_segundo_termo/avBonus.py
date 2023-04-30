def converterNumEmTexto(numero):
    def unidade(numero):
        return numero % 10

    def dezena(numero):
        return numero // 10

    if 10 <= numero <= 19:
        lista_especial = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
        print(lista_especial[unidade(numero)])
    else:
        lista_unidade = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
        if numero <= 9:
            print(lista_unidade[numero - 1])
        else:
            lista_dezena = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
            print(f'{lista_dezena[dezena(numero) - 2]} e {lista_unidade[unidade(numero) - 1]}')


converterNumEmTexto(int(input()))
