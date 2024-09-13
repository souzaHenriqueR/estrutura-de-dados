
def melhorPiorNadador(qtdAtletas):
    listaNomes = []
    listaTempos = []

    for i in range(qtdAtletas):
        listaNomes.append(input("Informe o nome do atleta "))
        listaTempos.append(int(input("Informe o tempo do atleta : ")))

    tempoMelhorAtleta = min(listaTempos)
    indiceMelhorAtleta = listaTempos.index(tempoMelhorAtleta)
    nomeMelhorAtleta = listaNomes[indiceMelhorAtleta]

    tempoPiorAtleta = max(listaTempos)
    indicePiorAtleta = listaTempos.index(tempoPiorAtleta)
    nomePiorAtleta = listaNomes[indicePiorAtleta]

    somaTempoMedio = listaTempos[0]
    for i in range(len(listaTempos)):
        somaTempoMedio += listaTempos[i]

    tempoMedio = somaTempoMedio / qtdAtletas


    return print(f"O melhor atleta foi {nomeMelhorAtleta} com tempo : {tempoMelhorAtleta}s\ne o pior atleta foi {nomePiorAtleta} com o tempo : {tempoPiorAtleta}s \ne o tempo medio foi : {tempoMedio:.2f} ")



melhorPiorNadador(5)