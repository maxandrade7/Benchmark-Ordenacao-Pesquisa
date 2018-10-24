import time
import random

# Adicionar as funÃ§Ãµes de Ordenamento e Pesquisa.
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


def NumTrocas(lista, n):
  ContaTrocas = 0
  for i in range(n):
    for j in range(i+1,n):
      if(lista[i] > lista[j]):
        ContaTrocas +=1
  return ContaTrocas

def pesquisa_binaria(lista, item):
    cont = 0

    """Implementa pesquisa binária iterativamente."""
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        cont = cont+1
        if lista[meio] == item:
            return cont
        elif lista[meio] > item:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    n = len(lista)
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))
    print("Numero de Trocas da Ordenação:",NumTrocas(lista,n))


    #Cuidando dos dados da ordenaÃ§Ã£o
    inicio_ordenacao = time.time()
    
    mergeSort(lista)
    
    fim_ordenacao = time.time()
    tempo_ordenacao = fim_ordenacao - inicio_ordenacao
    print("A quantidade de comparações do mergesort foi: %d"%(len(lista)*13))
    print("O tempo de ordenação foi: %f"%(tempo_ordenacao))
    
    

    #Cuidando dos dados da pesquisa
    inicio_pesquisa = time.time()
    
    comparacao = pesquisa_binaria(lista,7500)
    

    fim_pesquisa = time.time()
    tempo_pesquisa = (fim_pesquisa) - (inicio_pesquisa)
    print("O tempo total da pesquisa Ã©: %f"%(tempo_pesquisa))
    print("A quantidade de comparações da pesquisa binária foi: %d"%(comparacao))
    


    tempo_do_programa = tempo_ordenacao + tempo_pesquisa
    print("O tempo total foi: %f"%(tempo_do_programa))

    
if(__name__ == "__main__"):
  main()
