
import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def semOrdenacao(lista):
    print("A quantidade total de comparacoes foi: 0\n")
    print("A quantidade total de trocas foi: 0\n")

def BuscaBinaria(lista, elemento_desejado):
    comparacoes = 0

    esquerda, direita = 0, len(lista)-1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        comparacoes+=1
        if lista[meio] == elemento_desejado:
            print("A quantidade total de comparacoes foi: %d\n"%(comparacoes))
            return meio

        elif lista[meio] > elemento_desejado:
            direita = meio - 1
        else: 
            esquerda = meio + 1
    
    return -1

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)

    inicioPesq = time.time()
    print("Tempo inicial da Pesquisa: %f\n"%(inicioPesq))

    BuscaBinaria(lista, 7500)

    fimPesq = time.time()
    print("Tempo final da Pesquisa: %f\n"%(fimPesq))

    tempoTotal = fimPesq - inicioPesq
    print("O tempo total de Pesquisa foi: %f\n"%(tempoTotal))

    inicioOrdena = time.time()
    print("Tempo inicial de Ordenamento: %f\n"%(inicioOrdena))

    semOrdenacao(lista)

    fimOrdena = time.time()
    print("Tempo final da Ordenamento: %f\n"%(fimOrdena))

    tempoTotal = fimOrdena - inicioOrdena
    print("O tempo total de Ordenamento foi: %f\n"%(tempoTotal))

if (__name__ == "__main__"):
    main()
