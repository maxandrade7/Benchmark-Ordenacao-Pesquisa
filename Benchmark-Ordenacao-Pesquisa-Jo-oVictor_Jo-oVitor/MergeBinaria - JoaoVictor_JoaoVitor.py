import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
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
  Controcas = 0
  for i in range(n):
    for j in range(i+1,n):
      if(lista[i] > lista[j]):
        Controcas +=1
  return Controcas

def PesquiBina(lista, item):
    cont = 0


    Esq, Dire = 0, len(lista) - 1
    while Esq <= Dire:
        meio = (Esq + Dire) // 2
        cont = cont+1
        if lista[meio] == item:
            return cont
        elif lista[meio] > item:
            Dire = meio - 1
        else: # A[meio] < item
            Esq = meio + 1

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    n = len(lista)
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))
    print("Numero de Trocas da Ordenação foi de:",NumTrocas(lista,n))


    inicio_ordenacao = time.time()
    
    mergeSort(lista)
    
    fim_ordenacao = time.time()
    TempTotOrd = fim_ordenacao - inicio_ordenacao
    print("A quantidade de comparações do mergesort foi de: %d"%(len(lista)*13))
    print("O tempo de ordenação foi de: %f"%(TempTotOrd))
    
    

    PesquisaInicio = time.time()
    
    Comps = PesquiBina(lista,7500)
    

    PesquisaFim = time.time()
    TempTotPes = (PesquisaFim) - (PesquisaInicio)
    print("O tempo total da pesquisa foi de : %f"%(TempTotPes))
    print("A quantidade de comparações da pesquisa binária foi de: %d"%(Comps))
    


    TempTopPro = TempTotOrd + TempTotPes
    print("O tempo total foi de: %f"%(TempTopPro))

    
if(__name__ == "__main__"):
  main()
