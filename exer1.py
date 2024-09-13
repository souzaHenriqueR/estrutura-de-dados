def progAritmetica(priTermo,qtdTermos,razao):
    lista = []
    lista.append(priTermo)

    for i in range(qtdTermos -1 ):
        lista.append(lista[i] + razao)

    return print(lista)

progAritmetica(2,10,7)