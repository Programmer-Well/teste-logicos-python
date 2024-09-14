while True:
    entrada = str(input('Entre com alguma palavra para inverter: '))

    if bool(entrada):
        string_invertida = entrada[::-1]
        print(string_invertida)
    else:
        entrada = str(input('Entre apenas com strigns, tente novamente: '))
