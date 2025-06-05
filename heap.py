from bloco import Livre, Alocado

#Classe heap que é armazenado em um vetor que possui uma série de atributos.
class Heap:
    def __init__(self, tamanho, tipo):
            self.heap = [0] * tamanho  # 0 = livre, 1 = ocupado
            self.livres = [Livre(0, tamanho)]
            self.alocados = []
            self.capacidade = tamanho
            self.numLivres = 1
            self.numAlocados = 0
            self.ultimaPosicao = 0
            self.tipo = tipo

    def encontrar_bloco_livre(self, tamanho):
        indiceEscolhido = -1
        if self.tipo == "best":
            menorTamanho = self.capacidade + 1
            for i, bloco in enumerate(self.livres):
                if bloco.tamanho >= tamanho and bloco.tamanho < menorTamanho:
                    menorTamanho = bloco.tamanho
                    indiceEscolhido = i
        elif self.tipo == "worst":
            maiorTamanho = -1
            for i, bloco in enumerate(self.livres):
                if bloco.tamanho >= tamanho and bloco.tamanho > maiorTamanho:
                    maiorTamanho = bloco.tamanho
                    indiceEscolhido = i
        elif self.tipo == "first":
            for i, bloco in enumerate(self.livres):
                if bloco.tamanho >= tamanho:
                    indiceEscolhido = i
                    break
        elif self.tipo == "next":
            inicio = self.ultimaPosicao
            for i in range(self.numLivres):
                posicaoAtual = (inicio + i) % self.numLivres
                bloco = self.livres[posicaoAtual]
                if bloco.tamanho >= tamanho:
                    indiceEscolhido = posicaoAtual
                    self.ultimaPosicao = (posicaoAtual + 1) % self.numLivres
                    break
        return indiceEscolhido

    def alocar(self, tamanho):
        indice = self.encontrar_bloco_livre(tamanho)
        if indice != -1:
            bloco = self.livres[indice]
            for i in range(bloco.inicio, bloco.inicio + tamanho):
                self.heap[i] = 1
            self.alocados.append(Alocado(bloco.inicio, bloco.inicio + tamanho - 1))
            self.numAlocados += 1
            if bloco.tamanho == tamanho:
                del self.livres[indice]
                self.numLivres -= 1
            else:
                bloco.inicio += tamanho
                bloco.tamanho -= tamanho
            print("Memória alocada com sucesso.")
        else:
            print(f"Erro: Não foi possível alocar {tamanho} blocos.")

    def desalocar(self, inicio, tamanho):
        for i in range(inicio, inicio + tamanho):
            self.heap[i] = 0
        for i, bloco in enumerate(self.alocados):
            if bloco.inicio == inicio:
                del self.alocados[i]
                self.numAlocados -= 1
                break
        self.livres.append(Livre(inicio, tamanho))
        self.numLivres += 1

    def exibe(self):
        print("\nEstado do Heap:")
        print("Legenda: [X] = Ocupado, [ ] = Livre\n")
        for bloco in self.heap:
            print("[X]" if bloco else "[ ]", end=" ")
        print("\n\nBlocos Alocados:")
        for i, bloco in enumerate(self.alocados, start=1):
            print(f"Bloco {i}: Início = {bloco.inicio}, Final = {bloco.final}")

    
        


