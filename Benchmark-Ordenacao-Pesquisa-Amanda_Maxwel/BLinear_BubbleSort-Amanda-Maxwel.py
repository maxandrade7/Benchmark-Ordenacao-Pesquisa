import random
import time

# Adicionar as funÃ§Ãµes de Ordenamento e Pesquisa.
def BubbleSort(lista):
      cont_comparacoes = 0
      cont_trocas = 0
      for i in range(len(lista)):
              for j in range(len(lista)-i-1):
                  cont_comparacoes+=1
                  if lista[j] > lista[j+1]:
                    cont_trocas+=1
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                        
      print("O numero total de Trocas: %d\n"%(cont_trocas))                
    
      return (lista)

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

  inicioOrdena = time.time()
  print("Tempo inicial de Ordenamento: %f\n"%(inicioOrdena))
  
  BubbleSort(lista)
  print("A quantidade de comparações no BubbleSort foi: %d\n"%(len(lista)**2))
  
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

  Total = (tempoOrdena) + (TempoPesq)
  print("O tempo total de execucao foi: %f\n"%(Total))

if (__name__ == "__main__"):
    main()
