import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def semOrdenacao(lista):
    pass

def pesquisa_binaria(lista, item):
    cont = 0

    """Implementa pesquisa binária iterativamente."""
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        cont = cont+1
        if lista[meio] == item:
            return cont
        elif lista[meio] > item:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1


    print("comparações da busca: %d"%(cont))
    print("-1")


    
# Programa principal
def main():
    item = 7500
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))


    #Cuidando dos dados da ordenação
    inicio_ordenacao = time.time()
    

    semOrdenacao(lista)

    fim_ordenacao = time.time()
    tempo_ordenacao = (fim_ordenacao) - (inicio_ordenacao)
    
    print("O tempo total da ordenação foi: %f"%(tempo_ordenacao))





    #Cuidando dos dados da pesquisa
    inicio_pesquisa = time.time()
    

    comparacao = pesquisa_binaria(lista,7500)
    

    fim_pesquisa = time.time()
    tempo_pesquisa = (fim_pesquisa) - (inicio_pesquisa)
    
    print("O tempo total da pesquisa é: %f"%(tempo_pesquisa))
    

    #A busca binária trabalha com listas ordenadas, que é o contrário do que está acontecendo aqui, já que não estamos ordenando a lista
    





    TempoTotal = (tempo_ordenacao) + (tempo_pesquisa)
    print("O tempo total foi: %f"%(TempoTotal))

    

    
    

    

if (__name__ == "__main__"):
    main()
