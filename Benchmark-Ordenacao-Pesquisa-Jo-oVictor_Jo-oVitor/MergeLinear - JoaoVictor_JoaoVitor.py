import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def mergeSort(lista):
  cont = 0
  if len(lista)>1:
    mid = len(lista)//2
    Esq = lista[:mid]
    Dire = lista[mid:]

    mergeSort(Esq)
    mergeSort(Dire)
        
    i=0
    j=0
    k=0
    while i < len(Esq) and j < len(Dire):
      if Esq[i] < Dire[j]:
        lista[k]=Esq[i]
        i=i+1
      else:
          lista[k]=Dire[j]
          j=j+1
          k=k+1
      while i < len(Esq):
        lista[k]=Esq[i]
        i=i+1
        k=k+1

      while j < len(Dire):
        lista[k]=Dire[j]
        j=j+1
        k=k+1

def NumTrocas(lista, n):
  ContaTrocas = 0
  for i in range(n):
    for j in range(i+1,n):
      if(lista[i] > lista[j]):
        ContaTrocas +=1
  return ContaTrocas


def PesquiLine(lista, elemento_desejado):
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
  lista = list(range(1, 15000+1))
  n = len(lista)
  random.shuffle(lista)
  print("Tamanho da lista: %d\n"%(len(lista)))
  print("Número de Trocas da Ordenação:{}\n".format(NumTrocas(lista,n)))
  print("Comparações da Ordenação: %d\n"%(len(lista)*13))
  print("Comparações da Pesquisa: %d"%PesquiLine(lista, elemento_desejado))

  OrdenaçãoInicio = time.time()
  print("Tempo inicial Ordenação: %f\n"%(OrdenaçãoInicio))
    
  mergeSort(lista)
    
  OrdenaçãoFim = time.time()
  print("Tempo final da Ordenação: %f\n"%(OrdenaçãoFim))

  TempTotOrdenação = OrdenaçãoFim - OrdenaçãoInicio
  print("O tempo total da Ordenação foi %f\n"%(TempTotOrdenação))

  PesquisaInicio = time.time()
  print("Tempo inicial Pesquisa: %f\n"%(PesquisaInicio))
    
  posicao = PesquiLine(lista, 7500)
  print("Posição do item é: {}\n".format(posicao))

  PesquisaFim = time.time()
  print("Tempo final da Pesquisa: %f\n"%(PesquisaFim))

  TempTotPesquisa = PesquisaFim - PesquisaInicio
  print("O tempo total da Pesquisa foi: %f\n"%(TempTotPesquisa))
    
  fim = time.time()
  print("Tempo final: %f\n"%(fim))

  TempTot = TempTotOrdenação - TempTotPesquisa
  print("O tempo total foi %f\n"%(TempTot))

if (__name__== "__main__"):
    main()
