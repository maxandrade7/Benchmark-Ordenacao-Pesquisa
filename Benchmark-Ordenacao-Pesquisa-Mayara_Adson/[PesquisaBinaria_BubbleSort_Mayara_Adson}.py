
import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.

def bubbleSort(lista):
    tamanho = len(lista)
    trocaOrdem= 0
    compOrdem= 0
    for j in range(0, tamanho):
        i = 1
        while (i < tamanho):
            compOrdem+=1
            posterior = lista[i]
            anterior = lista[i-1]
            if (posterior < anterior):
                trocaOrdem+=1
                lista[i] = anterior
                lista[i-1] = posterior
            i+=1

    print("   ")
    print("O número de comparações da ordenação foi {}".format(compOrdem))
    print("O número de trocas da ordenação foi %d"%(trocaOrdem))


compPesq=0
trocaPesq=0
def pesquisaBinaria(lista,item,E,D):
    compPesq=0
    trocaPesq=0
    if (D<E):
        return -1
    meio=(E+D)//2
    if ([meio] == item):
        compPesq+=1
        return meio 
    elif(lista[meio] == item):
        trocaPesq+=1
        return pesquisabinaria(lista,item,meio+1, D)
    else:
        trocaPesq+=1
        return pesquisabinaria(lista, item, E, meio-1)

    print("    ")
    print("O número de comparações da pesquisa foi {}".format(compPesq))
    print("O número de trocas da pesquisa foi %d"%(trocaPesq))
    
# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    bubbleSort(lista)

    fimOrdem = time.time()

    tempoOrdem = fimOrdem - inicio 

    inicioPesq = time.time()
    
    pesquisaBinaria(lista,7500,len(lista),0)
    print("    ")
    print("O número de comparações da pesquisa foi {}".format(compPesq))
    print("O número de trocas da pesquisa foi %d"%(trocaPesq))

    fim = time.time()
    tempoPesq = fim - inicioPesq
    print("   ")
    print("Tempo final: %f"%(fim))     

    tempoTotal = fim - inicio
    print("O tempo da ordenação foi %f"%(tempoOrdem))
    print("O tempo da pesquisa foi %f"%(tempoPesq))
    print("O tempo total foi %f"%(tempoTotal))

if (__name__ == "__main__"):
    main()
