import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def semOrdenacao(lista):
    pass

def pesquisaLinear(lista, elemento_desejado):
    posicao = 0
    for item in lista:
        if(item == elemento_desejado):
            return posicao
        posicao = posicao + 1

    return -1

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))

    #Dados da ordenação
    
    inicio_ordenacao = time.time()
    print("Tempo inicial da ordenação: %f"%(inicio_ordenacao))

    semOrdenacao(lista)

    fim_ordenacao = time.time()
    print("Tempo final da ordenação: %f"%(fim_ordenacao))

    tempoTotal_ordenacao = fim_ordenacao - inicio_ordenacao
    print("O tempo total da ordenação foi %f"%(tempoTotal_ordenacao))

   
   
   
    #Dados da pesquisa

    inicio_pesquisa = time.time() 
    print("tempo inicial da pesquisa: %f"%(inicio_pesquisa))

    posicao = pesquisaLinear(lista, 2500)
    print("Posição do item é %d"%(posicao))

    fim_pesquisa = time.time() 
    print("Tempo final da pesquisa: %f"%(fim_pesquisa)) 

    tempototal_pesquisa = fim_pesquisa - inicio_pesquisa
    print ("O tempo total da pesquisa foi %f "%(tempototal_pesquisa))

    inicio_pesquisa_ordenacao = time.time() 
    print ("Tempo inicial da pesquisa_ordenacao: %f"% (inicio_pesquisa_ordenacao))

    semOrdenacao(lista)
    posicao = pesquisaLinear(lista, 2500)

    fim_pesquisa_ordenacao = time.time()
    print ("Tempo final da pesquisa_ordenacao: %f "%(fim_pesquisa_ordenacao))

    tempototal_pesquisa_ordenacao = tempototal_pesquisa + tempoTotal_ordenacao
    print ("O tempo total da pesquisa_ordenacao: %f"%(tempototal_pesquisa_ordenacao))





if (__name__ == "__main__"):
    main()
