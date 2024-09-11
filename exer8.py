def vefMatrizId():
    qtdColunas = int(input("Informe o número de colunas da matriz : "))
    qtdLinhas = int(input("Informe o número de linhas da matriz : "))
    
    if (qtdColunas != qtdLinhas):
        return print("Valores informados não podem formar uma matriz identidade")
    
    m = []
    for i in range(qtdColunas):
        l = [] 
        for i in range(qtdLinhas):
            valor = int(input("Informe o valor a ser inserido : 1 ou 0 "))
            l.append(valor)
        m.append(l)
        
    diagonal = 0
    soma = 0
    for i in range(qtdColunas):
        for j in range(qtdLinhas):
            soma += m[i][j]
            if (i == j):
                diagonal += m[i][j]   
    
    if (soma > diagonal):
        return print("Matriz não é identidade")
    if (soma == diagonal and soma and diagonal > 0):
        return print("Matriz identidade")
    else:
        return print("Matriz nula")
      
vefMatrizId()
        
    