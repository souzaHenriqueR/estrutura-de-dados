import random

def sortearGanhador():
    lista = []    
    qtdPessoas = int(input("Informe quantas pessoas participam do sorteio : "))
    for i in range(qtdPessoas):
        pessoa = (input("Informe o nome do participante : "))
        lista.append(pessoa)
    random.shuffle(lista)
    ganhador = random.choice(lista)
    
    return print(f"O ganhador foi : {ganhador}")


sortearGanhador()