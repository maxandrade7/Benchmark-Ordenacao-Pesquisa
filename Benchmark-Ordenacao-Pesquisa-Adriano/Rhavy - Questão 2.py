import time 
import random 

  

# Adicionar as funções de Ordenamento e Pesquisa. 

def semOrdenacao(lista): 
    pass 

  
def pesquisaBinaria(lista, esquerda, direita, item):
    
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    
    if lista[meio] == item:
        return meio
    
    elif lista[meio] > item:
        return pesquisaBinaria(lista, esquerda, meio - 1, item)
    else: 
        return pesquisaBinaria(lista, meio + 1, direita, item)


  

# Programa principal 

def main():

    lista = list(range(1, 15000+1))
#   "random.shuffle(lista)" retirado pois a pesquisa Binária so pesquisa elementos em listas ordenadas 
    esquerda = lista[0]
    direita = lista[-1]
    print("Tamanho da lista: %d"%(len(lista))) 

    inicioOrdenacao = time.time() 
    print("Tempo inicial da Ordenacao: %f"%(inicioOrdenacao)) 
  
    semOrdenacao(lista)

    fimOrdenacao = time.time() 
    print("Tempo final da Ordenacao: %f"%(fimOrdenacao))  

    tempoTotaldaOrdenacao = fimOrdenacao - inicioOrdenacao 
    print("O tempo total da Ordenacao foi %f"%(tempoTotaldaOrdenacao))     

    inicioPesquisa = time.time() 
    print("Tempo inicial da Pesquisa: %f"%(inicioPesquisa)) 

    posicaoNum_Comparacao = pesquisaBinaria(lista, esquerda, direita, 7500) 
    print("Posição do item é %d"%(posicaoNum_Comparacao)) 

    fimPesquisa = time.time() 
    print("Tempo final da Pesquisa: %f"%(fimPesquisa)) 

    tempoTotaldaPesquisa = fimPesquisa - inicioPesquisa
    print("O tempo total da Pesquisa %f"%(tempoTotaldaPesquisa)) 

    inicioOrdenacaoPesquisa = time.time() 
    print("Tempo inicial: %f"%(inicioOrdenacaoPesquisa)) 

    semOrdenacao(lista) 
    posicaoNum_Comparacao = pesquisaBinaria(lista, esquerda, direita, 7500) 

    fimOrdenacaoPesquisa = time.time() 
    print("Tempo final: %f"%(fimOrdenacaoPesquisa)) 

    tempoTotal = fimOrdenacaoPesquisa - inicioOrdenacaoPesquisa 
    print("O tempo total foi %f"%(tempoTotal))

    print("O numero de comparacoes na ordenacao foi: %d"%(0))
    print("O numero de trocas na ordenacao foi: %d"%(0))
    print("O numero de comparacoes na Pesquisa foi: %d"%(posicaoNum_Comparacao))

if (__name__ == "__main__"):
    main() 

 
