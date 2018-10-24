import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def semOrdenacao(lista):
    pass

def pesquisaLinear(lista, elemento_desejado):
    cont = 0
    posicao = 0
    for item in lista:
        cont = cont+1
        if(item == elemento_desejado):
            print("A pesquisa fez %d comparações"%(cont))
            return posicao
        posicao = posicao + 1

    return -1

# Programa principal
def main():
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
    

    posicao = pesquisaLinear(lista, 7500)
    print("Posição do item é %d"%(posicao))

    fim_pesquisa = time.time()
    tempo_pesquisa = (fim_pesquisa) - (inicio_pesquisa)
    
    print("O tempo total da pesquisa é: %f"%(tempo_pesquisa))
    





    TempoTotal = (tempo_ordenacao) + (tempo_pesquisa)
    print("O tempo total foi: %f"%(TempoTotal))

    

    
    

    

if (__name__ == "__main__"):
    main()
