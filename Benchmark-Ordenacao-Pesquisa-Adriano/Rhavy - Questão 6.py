import time 

import random 

  

# Adicionar as funções de Ordenamento e Pesquisa. 

def MergeSort(lista):
    if len(lista)>1:
        mid = len(lista)//2
        esquerda = lista[:mid]
        direita = lista[mid:]

        MergeSort(esquerda)
        MergeSort(direita)

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

  

def pesquisaBinaria(lista, item):

    Inicio = 0
    final = len(lista)-1
    posicao = -1
    cont = 0

    while(Inicio<=final):
        meio = (Inicio+final)//2

        if(lista[meio] == item):
            cont += 1
            posicao = meio
            break
        elif(lista[meio] > item):
            cont += 1
            final = meio-1
        else:
            cont += 1
            Inicio = meio+1

    print("O numero de comparacoes na pesquisa foi: %d"%(posicao))

    return posicao



  

# Programa principal 

def main():

    lista = list(range(1, 15000+1))
    #   "random.shuffle(lista)" retirado pois a pesquisa Binária so pesquisa elementos em listas ordenadas 
    print("Tamanho da lista: %d"%(len(lista))) 

    inicioOrdenacao = time.time() 
    print("Tempo inicial da Ordenacao: %f"%(inicioOrdenacao)) 

    MergeSort(lista) 

    fimOrdenacao = time.time() 
    print("Tempo final da Ordenacao: %f"%(fimOrdenacao)) 

    tempoTotaldaOrdenacao = fimOrdenacao - inicioOrdenacao 
    print("O tempo total da Ordenacao foi %f"%(tempoTotaldaOrdenacao)) 

    inicioPesquisa = time.time() 
    print("Tempo inicial da Pesquisa: %f"%(inicioPesquisa)) 

    posicao = pesquisaBinaria(lista, 7500) 
    print("Posição do item é %d"%(posicao)) 

    fimPesquisa = time.time() 
    print("Tempo final da Pesquisa: %f"%(fimPesquisa)) 

    tempoTotaldaPesquisa = fimPesquisa - inicioPesquisa
    print("O tempo total da Pesquisa %f"%(tempoTotaldaPesquisa)) 

    inicioOrdenacaoPesquisa = time.time() 
    print("Tempo inicial: %f"%(inicioOrdenacaoPesquisa)) 

    MergeSort(lista) 
    posicao = pesquisaBinaria(lista, 7500)  

    fimOrdenacaoPesquisa = time.time() 
    print("Tempo final: %f"%(fimOrdenacaoPesquisa)) 

    tempoTotal = fimOrdenacaoPesquisa - inicioOrdenacaoPesquisa 
    print("O tempo total foi %f"%(tempoTotal)) 

if (__name__ == "__main__"): 
    main() 

