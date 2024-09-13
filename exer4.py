def calcFatorMeioLista(qtdNumeros):
    lista = []
    for i in range(qtdNumeros):
        numero = int(input("Informe o número : "))
        lista.append(numero)
        
    indexElementoMeio = len(lista) // 2
    elementoMeio = lista[indexElementoMeio]
    fat = 1
    
    for i in range(elementoMeio,1,-1):
        fat *= i
    
    return print(f"O fatorial de {elementoMeio} é {fat}")

calcFatorMeioLista(5)