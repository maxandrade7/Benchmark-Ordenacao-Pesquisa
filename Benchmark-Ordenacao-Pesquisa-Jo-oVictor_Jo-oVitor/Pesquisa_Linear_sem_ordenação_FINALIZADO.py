import time
import random

#funções de ordenação e pesquisa

def Desordenada(lista):
  pass

def PesquiLine(lista, ele_dese):
  posi = 0
  cont = 0
  for item in lista:
    cont+=1
    if(item==ele_dese):
      print("A quantidade de comparações da pesquisaa foi de {}\n".format(cont))
      return posi
    posi = posi+1
  return -1



# Programa principal

def main():

  lista = list(range(1, 15000+1))
  random.shuffle(lista)
  print("Tamanho da lista: {}\n".format(len(lista)))

  inicial = time.time()
  print("Tempo inicial da pesquisa: %f\n" %(inicial))

  Desordenada(lista)
  posi = PesquiLine(lista, 7500)
  print("Posição do item é {}\n".format(posi))

  fim = time.time()
  print("Tempo final da pesquisa: %f\n" %(fim))

  TempTot = fim - inicial
  print("O tempo total da pesquisa: %f\n" %(TempTot))

if(__name__=="__main__"):
  main()
