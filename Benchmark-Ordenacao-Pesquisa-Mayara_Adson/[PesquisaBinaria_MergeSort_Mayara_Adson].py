import time
import random


def merge(A, aux, esquerda, meio, direita):
    
    for k in range(esquerda, direita + 1):
        aux[k] = A[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            A[k] = aux[j]
            j += 1
        elif j > direita:
            A[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            A[k] = aux[j]
            j += 1
        else:
            A[k] = aux[i]
            i += 1


def mergesort(A, aux, esquerda, direita):
    compOrdem= 0
    trocaOrdem= 0
    compOrdem+= 1
    if direita <= esquerda:
        return
        trocaOrdem+= 1
    meio = (esquerda + direita) // 2

    mergesort(A, aux, esquerda, meio)
    
    mergesort(A, aux, meio + 1, direita)

    merge(A, aux, esquerda, meio, direita)

    print("    ")
    print("O número de comparações da ordenação foi {}.".format(compOrdem))
    print("O número de trocas da ordenação foi {}.".format(trocaOrdem))

    
def pesquisaBinaria(lista,item,E,D):
    compPesq= 0
    trocaPesq= 0
    if (D<E):
        return -1
    meio=(E+D)//2
    if ([meio] == item):
        compPesq+= 1
        return meio
    elif(lista[meio] == item):
        trocaPesq+= 1
        return pesquisa_linear(lista,item,meio+1, D)
    else:
        trocaPesq+= 1
        return pesquisa_linear(lista, item, E, meio-1)

    print("    ")
    print("O número de comparações na pesquisa foi {}.".format(compPesq))
    print("O número de trocas na pesquisa foi {}.".format(trocaPesq))

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    aux = [0] * len(lista)
    mergesort(lista, aux, 0, len(lista) - 1)

    print("    ")
    print("O número de comparações da ordenação foi {}.".format(compOrdem))
    print("O número de trocas da ordenação foi {}.".format(trocaOrdem))

    fimOrdem = time.time()

    tempoOrdem = fimOrdem - inicio 

    inicioPesq = time.time()
    
    pesquisaBinaria(lista,7500,len(lista),0)

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
