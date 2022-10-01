from lista import Lista

lista = Lista()

lista.adicionar(1)
lista.adicionar(2, inicio=True)
lista.adicionar(3)
lista.adicionar(4)
lista.adicionar(5)
lista.adicionar(6, inicio=True)

lista.show()

lista.remover(3)
lista.remover(5)
lista.remover(6)

lista.show()