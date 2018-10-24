import time
import random

compOrdem= 0
trocaOrdem= 0
def merge(A, aux, esquerda, meio, direita):
    compOrdem= 0
    trocaOrdem= 0
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

    print("  ") 
    print("O número de comparações da ordenação foi {}".format(compOrdem))
    print("O número de trocas da ordenação foi {}".format(trocaOrdem))
    
            
compOrdem= 0
trocaOrdem= 0
def mergesort(A, aux, esquerda, direita):
    compOrdem= 0
    trocaOrdem= 0
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2

    mergesort(A, aux, esquerda, meio)
    
    mergesort(A, aux, meio + 1, direita)

    merge(A, aux, esquerda, meio, direita)

    print("  ") 
    print("O número de comparações da ordenação foi {}".format(compOrdem))
    print("O número de trocas da ordenação foi {}".format(trocaOrdem))
   
compPesq= 0
trocaPesq= 0
def pesquisaLinear(lista,elemento):
    compPesq= 0
    trocaPesq= 0
    posicao= 0
    for item in lista:
        if(item == elemento):
            return posicao
        posicao=posicao + 1
        
    return -1

    print("  ")
    print("O número de comparações da pesquisa foi {}".format(compPesq))
    print("O número de trocas da pesquisa foi {}".format(trocaPesq))

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    aux=[0] * len(lista)
    mergesort(lista, aux, 0, len(lista)-1)
    print("  ") 
    print("O número de comparações da ordenação foi {}".format(compOrdem))
    print("O número de trocas da ordenação foi {}".format(trocaOrdem))
    
    fimOrdem = time.time()

    tempoOrdem = fimOrdem - inicio 

    inicioPesq = time.time()
    
    pesquisaLinear(lista,7500)
    print("  ")
    print("O número de comparações da pesquisa foi {}".format(compPesq))
    print("O número de trocas da pesquisa foi {}".format(trocaPesq))

    fim = time.time()
    tempoPesq = fim - inicioPesq
    print("    ")
    print("Tempo final: %f"%(fim))     

    tempoTotal = fim - inicio
    print("O tempo da ordenação foi %f"%(tempoOrdem))
    print("O tempo da pesquisa foi %f"%(tempoPesq))
    print("O tempo total foi %f"%(tempoTotal))

if (__name__ == "__main__"):
    main()
