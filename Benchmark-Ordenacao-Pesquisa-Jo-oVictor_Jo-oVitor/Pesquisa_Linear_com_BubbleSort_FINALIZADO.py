
import time
import random

# Adicionar as funções de Ordenamento e Pesquisa

def BBSort(lista):
    tam = len(lista)
    cont = 0
    comp = len(lista)**2
    print("A quantidade de comparações da ordenação foi de {}\n".format(comp))

    for k in range(0, tam):
        i = 1

        while(i<tam):
            suc = lista[i]
            antc = lista[i-1]

            if(suc<antc):
                lista[i] = antc
                lista[i-1] = suc
                cont+=1

            i+=1
    print('A quantidade de trocas foi de {}\n'.format(cont))

def PesquiLine(lista, EleDeje):
    posi = 0
    cont = 0
    for item in lista:
      cont += 1
      if(item==EleDeje):
        print("A quantidade de comparações da pesquisa foi de {}\n".format(cont))
        return posi
      posi = posi + 1

      

    return -1

# Programa Principal

def main():
  lista = list(range(1, 15000+1))
  n = len(lista)
  random.shuffle(lista)
  print("Tamanho da lista: {}".format(len(lista)))

  inicialOrde = time.time()
  print("O tempo inicial da ordenação foi de %f\n"%(inicialOrde))

  BBSort(lista)

  FinalOrde = time.time()
  print("O tempo final da ordenação foi de %f\n" %(FinalOrde))
  TotalOrde = FinalOrde - inicialOrde

  print("O tempo total da ordenação foi de {}\n".format(TotalOrde))

  


  inicialPesqui = time.time()
  print("O tempo inicial da pesquisa foi de %f\n"%(inicialPesqui))

  PesquiLine(lista, 7500)

  FinalPesqui = time.time()
  print("O tempo final da pesquisa foi de %f\n"%(FinalPesqui))
  
  TotalPesqui = FinalPesqui - inicialPesqui

  print("O tempo total da pesquisa foi de {}\n".format(TotalPesqui))

  print("O tempo total do programa foi de {}\n".format(TotalOrde+TotalPesqui))



if(__name__=="__main__"):
    main()


        
