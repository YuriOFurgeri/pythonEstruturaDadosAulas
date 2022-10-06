class NoDuplamenteLigada():
    def __init__(self, elemento, proximo = None, anterior = None): # Alteração
        self.__elemento = elemento
        self.__proximo = proximo
        self.__anterior = anterior # Novo

    @property
    def elemento(self):
        return self.__elemento

    @elemento.setter
    def elemento(self, elemento):
        self.__elemento = elemento

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proximo(self, proximo):
        self.__proximo = proximo

    # Daqui pra baixo, tudo novo
    @property 
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior