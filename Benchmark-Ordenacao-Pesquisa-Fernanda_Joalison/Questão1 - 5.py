
import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def mergeSort(lista):
    cont = 0
    if len(lista)>1:
        mid = len(lista)//2
        MetadeEsquerda = lista[:mid]
        MetadeDireita = lista[mid:]

        mergeSort(MetadeEsquerda)
        mergeSort(MetadeDireita)
        
        i=0
        j=0
        k=0
        while i < len(MetadeEsquerda) and j < len(MetadeDireita):
            if MetadeEsquerda[i] < MetadeDireita[j]:
                lista[k]=MetadeEsquerda[i]
                i=i+1
            else:
                lista[k]=MetadeDireita[j]
                j=j+1
            k=k+1
        while i < len(MetadeEsquerda):
            lista[k]=MetadeEsquerda[i]
            i=i+1
            k=k+1

        while j < len(MetadeDireita):
            lista[k]=MetadeDireita[j]
            j=j+1
            k=k+1

def NumTrocas(lista, n):
  ContaTrocas = 0
  for i in range(n):
    for j in range(i+1,n):
      if(lista[i] > lista[j]):
        ContaTrocas +=1
  return ContaTrocas


def pesquisaLinear(lista, elemento_desejado):
    posicao = 0
    cont = 0
    for item in lista:
        cont+=1

        if(item == elemento_desejado):
            print("Comparações da Pesquisa: %d"%(cont))
            return posicao
        posicao = posicao + 1
    return -1


# Programa principal
def main():
    lista = list(range(1, 15000
                       +1))
    n = len(lista)
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))
    print("Numero de Trocas da Ordenação:",NumTrocas(lista,n))
    print("Comparações da Ordenação: %d"%(len(lista)*13))

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    InicioOrdenacao = time.time()
    print("Tempo inicial Ordenação: %f"%(InicioOrdenacao))
    
    mergeSort(lista)
    
    FinalOrdenacao = time.time()
    print("Tempo final da Ordenação: %f"%(FinalOrdenacao))

    TempoTotalOrdenacao = FinalOrdenacao - InicioOrdenacao
    print("O tempo total da Ordenação foi %f"%(TempoTotalOrdenacao))

    InicioPesquisa = time.time()
    print("Tempo inicial Pesquisa: %f"%(InicioPesquisa))
    
    posicao = pesquisaLinear(lista, 7500)
    print("Posição do item é: %d"%(posicao))

    FinalPesquisa = time.time()
    print("Tempo final da Pesquisa: %f"%(FinalPesquisa))

    TempoTotalPesquisa = FinalPesquisa - InicioPesquisa
    print("O tempo total da Pesquisa foi: %f"%(TempoTotalPesquisa))
    
    fim = time.time()
    print("Tempo final: %f"%(fim))

    tempoTotal = fim - inicio
    print("O tempo total foi %f"%(tempoTotal))

if (__name__ == "__main__"):
    main()
