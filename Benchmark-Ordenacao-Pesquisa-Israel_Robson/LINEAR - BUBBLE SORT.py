import random
import time

#funções de Ordenamento e Pesquisa.
def bubble_sort(lista):
    comparacoes = 0
    trocas = 0
    for i in range(len(lista)):
        for c in range(i+1,len(lista)):
            comparacoes+=1
            if(lista[c] < lista[i]):
                trocas+=1
                aux = lista[i]
                lista[i] = lista[c]
                lista[c] = aux
    print("comparações: %d"%(comparacoes))
    print("TROCAS: %d"%(trocas))

    return lista

def mergeSort(alista):
    if len(alista)>1:
        mide = len(alista)//2
        lefthalf = alista[:mide]
        righthalf = alista[mide:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        x=0
        a=0
        s=0
        while x < len(lefthalf) and a < len(righthalf):
            if lefthalf[x] < righthalf[a]:
                alist[s]=lefthalf[x]
                x=x+1
            else:
                alist[s]=righthalf[a]
                a=a+1
            k=k+1

        while x < len(lefthalf):
            alist[s]=lefthalf[x]
            x=x+1
            s=s+1

        while a < len(righthalf):
            alist[s]=righthalf[a]
            a=a+1
            s=s+1


def pesquisaLinear(lista, elementoDesejado):
    comparacao = 0
    posicao = -1
    for Item in lista:
        posicao = posicao + 1
        comparacao += 1
        if(Item == elementoDesejado):
            break
    print(comparacao)

    return posicao

# Programa primario
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)

    inicio = time.time()
    print("TempoInicial: %f"%(inicio))

    bubble_sort(lista)

    fim = time.time()
    print("TempoFinal: %f"%(fim))

    print("%f"%(fim-inicio))

    inicio = time.time()
    print("TempoInicial: %f"%(inicio))

    posicao = pesquisaLinear(lista, 7500)
    print("PosiçãoItem : %d"%(posicao))

    fim = time.time()
    print("TempoIinal: %f"%(fim))

    tempoTotal = fim - inicio
    print("TempoTotal : %f"%(tempoTotal))

if (__name__ == "__main__"):
    main()
