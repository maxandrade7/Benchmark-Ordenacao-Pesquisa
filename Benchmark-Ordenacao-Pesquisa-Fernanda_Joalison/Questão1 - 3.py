import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def BubbleSort(lista):
  tamanho = len(lista)
  for j in range(0,tamanho):
    i = 1
    while(i<tamanho):
      posterior = lista[i]
      anterior = lista[i-1]
      comparacoes = len(lista)**2
      if(posterior < anterior):
        lista[i] = anterior
        lista[i-1] = posterior

      i+=1
  print("Comparações da Ordenação: %d"%(comparacoes))


def NumTrocas(lista, n):
  ContaTrocas = 0
  for i in range(n):
    for j in range(i+1,n):
      if(lista[i] > lista[j]):
        ContaTrocas +=1
  return ContaTrocas

def pesquisaLinear(lista, elemento_desejado):
    posicao = 0
    cont=0
    for item in lista:
      cont+=1
      if(item == elemento_desejado):
        print("Comparacões da Pesquisa Linear: %s"%(cont))
        return posicao
      posicao = posicao + 1

    return -1


# Programa principal
def main():
  lista = list(range(1, 15000 +1))
  n = len(lista)
  random.shuffle(lista)
  print("Números de Trocas da Ordenação:",NumTrocas(lista,n))
  print("Tamanho da lista: %d"%(len(lista)))

  inicio = time.time()
  print("Tempo inicial: %f"%(inicio))

  InicioOrdenacao = time.time()
    
  BubbleSort(lista)

  FinalOrdenacao = time.time()

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
