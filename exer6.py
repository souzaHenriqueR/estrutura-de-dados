def mediaGeometricaTotal():
    qtdNumeros = int(input("Informe quantos elementos serão inseridos : "))
    lista = []
    for i in range(qtdNumeros):
        numero = int(input("Informe o número a ser inserido : "))
        lista.append(numero)
    
    multNums = 1
    for i in range(qtdNumeros):
        multNums *= lista[i]
        
    base = multNums
    expoente = 1/qtdNumeros
    mGeometricaTotal = base **expoente
    
    return print(f"A media geometrica da lista {lista} é : {mGeometricaTotal:.2f}")

mediaGeometricaTotal()