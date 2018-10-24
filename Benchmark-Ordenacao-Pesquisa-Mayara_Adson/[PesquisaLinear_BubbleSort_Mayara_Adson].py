import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def bubbleSort(lista):
    trocaOrdem = 0
    compOrdem= 0
    tamanho = len(lista)
    for j in range(0, tamanho):
        i = 1
        while (i < tamanho):
            compOrdem+= 1
            posterior = lista[i]
            anterior = lista[i-1]
            if (posterior < anterior):
                trocaOrdem= 0
                lista[i] = anterior
                lista[i-1] = posterior
            i+=1
            
    print("  ")
    print("O número de comparações da ordenação foi {}".format(compOrdem))
    print("O número de trocas da ordenação foi {}".format(trocaOrdem))


compPesq= 0
trocaPesq= 0
def pesquisaLinear(lista,elemento):
    compPesq= 0
    trocaPesq= 0
    posicao= 0
    for item in lista:
        compPesq+= 1
        if(item == elemento):
            return posicao
            trocaPesq+= 1
        posicao=posicao + 1
        
    return -1

    print("  ")
    print("O número de comparações da pesquisa foi {}".format(compPesq))
    print("O número de trocas da pesquisa foi {}".format(trocaPesq))


# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))

    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    bubbleSort(lista)
    fimOrdem = time.time()

    tempoOrdem = fimOrdem - inicio 

    inicioPesq = time.time()
    
    pesquisaLinear(lista,7500)
    print("  ")
    print("O número de comparações da pesquisa foi {}".format(compPesq))
    print("O número de trocas da pesquisa foi {}".format(trocaPesq))

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
