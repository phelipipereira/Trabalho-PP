class Livre:
    def __init__(self, endereco, tamanho):
        self.inicial = endereco
        self.tamanho = tamanho

class Alocado:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final