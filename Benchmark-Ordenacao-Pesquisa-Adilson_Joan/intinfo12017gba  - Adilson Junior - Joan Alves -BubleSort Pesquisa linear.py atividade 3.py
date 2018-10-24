import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def Bubble_Sort(lista):
    trocas = 0
    if len(lista) <= 1:
        V = lista
    else:
        for j in range(0,len(lista)):
            for i in range(0,len(lista)-1):
                if lista[i]>lista[i+1]:
                    trocas += 1
                    A = lista[i+1]
                    lista[i+1] = lista[i]
                    lista[i] = A
        V = lista

    print("A quantidade de trocas foi: %d"%(trocas))
    return V
  
def pesquisa_Linear(lista, elemenDesejado):
    posicao = 0
    contador = 0
    for item in lista:
        contador = contador+1
        if(item == elemenDesejado):
            print ("A quantidade de comparações da pesquisa foi: %d"%(contador))
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
    
    Bubble_Sort(lista)
    

    fim_ordenacao = time.time()
    print("Tempo final da ordenação: %f"%(fim_ordenacao))

    tempoTotal_ordenacao = fim_ordenacao - inicio_ordenacao
    print("O tempo total da ordenação foi %f"%(tempoTotal_ordenacao))

   
   
   
    #Dados da pesquisa

    inicio_pesquisa = time.time() 
    print("tempo inicial da pesquisa: %f"%(inicio_pesquisa))

    
    posicao = pesquisa_Linear(lista, 7500)
    print("Posição do item é %d"%(posicao))

    fim_pesquisa = time.time() 
    print("Tempo final da pesquisa: %f"%(fim_pesquisa)) 

    tempototal_pesquisa = fim_pesquisa - inicio_pesquisa
    print ("O tempo total da pesquisa foi %f "%(tempototal_pesquisa))

    tempoTotal  = tempoTotal_ordenacao + tempototal_pesquisa
    print("O tempo total do código foi: %f"%(tempoTotal))

    print("A quantidade de comparações da ordenacao foi: %d"%(len(lista)**2))




if (__name__ == "__main__"):
    main()
