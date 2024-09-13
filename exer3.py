import random
'''
def sortearGanhador(qtdPessoas):
    lista = []    
    for i in range(qtdPessoas):
        pessoa = (input("Informe o nome do participante : "))
        lista.append(pessoa)
    random.shuffle(lista)
    ganhador = random.choice(lista)
    
    return print(f"O ganhador foi : {ganhador}")


sortearGanhador(3)'''

listaNomes = ["henmrique","joão","kauna","kiki"]


def sortearGanhador(qtdPessoas = 0,lista = None):
    if lista == None:
        lista = []
        for i in range(qtdPessoas):
            lista.append(input("Informe o nome do participante : "))
        random.shuffle(lista)
        ganhador = random.choice(lista)
        
        return print(f"O ganhador do sorteio foi : {ganhador}")
    else:
         random.shuffle(lista)
         ganhador = random.choice(lista)
         return print(f"O ganhador foi {ganhador}")
        

sortearGanhador(qtdPessoas=5)

        
        
    
    