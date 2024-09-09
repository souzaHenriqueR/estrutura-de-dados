def progAritmetica():
    lista = []
    priTermo = int(input("Informe o primeiro termo : "))
    qtdTermos = int(input("Informe a quantidade de termos : "))
    razao = int(input("Informe a razão : "))
    lista.append(priTermo)

    for i in range(qtdTermos -1 ):
        lista.append(lista[i] + razao)

    return print(lista)

progAritmetica()