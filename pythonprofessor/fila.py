from lista_ligada import ListaLigada
class Fila():
    def __init__(self):
        self.__elementos = ListaLigada()

    def enfileirar(self, elemento):
        self.__elementos.inserir(elemento)

    def esta_vazia(self):
        return self.__elementos.esta_vazia()

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        resultado = self.__elementos.recuperar_elemento_no(0)
        self.__elementos.remover_posicao(0)
        return resultado

    def __str__(self):
        return self.__elementos.__str__()