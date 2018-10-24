import time 

import random 

  

# Adicionar as funções de Ordenamento e Pesquisa. 


def MergeSort(lista):
    if len(lista)>1:
        mid = len(lista)//2
        E = lista[:mid]
        D = lista[mid:]

        MergeSort(E)
        MergeSort(D)

        M = 0
        N = 0
        O = 0
        while M < len(E) and N < len(direita):
            if E[M] < D[N]:
                lista[O] = E[M]
                M += 1
            else:
                lista[O] = D[N]
                N += 1
            O += 1

        while M < len(E):
            lista[O] = E[M]
            M += 1
            O += 1

        while a < len(D):
            lista[O] = D[N]
            N += 1
            O += 1


def pesquisaLinear(lista, elemento_desejado):
    posicao = 0
    cont = 0
    for item in lista:
        cont = cont + 1
        if(item == elemento_desejado):
            print("A quantidade de comparações da pesquisa foi: %d"%(cont))
            return posicao
        posicao = posicao + 1

    return -1


  

# Programa principal 

def main():
    lista = list(range(1, 150+1))
    random.shuffle(lista)
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

    posicao = pesquisaLinear(lista, 75)  
    print("Posição do item é %d"%(posicao))  

    fimPesquisa = time.time()  
    print("Tempo final da Pesquisa: %f"%(fimPesquisa))  

    tempoTotaldaPesquisa = fimPesquisa - inicioPesquisa 
    print("O tempo total da Pesquisa %f"%(tempoTotaldaPesquisa))  

    inicioOrdenacaoPesquisa = time.time()  
    print("Tempo inicial: %f"%(inicioOrdenacaoPesquisa))  
 
    MergeSort(lista)
    posicao = pesquisaLinear(lista, 75)    

    fimOrdenacaoPesquisa = time.time()  
    print("Tempo final: %f"%(fimOrdenacaoPesquisa))  

    tempoTotal = fimOrdenacaoPesquisa - inicioOrdenacaoPesquisa  
    print("O tempo total foi %f"%(tempoTotal))

    print("O numero de comparacoes na ordenacao foi: %d"%(len(lista)**2)
  
if (__name__ == "__main__"):
    main()  
