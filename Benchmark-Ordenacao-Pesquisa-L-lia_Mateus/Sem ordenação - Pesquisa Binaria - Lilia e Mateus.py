import time
import random

#Adicionar as funções de Ordenamento e Pesquisa.


def semOrdenacao(lista):
    pass
def pesquisa_binaria(lista, elemento_desejado):
    """Implementa pesquisa binária iterativamente."""   
    posicao = 0
    tamanho = len(lista)
    comps= 0
    '''for j in range(0, tamanho):
    comps+=1'''

    #print (comps)
    pos = -1
    i =0


    for item in lista:
        i+=1
        comps+=1
        if(item == elemento_desejado):
            pos = 1
        break
    posicao = posicao + 1

    print("comparacoes: %d" % (comps))

    return pos

    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] > item:
            direita = meio - 1
        else: # lista[meio] < item
            esquerda = meio + 1
        return -1

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))

#Começa contar o tempo
    inicio = time.time()
    print("Tempo inicial: %f"%(inicio))

    semOrdenacao(lista)
    posicao = pesquisa_binaria(lista, 2500)
    print("Posição do item é %d"%(posicao))

    fim = time.time()
    print("Tempo final: %f"%(fim))

    tempoTotal = fim - inicio
    print("O tempo total foi %f"%(tempoTotal))
if (__name__ == "__main__"):
    main()
