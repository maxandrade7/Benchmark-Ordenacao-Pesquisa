import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def semOrdenacao(lista):
    pass

def pesquisaLinear(lista, elemento_desejado):
    posicaoNum_Comparacao = 0
    for item in lista:
        if(item == elemento_desejado):
            return posicaoNum_Comparacao
        posicaoNum_Comparacao = posicaoNum_Comparacao + 1
        
    return -1
    
# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))

    inicioOrdenacao = time.time() 
    print("Tempo inicial da Ordenação: %f"%(inicioOrdenacao))   

    semOrdenacao(lista)   

    fimOrdenacao = time.time()   
    print("Tempo final da Ordenação: %f"%(fimOrdenacao)) 

    tempoTotaldaOrdenacao = fimOrdenacao - inicioOrdenacao   
    print("O tempo total da Ordenação foi %f"%(tempoTotaldaOrdenacao))   

    inicioPesquisa = time.time()   
    print("Tempo inicial da Pesquisa: %f"%(inicioPesquisa))   

    posicaoNum_Comparacao = pesquisaLinear(lista, 7500)   
    print("Posição do item é %d"%(posicaoNum_Comparacao))

    fimPesquisa = time.time()   
    print("Tempo final da Pesquisa: %f"%(fimPesquisa))

    tempoTotaldaPesquisa = fimPesquisa - inicioPesquisa  
    print("O tempo total da Pesquisa %f"%(tempoTotaldaPesquisa))   

    inicioOrdenacaoPesquisa = time.time()   
    print("Tempo inicial: %f"%(inicioOrdenacaoPesquisa))   

    semOrdenacao(lista) 
    posicaoNum_Comparacao = pesquisaLinear(lista, 7500)     

    fimOrdenacaoPesquisa = time.time()   
    print("Tempo final: %f"%(fimOrdenacaoPesquisa))   

    tempoTotal = fimOrdenacaoPesquisa - inicioOrdenacaoPesquisa   
    print("O tempo total foi %f"%(tempoTotal))

    print("O numero de comparações na ordenação foi: %d"%(0))
    print("O numero de trocas na ordenação foi: %d"%(0))
    print("O numero de comparacões na Pesquisa foi: %d"%(posicaoNum_Comparacao))

if (__name__ == "__main__"):
    main()

