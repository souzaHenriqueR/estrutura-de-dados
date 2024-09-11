
import random
def verificarMatriz():
    
    qtdColunas = int(input("Informe o número de colunas da matriz : "))
    qtdLinhas = int(input("Informe o número de linhas da matriz : "))
    m = []
    for i in range(qtdColunas):
        l = [] 
        for i in range(qtdLinhas):
            valor = int(input("Informe o valor a ser inserido : 1 ou 0 "))
            l.append(valor)
        m.append(l)
    
    soma = 0
    diagonal = True
    
    for i in range(qtdColunas):
        for j in range(qtdLinhas):
            if (i == j):
                if (m[i][j] > 0 ):
                    diagonal = True
                else:
                    diagonal = False
    
    if (diagonal == True):
        return print("A matriz é identidade")
    else:
        return print("A matriz não é identidade")
      

verificarMatriz()
        
    