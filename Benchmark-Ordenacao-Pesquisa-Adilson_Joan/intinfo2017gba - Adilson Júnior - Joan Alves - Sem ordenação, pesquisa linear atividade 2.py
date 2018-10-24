import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def semOrdenacao(lista):
    pass

def pesquisaBinaria(lista, item, E, D):
    if (D<E):
      return -1
    meio = (E+D)//2
  
    if (lista[meio]==item):
      return meio

    elif (item>lista[meio]):
      return pesquisaBinaria(lista, item, meio+1,D)

    else:
      return pesquisaBinaria(lista, item, E, meio-1)
  
    print (pesquisaBinaria(lista, item, 0, len(lista-1)))

    lista = [0,2,4,6,8]
    item = 6

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    E = lista[0]
    D = lista[-1]

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

    posicao = pesquisaBinaria(lista, 7500, E, D)
    print("Posição do item é %d"%(posicao))

    fim_pesquisa = time.time() 
    print("Tempo final da pesquisa: %f"%(fim_pesquisa)) 

    tempototal_pesquisa = fim_pesquisa - inicio_pesquisa
    print ("O tempo total da pesquisa foi %f "%(tempototal_pesquisa))

    inicio_pesquisa_ordenacao = time.time() 
    print ("Tempo inicial da pesquisa_ordenacao: %f"% (inicio_pesquisa_ordenacao))

    semOrdenacao(lista)
    posicao = pesquisaBinaria(lista, 7500, E, D)

    fim_pesquisa_ordenacao = time.time()
    print ("Tempo final da pesquisa_ordenacao: %f "%(fim_pesquisa_ordenacao))

    tempototal_pesquisa_ordenacao = tempototal_pesquisa + tempoTotal_ordenacao
    print ("O tempo total da pesquisa_ordenacao: %f"%(tempototal_pesquisa_ordenacao))





if (__name__ == "__main__"):
    main()
