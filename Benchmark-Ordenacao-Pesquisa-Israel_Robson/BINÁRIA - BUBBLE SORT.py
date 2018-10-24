import random
import time

#Funções de Ordenamento e Pesquisa.
def bubble_sort(lista):
    comparacoes = 0
    trocas = 0
    for i in range(len(lista)):
        for d in range(i+1,len(lista)):
            comparacoes+=1
            if(lista[d] < lista[i]):
                trocas+=1
                aux = lista[i]
                lista[i] = lista[d]
                lista[d] = aux
    print("comrações: %d"%(comparacoes))
    print("trocas: %d"%(trocas))

    return lista

def bb(lista,x):

    inicio = 0
    fim = len(lista)-1
    posicao = -1
    contador = 0

    while(inicio<=fim):
        meio = (inicio+fim)//2
        contador+=1
        if(lista[meio]==x):
            posicao = meio
            break
        elif(lista[meio]>x):
            contador+=1
            fim = meio-1
        else:
            contador+=1
            inicio = meio+1

    print("contador: %d"%(contador))
    return posicao
        

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

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

        while i < len(lefthalf):
            alist[s]=lefthalf[x]
            x=x+1
            s=s+1

        while j < len(righthalf):
            alist[s]=righthalf[a]
            a=a+1
            s=s+1


def pesquisaLinear(lista, elemento_desejado):
    comp = 0
    posicao = -1
    for item in lista:
        posicao = posicao + 1
        comp += 1
        if(item == elemento_desejado):
            break
    print(comp)

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

    posicao = bb(lista, 7500)
    print("PosiçãoItem : %d"%(posicao))

    fim = time.time()
    print("TempoFinal: %f"%(fim))

    tempoTotal = fim - inicio
    print("TempoTotal : %f"%(tempoTotal))

if (__name__ == "__main__"):
    main()
