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


def PesquisaBinaria(lista,item):

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

    print("Comparações da pesquisa: %d"%(cont))
    return posicao


# Programa principal
def main():
    lista = list(range(1, 15000+1))
    n = len(lista)
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))
    print("Números de Trocas da Ordenação:",NumTrocas(lista,n))

    Inicio = time.time()
    print("Tempo Inicial: %f"%(Inicio))
    
    inicioOrdenacao = time.time()
    print("Tempo inicial da Ordenação: %f"%(inicioOrdenacao))

    BubbleSort(lista)

    FimOrdenacao = time.time()
    print("Tempo final da Ordenação: %f"%(FimOrdenacao))

    TempoTotalOrdenacao = FimOrdenacao - inicioOrdenacao
    print("O tempo total da Ordenação foi: %f"%(TempoTotalOrdenacao))

    inicioPesquisa = time.time()
    print("Tempo inicial da Pesquisa: %f"%(inicioPesquisa))
    
    posicao = PesquisaBinaria(lista, 7500)
    print("posicao do item: %d"%(posicao))

    FimPesquisa = time.time()
    print("Tempo final da Pesquisa: %f"%(FimPesquisa))

    TempoTotalPesquisa = FimPesquisa - inicioPesquisa
    print("Tempo total da Pesquisa: %f"%(TempoTotalPesquisa))    

    
    Final = time.time()
    print("Tempo final: %f"%(Final))

    TempoTotal = Final - Inicio
    print("O tempo total é: %f"%(TempoTotal))


if (__name__ == "__main__"):
    main()
