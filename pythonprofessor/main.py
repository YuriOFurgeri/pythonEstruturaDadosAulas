from array import array
from vetores import Vetor
from lista_ligada import ListaLigada
from lista_duplamente_ligada import ListaDuplamenteLigada
from fila import Fila
from pilha import Pilha


print(30 * "-", "MENU", 30 * "-")
print("1. Vetores")
print("2. Listas Ligadas")
print("3. Listas Duplamente Ligadas")
print("4. Pilhas")
print("5. Filas")

menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetor_teste = Vetor(0)
    vetor_teste.inserir_elemento_posicao(1, 0)
    vetor_teste.inserir_elemento_posicao(2, 1)
    vetor_teste.inserir_elemento_posicao(3, 2)
    vetor_teste.inserir_elemento_posicao(4, 2)
    vetor_teste.inserir_elemento_posicao(5, 2)
    vetor_teste.inserir_elemento_final(1)
    print(vetor_teste.tamanho_vetor())
    print(vetor_teste)
    # print(vetor_teste.contem(8))
    print(vetor_teste.indice(4))
    vetor_teste.remover_elemento_indice(3)
    print(vetor_teste)
    vetor_teste.remover_elemento(5)
    print(vetor_teste)
    # print(vetor_teste)

elif menu == 2:
    lista_teste = ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(2, 10)
    print(lista_teste)
    lista_teste.remover_elemento(4)
    print(lista_teste)
    print(lista_teste.contem(5))
    print(lista_teste.indice(55))

    print(lista_teste.recuperar_elemento_no(3))

elif menu == 3:
    lista_teste = ListaDuplamenteLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(2, 10)
    print(lista_teste)
    #lista_teste.remover_elemento(4)
    lista_teste.remover_posicao(1)
    print(lista_teste)
    # print(lista_teste.contem(5))
    # print(lista_teste.indice(55))
    print(lista_teste.imprimir_reverso())

    # print(lista_teste.recuperar_elemento_no(3))
elif menu == 4:
    pilha_teste = Pilha()
    pilha_teste.empilhar(1)
    pilha_teste.empilhar(2)
    pilha_teste.empilhar(3)
    print(pilha_teste)
    print(pilha_teste.desempilhar())
    print(pilha_teste.desempilhar())
    print(pilha_teste.desempilhar())
    print(pilha_teste.desempilhar())
    print(pilha_teste)
elif menu == 5:
    fila_teste = Fila()
    fila_teste.enfileirar(1)
    fila_teste.enfileirar(2)
    fila_teste.enfileirar(3)
    fila_teste.enfileirar(4)
    print(fila_teste)
    print(fila_teste.desenfileirar())
    print(fila_teste)
    print(fila_teste.desenfileirar())
    print(fila_teste)    
else:
    print("Opção inválida")

