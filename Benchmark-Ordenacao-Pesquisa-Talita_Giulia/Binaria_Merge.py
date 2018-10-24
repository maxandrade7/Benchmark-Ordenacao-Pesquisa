import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def bubble_sort(lista):
    comparacoes = 0
    t = 0
    for i in range(len(lista)):
        for c in range(i+1,len(lista)):
            comparacoes+=1
            if(lista[c] < lista[i]):#trocar
                t+=1
                aux = lista[i]
                lista[i] = lista[c]
                lista[c] = aux
    print("comparacao: %d"%(comparacoes))
    print("t: %d"%(t))

    return lista

def buscaBinaria(lista,x):

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
        

def mergeSort(lista):
    if len(lista)>1:
        mid = len(lista)//2
        esquerda = lista[:mid]
        direita = lista[mid:]

        mergeSort(esquerda)
        mergeSort(direita)

        i=0
        a=0
        b=0
        while i < len(esquerda) and a < len(direita):
            if esquerda[i] < direita[a]:
                lista[b]=esquerda[i]
                i=i+1
            else:
                lista[b]=direita[a]
                a=a+1
            b=b+1

        while i < len(esquerda):
            lista[b]=esquerda[i]
            i=i+1
            b=b+1

        while a < len(direita):
            lista[b]=direita[a]
            a=a+1
            b=b+1


def pesquisaLinear(lista, elemento_deseaado):
    comparacao = 0
    posicao = -1
    for item in lista:
        posicao = posicao + 1
        comparacao += 1
        if(item == elemento_deseaado):
            break
    print(comparacao)

    return posicao

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    mergeSort(lista)

    fim = time.time()
    print("Tempo final: %f"%(fim))

    print("%f"%(fim-inicio))

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    posicao = buscaBinaria(lista, 7500)
    print("Posi�ao do item  %d"%(posicao))

    fim = time.time()
    print("Tempo final: %f"%(fim))

    tempoTotal = fim - inicio
    print("O tempo total foi %f"%(tempoTotal))

if (__name__ == "__main__"):
    main()
