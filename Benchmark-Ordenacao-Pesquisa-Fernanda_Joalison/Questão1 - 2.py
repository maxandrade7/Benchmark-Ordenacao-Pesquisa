import time
import random

# Adicionar as funções de Ordenamento e Pesquisa.
def semOrdenacao(lista):
    pass

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
    random.shuffle(lista)
    
    print("Tamanho da lista: %d"%(len(lista)))

    Inicio = time.time()
    print("Tempo Inicial: %f"%(Inicio))

    semOrdenacao(lista)

    inicioPesquisa = time.time()
    print("Tempo inicial da Pesquisa: %f"%(inicioPesquisa))
    
    posicao = PesquisaBinaria(lista, 7500)
    print("Posicao do item: %d"%(posicao))

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

