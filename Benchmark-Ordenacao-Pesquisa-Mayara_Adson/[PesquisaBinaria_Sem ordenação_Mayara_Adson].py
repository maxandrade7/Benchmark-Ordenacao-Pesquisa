import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def semOrdenacao(lista):
    pass

compPesq= 0
def pesquisa_binaria(lista,item,E,D):
    compPesq= 0
    if (D<E):
        return -1
    meio=(E+D)//2
    if ([meio] == item):
        return meio
        compPesq+=1
    elif(lista[meio] == item):
        troca+=1
        return pesquisa_binaria(lista,item,meio+1, D)
    else:
        troca+=1
        return pesquisa_binaria(lista, item, E, meio-1)

    print("  ")
    print("O número de comparações da pesquisa foi {}".format(compPesq))

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    semOrdenacao(lista)

    fimOrdem = time.time()

    tempoOrdem = fimOrdem - inicio 

    inicioPesq = time.time()
    
    pesquisa_binaria(lista,7500,len(lista),0)
    print("  ")
    print("O número de comparações da pesquisa foi {}".format(compPesq))

    fim = time.time()
    tempoPesq = fim - inicioPesq
    print("   ")
    print("Tempo final: %f"%(fim))     

    tempoTotal = fim - inicio
    print("O tempo da ordenação foi %f"%(tempoOrdem))
    print("O tempo da pesquisa foi %f"%(tempoPesq))
    print("O tempo total foi %f"%(tempoTotal))    

if (__name__ == "__main__"):
    main()
