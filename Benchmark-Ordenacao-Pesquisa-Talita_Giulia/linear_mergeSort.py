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
    print("COMParacao: %d"%(comparacoes))
    print("t: %d"%(t))

    return lista

def Busca_Binaria(lista,x):

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

    print("CONTador: %d"%(contador))
    return posicao
        

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


def pesquisaLinear(lista, elemento_desejado):
    comparacao = 0
    posicao = -1
    for item in lista:
        posicao = posicao + 1
        comparacao += 1
        if(item == elemento_desejado):
            break
        
    print("linear comparacoes: %d"%(comparacao))

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

    iniciocio = time.time()
    print("Tempo inicial: %f"%(inicio))

    posicao = pesquisaLinear(lista, 7500)
    print("Posicao do item �: %d"%(posicao))

    fim = time.time()
    print("Tempo final: %f"%(fim))

    tempoTotal = fim - inicio
    print("O tempo total foi %f"%(tempoTotal))

if (__name__ == "__main__"):
    main()
