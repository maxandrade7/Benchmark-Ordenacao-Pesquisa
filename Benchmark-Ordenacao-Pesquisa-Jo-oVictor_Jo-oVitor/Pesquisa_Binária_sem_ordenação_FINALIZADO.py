import time
import random

#funções de ordenação e pesquisa

def Desordenada(lista):
  pass

def PesquiBina(lista,item):

    ini = 0
    fim = len(lista)-1
    posicao = -1
    cont = 0

    while(ini <= fim):
        meio = (ini + fim)//2
        cont+=1
        if(lista[meio] == item):
            posicao = meio
            break
        elif(lista[meio] > item):
            cont+=1
            fim = meio - 1
        else:
            cont+=1
            ini = meio + 1

    print("A quantidade de comparações da pesquisa foi: {}\n".format(cont))
    return posicao
  
# Programa principal

def main():

  lista = list(range(1, 15000+1))
  random.shuffle(lista)
  print("Tamanho da lista: {}\n".format(len(lista)))

  PesquisaInicio = time.time()
  print("Tempo inicial da pesquisa foi: %f\n" %(PesquisaInicio))

  Desordenada(lista)
  posi = PesquiBina(lista, 7500)
  print("Posição do item é: {}\n".format(posi))

  PesquisaFim = time.time()
  print("Tempo final da pesquisa foi: %f\n" %(PesquisaFim))

  TempTot = PesquisaFim - PesquisaInicio
  print("O tempo total foi: %f\n" %(TempTot))

if(__name__=="__main__"):
  main()
