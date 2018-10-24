import time
import random

# Adicionar as funÃ§Ãµes de Ordenamento e Pesquisa.
def bubbleSort(lista):
    tamanho = len(lista)
    troca = 0
    for iteracao in range(0,tamanho):

        i = 1
        while(i<tamanho):
            if(lista[i])<(lista[i-1]):
                troca = troca +1
                aux = lista[i-1]
                lista[i-1] = lista[i]
                lista[i] = aux

            i = i+1
    print("A quantidade de trocas foi: %d:"%(troca))

def pesquisaLinear(lista, elemento_desejado):
    cont = 0
    posicao = 0
    for item in lista:
        cont = cont+1
        if(item == elemento_desejado):
            print("A pesquisa fez %d comparaÃ§Ãµes"%(cont))
            return posicao
        posicao = posicao + 1

    return -1

# Programa principal
def main():
    lista = list(range(1, 15000+1))
    random.shuffle(lista)
    print("Tamanho da lista: %d"%(len(lista)))


    #Cuidando dos dados da ordenaÃ§Ã£o
    inicio_ordenacao = time.time()
    
    bubbleSort(lista)

    fim_ordenacao = time.time()
    tempo_ordenacao = (fim_ordenacao) - (inicio_ordenacao)
    print("O tempo total da ordenaÃ§Ã£o foi: %f"%(tempo_ordenacao))
    #Aprendemos na disciplina que a quantidade de comparações do bubble é a quantidade de elementos^2, então:
    print("A quantidade de comparações no BubbleSort foi: %d"%(len(lista)**2))




    #Cuidando dos dados da pesquisa
    inicio_pesquisa = time.time()
    

    posicao = pesquisaLinear(lista, 7500)
    print("PosiÃ§Ã£o do item Ã© %d"%(posicao))

    fim_pesquisa = time.time()
    tempo_pesquisa = (fim_pesquisa) - (inicio_pesquisa)
    print("O tempo total da pesquisa Ã©: %f"%(tempo_pesquisa))
    





    TempoTotal = (tempo_ordenacao) + (tempo_pesquisa)
    print("O tempo total foi: %f"%(TempoTotal))

    


if (__name__ == "__main__"):
    main()
