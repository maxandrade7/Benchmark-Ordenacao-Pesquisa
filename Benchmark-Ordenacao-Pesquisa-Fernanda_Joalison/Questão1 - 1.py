import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def semOrdenacao(lista):
  pass

def pesquisaLinear(lista, elemento_desejado):
    posicao = 0
    cont = 0
    for item in lista:
      cont+=1
      if(item == elemento_desejado):
        print("Comparacões da Pesquisa: %s"%(cont))
        return posicao
      posicao = posicao + 1

    return -1
    

# Programa principal
def main():
  lista = list(range(1, 15000+1))
  random.shuffle(lista)
  print("Tamanho da lista: %d"%(len(lista)))

  inicio = time.time()
  print("Tempo inicial: %f"%(inicio))

  semOrdenacao(lista)
    
  InicioPesquisa = time.time()
  print("Tempo inicial da Pesquisa: %f"%(InicioPesquisa))

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
