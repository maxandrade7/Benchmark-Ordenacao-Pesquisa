import random
import time

# Adicionar as funções de Ordenamento e Pesquisa.
def mergeSort(lista):
    if len(lista)>1:
        meio = len(lista)//2
        metade_esquerda = lista[:meio]
        metade_direita = lista[meio:]

        mergeSort(metade_esquerda)
        mergeSort(metade_direita)

        i=0
        j=0
        k=0
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                lista[k]=metade_esquerda[i]
                i=i+1
            else:
                lista[k]=metade_direita[j]
                j=j+1
            k=k+1

        while i < len(metade_esquerda):
            lista[k]=metade_esquerda[i]
            i=i+1
            k=k+1

        while j < len(metade_direita):
            lista[k]=metade_direita[j]
            j=j+1
            k=k+1


def ContadorTrocas(lista, n):
  ContaTrocas = 0
  for i in range(n):
    for j in range(i+1,n):
      if(lista[i] > lista[j]):
        ContaTrocas +=1
  return ContaTrocas

def pesquisaLinear(lista, elemento_desejado):
    posicao = 0
    comparacoes = 0
    for item in lista:
        comparacoes+=1
        posicao+=1
        if(item == elemento_desejado):
              print("A quantidade de comparacoes na pesquisa foi: %d\n"%(comparacoes))
              return posicao
        posicao+=1
        
    return posicao

# Programa principal
def main():
  lista = list(range(1, 15000+1))
  random.shuffle(lista)
  n= len(lista)


  print("A quantidade de trocas de Ordenamento: \n",ContadorTrocas(lista,n))
  inicioOrdena = time.time()

  mergeSort(lista)
  print("A quantidade de comparações total foi: %d\n"%(len(lista)*13))

  fimOrdena = time.time()
  
  tempoOrdena = fimOrdena - inicioOrdena
  print("O tempo total de Ordenamento foi: %f\n"%(tempoOrdena))

  inicioPesq = time.time()

  pesquisaLinear(lista, 7500)

  fimPesq = time.time()

  TempoPesq = fimPesq - inicioPesq
  print("O tempo total de Pesquisa foi: %f\n"%(TempoPesq))

  print("O tempo total de Execucao foi: %f\n"%(tempoOrdena+TempoPesq))

if (__name__ == "__main__"):
    main()
