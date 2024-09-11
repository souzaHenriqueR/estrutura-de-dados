def mediaGeometrica():
    
    qtdNumeros = int(input("Informe quantos elementos serão inseridos : "))
    lista = []
    for i in range(qtdNumeros):
        numero = int(input("Informe o número a ser inserido : "))
        lista.append(numero)
    
    maior = max(lista)
    menor = min(lista)
    mGeomtrica =  ( (maior * menor) ** 0.5 )
    
    return print(f"A media é : {mGeomtrica:.2f}")

mediaGeometrica()