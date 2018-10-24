import time 

import random 

  

# Adicionar as funções de Ordenamento e Pesquisa. 

def BubbleSort(lista):
    trocas = 0
    if len(lista) <= 1:
        sA = lista
    else:
        for j in range(0,len(lista)):
            for i in range(0,len(lista)-1):
                if lista[i]>lista[i+1]:
                    trocas = trocas + 1
                    Aux = lista[i+1]
                    lista[i+1] = lista[i]
                    lista[i] = Aux
        sA = lista
    print("A quantidade de trocas foi: %d"%(trocas))
    return sA

  
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
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))

    inicioOrdenacao = time.time()
     
  
    BubbleSort(lista)  
  
    fimOrdenacao = time.time()  
    

    tempoTotaldaOrdenacao = fimOrdenacao - inicioOrdenacao  
    print("O tempo total da Ordenacao foi %f"%(tempoTotaldaOrdenacao))  
  
    inicioPesquisa = time.time()  
      

    posicao = pesquisaLinear(lista, 7500)  
    print("Posição do item é %d"%(posicao))  

    fimPesquisa = time.time()  
      

    tempoTotaldaPesquisa = fimPesquisa - inicioPesquisa 
    print("O tempo total da Pesquisa %f"%(tempoTotaldaPesquisa))  

    tempoTotal = tempoTotaldaOrdenacao + tempoTotaldaPesquisa
    print("O tempo total do código foi: %f"%(tempoTotal))

    print("A quantidade de comparações da ordenacao foi: %d"%(len(lista)**2))
  
if (__name__ == "__main__"):
    main()
