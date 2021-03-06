import time
import random

# Adicionar as fun��es de Ordenamento e Pesquisa.
def bubble_sort(lista):
    comps = 0
    trocas = 0
    for i in range(len(lista)):
        for c in range(i+1,len(lista)):
            comps+=1
            if(lista[c] < lista[i]):#trocar
                trocas+=1
                aux = lista[i]
                lista[i] = lista[c]
                lista[c] = aux
    print("COMP: %d"%(comps))
    print("TROCAS: %d"%(trocas))

    return lista

def bb(lista,x):

    ini = 0
    fim = len(lista)-1
    pos = -1
    cont = 0

    while(ini<=fim):
        meio = (ini+fim)//2
        cont+=1
        if(lista[meio]==x):
            pos = meio
            break
        elif(lista[meio]>x):
            cont+=1
            fim = meio-1
        else:
            cont+=1
            ini = meio+1

    print("CONT: %d"%(cont))
    return pos
        

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


def pesquisaLinear(lista, elemento_desejado):
    comp = 0
    posicao = -1
    for item in lista:
        posicao = posicao + 1
        comp += 1
        if(item == elemento_desejado):
            break
    print("LINEAR_COMPS: %d"%(comp))

    return posicao

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)

#Contar o tempo da ordena��o

    inicio = time.time()
    print("Tempo inicial da ordena��o: %f"%(inicio))

    mergeSort(lista)

    fim = time.time()
    print("Tempo final da ordena��o: %f"%(fim))
    
    tempoTotal1 = fim - inicio
    print("Tempo Total da ordena��o %f"%(tempoTotal1))

#Contar o tempo da pesquisa

    inicio = time.time()
    print("Tempo inicial da pesquisa: %f"%(inicio))

    posicao = pesquisaLinear(lista, 7500)
    print("Posi��o do item  %d"%(posicao))

    fim = time.time()
    print("Tempo final da pesquisa: %f"%(fim))

    tempoTotal2 = fim - inicio
    print("O tempo total da pesquisa: %f"%(tempoTotal2))

    TempoTotal = tempoTotal1 + tempoTotal2
    print ("O tempo Total: %f" % (TempoTotal))

if (__name__ == "__main__"):
    main()
