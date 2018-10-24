import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def BBSort(lista):
    tam = len(lista)
    for j in range(0,tam):
        i = 1
        while(i<tam):
            posterior = lista[i]
            anterior = lista[i-1]
            comp = len(lista)**2
            if(posterior < anterior):
                lista[i] = anterior
                lista[i-1] = posterior
            i+=1
    print("Comparações da Ordenação: %d\n"%(comp))

def QuanTrocas(lista, n):
  ContaTrocas = 0
  for i in range(n):
    for j in range(i+1,n):
      if(lista[i] > lista[j]):
        ContaTrocas +=1
  return ContaTrocas


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

    print("Comparações da pesquisa: %d\n"%(cont))
    return posicao


# Programa principal
def main():
    lista = list(range(1, 15000+1))
    n = len(lista)
    random.shuffle(lista)
    print("Tamanho da lista: {}\n".format(len(lista)))
    print("Números de Trocas da Ordenação: {}\n".format(QuanTrocas(lista,n)))
    
    OrdenaçãoInicio = time.time()
    print("Tempo inicial da Ordenação: %f\n"%(OrdenaçãoInicio))

    BBSort(lista)

    OrdenaçãoFim = time.time()
    print("Tempo final da Ordenação: %f\n"%(OrdenaçãoFim))

    TempoTotalOrdenacao = OrdenaçãoFim - OrdenaçãoInicio
    print("O tempo total da Ordenação foi: %f\n"%(TempoTotalOrdenacao))

    inicioPesquisa = time.time()
    print("Tempo inicial da Pesquisa: %f\n"%(inicioPesquisa))
    
    posicao = PesquiBina(lista, 7500)
    print("posicao do item: %d"%(posicao))

    FimPesquisa = time.time()
    print("Tempo final da Pesquisa: %f\n"%(FimPesquisa))

    TempoTotalPesquisa = FimPesquisa - inicioPesquisa
    print("Tempo total da Pesquisa: %f\n"%(TempoTotalPesquisa))    


    TempoTotal = TempoTotalOrdenacao - TempoTotalPesquisa
    print("O tempo total de execução do programa foi: %f\n"%(TempoTotal))


if (__name__== "__main__"):
    main()






