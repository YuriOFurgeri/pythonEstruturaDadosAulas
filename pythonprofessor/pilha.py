from lista_duplamente_ligada import ListaDuplamenteLigada
class Pilha():
    def __init__(self):
        self.__elementos = ListaDuplamenteLigada()

    def empilhar(self, elemento):
        self.__elementos.inserir(elemento)

    def esta_vazia(self):
        return self.__elementos.esta_vazia()

    def desempilhar(self):
        if self.esta_vazia():
            return None
        resultado = self.__elementos.recuperar_elemento_no(self.__elementos.tamanho -1)
        self.__elementos.remover_posicao(self.__elementos.tamanho -1)
        return resultado

    def __str__(self):
        temp = self.__elementos.__str__()
        return temp