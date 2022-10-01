from node import Node
class Lista:
    inicio = None
    def __init__(self):
        self.inicio = None

    #adicionar
    def adicionar(self, valor, inicio=False):
        if inicio:
            self.adicionar_no_inicio(valor)
        else:
            self.adicionar_no_fim(valor)

    #adicionar um node no início da lista
    def adicionar_no_inicio(self, valor):
        novo = Node(valor)
        novo.proximo = self.inicio
        self.inicio = novo

    #adiciona no fim
    def adicionar_no_fim(self, valor):
        if self.inicio == None:
            self.inicio = Node(valor, None)
        else:
            aux = self.inicio
            while aux.proximo != None:
                aux = aux.proximo
            aux.proximo = Node(valor, None)
            aux.proximo.anterior = aux

    #remover
    def remover(self, valor):
        aux = self.inicio
        if aux.valor == valor:
            
            self.inicio = aux.proximo

        else:

            while aux.proximo != None:
                aux = aux.proximo

                if aux.valor == valor:
                    aux.anterior.proximo = aux.proximo

    #mostrar
    def show(self):

        aux = self.inicio
        print("[", end='')

        while aux.proximo != None:

            print(f"{aux.valor}", end=', ')
            aux = aux.proximo

        print(f"{aux.valor}]")