def vefMatrizEsparsa(qtdColunas=0,qtdLinhas=0,matriz=None):
    m = []
    for i in range(qtdLinhas):
        l = [] 
        for j in range(qtdColunas):
            valor = int(input(f"Informe o valor : "))
            l.append(valor)
        m.append(l)
    
   
    count_zeros = 0
    total_elementos = qtdLinhas * qtdColunas
    
    for i in range(qtdLinhas):
        for j in range(qtdColunas):
            if m[i][j] == 0:
                count_zeros += 1
    
    if count_zeros > total_elementos / 2:
        return print("A matriz é esparsa.")
    else:
        return print("A matriz não é esparsa.")

m = [[0,0],[0,0]]


vefMatrizEsparsa(2,2)

vefMatrizEsparsa(matriz=m)