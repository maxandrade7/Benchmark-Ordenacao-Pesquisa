import random
import time

# funções de pesquisa e de Ordenamento
def bubble_sort(lista):
    comparacoes = 0
    trocas = 0
    for i in range(len(lista)):
        for a in range(i+1,len(lista)):
            comparacoes+=1
            if(lista[a] < lista[i]):
                trocas+=1
                aux = lista[i]
                lista[i] = lista[c]
                lista[a] = aux
    print("Comparações: %d"%(comparacoes))
    print("Trocas: %d"%(trocas))

    return lista

def mergeSort(alista):
    if len(alista)>1:
        mid = len(alista)//2
        lefthalf = alista[:mid]
        righthalf = alista[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        x=0
        i=0
        j=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alista[k]=lefthalf[i]
                i=i+1
            else:
                alista[k]=righthalf[j]
                j=j+1
            x=x+1

        while i < len(lefthalf):
            alista[k]=lefthalf[i]
            i=i+1
            x=x+1

        while j < len(righthalf):
            alista[k]=righthalf[j]
            j=j+1
            x=x+1


def pesquisaLinear(listA, elementoDesejado):
    compa = 0
    posicao = -1
    for item in listA:
        posicao = posicao + 1
        compa += 1
        if(item == elementoDesejado):
            break
    print(compa)

    return posicao

# Programa primario
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)

    comeco = time.time()
    print("Tempo inicial: %f"%(comeco))

    posicao = pesquisaLinear(lista, 7500)
    print("Posição do item é %d"%(posicao))

    fim = time.time()
    print("Tempo final: %f"%(fim))

    tempoTotal = fim - comeco
    print("O tempo total foi %f"%(tempoTotal))

if (__name__ == "__main__"):
    main()
