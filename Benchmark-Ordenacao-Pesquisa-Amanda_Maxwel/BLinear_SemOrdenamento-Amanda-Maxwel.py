import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def semOrdenacao(lista):
    print("A quantidade total de comparacoes foi: 0\n")
    print("A quantidade total de trocas foi: 0\n")

def pesquisaLinear(lista, elemento_desejado):
    posicao = 0
    comparacoes = 0
    for item in lista:
        comparacoes+=1
        posicao+=1
        if(item == elemento_desejado):
          break

    print("A quantidade de comparacoes na pesquisa foi: %d\n"%(comparacoes))
    return posicao

# Programa principal
def main():
  lista = list(range(1, 15000+1))
  random.shuffle(lista)

  inicioProg = time.time()

  inicioOrdena = time.time()
  print("Tempo inicial de Ordenamento: %f\n"%(inicioOrdena))
  
  semOrdenacao(lista)

  fimOrdena = time.time()
  print("Tempo final da Ordenamento: %f\n"%(fimOrdena))

  tempoOrdena = fimOrdena - inicioOrdena
  print("O tempo total de Ordenamento foi: %f\n"%(tempoOrdena))

  inicioPesq = time.time()
  print("Tempo inicial da Pesquisa: %f\n"%(inicioPesq))

  pesquisaLinear(lista, 7500)

  fimPesq = time.time()
  print("Tempo final da Pesquisa: %f\n"%(fimPesq))

  TempoPesq = fimPesq - inicioPesq
  print("O tempo total de Pesquisa foi: %f\n"%(TempoPesq))


  fimProg = time.time()
  print("O tempo total de Execucao foi: %f\n"%(fimProg-inicioProg))

if (__name__ == "__main__"):
    main()
