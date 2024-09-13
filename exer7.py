
import random
def verificarMatriz(qtdColunas,qtdLinhas):
    m = []
    for i in range(qtdColunas):
        l = [] 
        for i in range(qtdLinhas):
            valor = random.randint(0,1)
            l.append(valor)
        m.append(l)
    
    soma = 0
    for i in range(qtdColunas):
        for j in range(qtdLinhas):
            soma += m[i][j] 
    
    if (soma == 0):
        return print(f"A matriz é nula")
    elif(soma > 1):
        print(f"A matriz não é nula")
      

verificarMatriz(2,1)
        
    
    