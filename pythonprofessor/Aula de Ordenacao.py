#import random
def mergeSort(lista, inicio = 0, final = None):
    if final is None: # Se o final for igual a None
        final = len(lista) # Eu pego o tamanho da lista 
        
    if (final - inicio) > 1: # Verifica se eu tenho mais que um elemento na lista
        meio = (inicio + final)//2 # Somar Incio + Final e pego a parte Inteira
        mergeSort(lista, inicio, meio)
        #print(f'Dividi o lado da esquerda {inicio} , {final} ')
        mergeSort(lista, meio, final)
        #print(f'Dividi o lado da direita  {inicio} , {final}')
        merge(lista, inicio,meio, final)
        #print('Tenta Juntar')

def merge(lista, inicio, meio, final):
    pilha_esquerda = lista[inicio:meio]
    pilha_direita = lista[meio:final]
    topo_esquerda, topo_direita = 0, 0 
    for k in range(inicio, 10):
        if topo_esquerda >= len(pilha_esquerda):
            lista[k] = pilha_direita[topo_direita]
            topo_direita = topo_direita + 1
        elif topo_direita >= len(pilha_direita):
            lista[k] = pilha_esquerda[topo_esquerda]
            topo_esquerda = topo_esquerda + 1
        elif pilha_esquerda[topo_esquerda] < pilha_direita[topo_direita]:
            lista[k] = pilha_esquerda[topo_esquerda]
            topo_esquerda = topo_esquerda + 1
        else:
            lista[k] = pilha_direita[topo_direita]
            topo_direita = topo_direita + 1


def quicksort(lista, inicio = 0, final = None):
    if final is None:
        final = len(lista)-1
    #print(inicio)
    if inicio < final:
        p = particao(lista, inicio, final)
        print(p)
        # Recursividade na sublista da esquerda
        quicksort(lista, inicio, p-1)
        # Recursividade na sublista da Direita
        quicksort(lista, p+1, final)
            
def particao(lista, inicio, final):
    pivot = lista[final]
    i = inicio
    #print(inicio)
    #print(final)
    for j in range(inicio, final):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[final] = lista[final], lista[i]
    return i
    








repetidos   = [9,5,4,3,1,4]
print(repetidos)
quicksort(repetidos)
print(repetidos)




#aleatorios  = random.sample(range(1,1000) , 42)
#ordenados   = [1,2,4,5,6,7,8,9,20,22,28,32,34,39,40,42]
#inverso     = [42,40,39,34,32,28,22,20,9,8,7,6,5,4,3,2,1]


#teste = {   
#    'Numeros Aleatorios' : aleatorios,
#    'Já ordenados ' : ordenados,
#    'Ordem inverso' : inverso,
#    'Elementos Repetidos' : repetidos
#        }
        
#print(30 * '*')

#for name, lista in teste.items():
#    print("\nCaso de Teste: {}".format(name))
#    print(lista)
#    Ordenacao(lista)
#    print("\n Ordenado:")
    #print(lista)

#print(30 * '*')

