import time
import random

def MergeSort(lista):
    if len(lista)>1:
        meio = len(lista)//2
        Esq = lista[:meio]
        Dire = lista[meio:]

        MergeSort(Esq)
        MergeSort(Dire)

        a=0
        b=0
        c=0
        while a < len(Esq) and b < len(Dire):
            if Esq[a] < Dire[b]:
                lista[c]=Esq[a]
                a=a+1
            else:
                lista[c]=Dire[b]
                b=b+1
            c=c+1

        while a < len(Esq):
            lista[c]=Esq[a]
            a=a+1
            c=c+1

        while b < len(Dire):
            lista[c]=Dire[b]
            b=b+1
            c=c+1

def QuanTrocas(lista, num):
  ContadorTrocas = 0
  for a in range(num):
    for b in range(a+1,num):
      if(lista[a] > lista[b]):
        ContadorTrocas +=1
  return ContadorTrocas



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

    print("quantidade de comaparações da Pesquisa Binária: {}\n".format(cont))
    return posicao
  

# Programa principal 

def main():

    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: {}\n".format(len(lista)))
    print("Números de Trocas da Ordenação: {}\n".format(QuanTrocas(lista, num)))


    inicioOrdenacao = time.time () 
    print ("Tempo inicial da Ordenação: %f\n"%(inicioOrdenacao))

    MergeSort(lista) 
    posicao = PesquiBina(lista, 7500) 
    print ("Posição do item é: %d\n"%(posicao)) 

    fimOrdenacao = time.time ()
    print ("Tempo final da ordenação: %f\n"%(fimOrdenacao)) 

    tempoTotal = fimOrdenacao - inicioOrdenacao 
    print ("O tempo total da ordenação foi: %f\n"%(tempoTotal))




    PesquisaIni = time.time() 
    print("Tempo inicial da pesquisa: %f\n"%(PesquisaIni))


    PesquisaFim = time.time()
    print("Tempo final da pesquisa: %f\n"%(PesquisaFim))

    tempTot = PesquisaFim - PesquisaIni 
    print("O tempo total da pesquisa foi: %f\n"%(tempTot))

    TempoToTal = tempoTotal - tempTot
    print("O tempo total da execução do programa foi: {}".format(TempoToTal))

if (__name__== "__main__"): 
    main()
