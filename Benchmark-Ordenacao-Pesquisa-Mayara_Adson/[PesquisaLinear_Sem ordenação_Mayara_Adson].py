import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def semOrdenacao(lista):
    pass


compPesq= 0
def pesquisaLinear(lista,elemento):
    compPesq= 0
    posicao= 0
    for item in lista:
        compPesq+=1
        if(item == elemento):
            return posicao
        posicao=posicao + 1
        
    return -1

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
    
    pesquisaLinear(lista,7500)
    print("  ")
    print("O número de comparações da pesquisa foi {}.".format(compPesq))

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
