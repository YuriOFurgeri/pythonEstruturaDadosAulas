from no_duplamente_ligada import NoDuplamenteLigada

class ListaDuplamenteLigada():
    def __init__(self):
        self.__primeiro_no = None
        self.__ultimo_no = None
        self.__tamanho = 0
    
    @property
    def tamanho(self):
        return self.__tamanho

    def inserir(self, elemento):
        novo_no = NoDuplamenteLigada(elemento)
        if self.esta_vazia():
            self.__primeiro_no = novo_no
            self.__ultimo_no = novo_no
        else:
            self.__ultimo_no.proximo = novo_no
            novo_no.anterior = self.__ultimo_no # Novo
            self.__ultimo_no = novo_no
        self.__tamanho += 1

    def inserir_posicao(self, posicao, elemento):
        if posicao == 0:
            novo_no = NoDuplamenteLigada(elemento) # Alteração
            novo_no.proximo = self.__primeiro_no
            self.__primeiro_no.anterior = novo_no # Novo
            self.__primeiro_no = novo_no
        elif posicao == self.__tamanho:
            novo_no = NoDuplamenteLigada(elemento) # Alteração
            self.__ultimo_no.proximo = novo_no 
            novo_no.anterior = self.__ultimo_no # Novo
            self.__ultimo_no = novo_no
        else:
            no_atual = self.recuperar_no(posicao)
            no_anterior = no_atual.anterior # Troca de linha e Alteração 
            novo_no = NoDuplamenteLigada(elemento)
            no_anterior.proximo = novo_no
            novo_no.proximo = no_atual
            no_atual.anterior = novo_no # Novo
            novo_no.anterior = no_anterior # Novo
        self.__tamanho += 1

    def contem(self, elemento):
        for i in range(self.__tamanho):
            no_atual = self.recuperar_no(i)
            if no_atual.elemento == elemento:
                return True
        return False

    def indice(self, elemento):
        for i in range(self.__tamanho):
            no_atual = self.recuperar_no(i)
            if no_atual.elemento == elemento:
                return i
        return -1

    def esta_vazia(self):
        return self.__tamanho == 0

    def __str__(self):
        temp = self.__primeiro_no
        elementos = ''
        while(temp):
            elementos = f'{elementos}{temp.elemento} '
            temp = temp.proximo
        return elementos
    
    # Método Novo - Só para teste (não foi pedido na atividade)    
    def imprimir_reverso(self):
        temp = self.__ultimo_no
        elementos = ''
        while(temp):
            elementos = f'{elementos}{temp.elemento} '
            temp = temp.anterior
        return elementos

    def recuperar_elemento_no(self, posicao):
        no = self.recuperar_no(posicao)
        if no != None:
            return no.elemento
        return None

    def recuperar_no(self, posicao):
        resultado = 0
        for i in range(posicao + 1):
            if i == 0:
                resultado = self.__primeiro_no
            else:
                resultado = resultado.proximo
        return resultado

    def remover_elemento(self, elemento):
        no_remover = self.indice(elemento)
        if no_remover == -1:
            print("Elemento não existe")
        self.remover_posicao(no_remover)

    def remover_posicao(self, posicao):
        if posicao == 0:
            proximo_no = self.__primeiro_no.proximo
            self.__primeiro_no.proximo = None # Novo
            self.__primeiro_no.anterior = None # Novo
            self.__primeiro_no = proximo_no
        elif posicao == self.__tamanho - 1:
            penultimo_no = self.__ultimo_no.anterior # Alteração 
            penultimo_no.proximo = None
            self.__ultimo_no.anterior = None # Novo
            self.__ultimo_no = penultimo_no
        else:
            no_remover = self.recuperar_no(posicao)
            no_anterior = no_remover.anterior # Alteração
            no_proximo = no_remover.proximo # Novo
            no_anterior.proximo = no_proximo # Alteração
            no_proximo.anterior = no_anterior # Novo
            no_remover.proximo = None
            no_remover.anterior = None # Novo
        self.__tamanho -= 1