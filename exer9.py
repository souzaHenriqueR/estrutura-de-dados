def vefMatrizDiag(qtdColunas,qtdLinhas):    
    if qtdColunas != qtdLinhas:
        return print("Valores informados não podem formar uma matriz quadrada.")
    
    m = []
    for i in range(qtdLinhas):
        l = [] 
        for j in range(qtdColunas):
            valor = int(input(f"Informe o valor : "))
            l.append(valor)
        m.append(l)
    
    for i in range(qtdLinhas):
        for j in range(qtdColunas):
            if i != j and m[i][j] != 0:
                return print("A matriz não é diagonal.")
    
    return print("A matriz é diagonal.")

vefMatrizDiag(4,4)