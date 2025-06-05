class BlocoLivre:
    def __init__(self, inicio, tamanho):
        self.inicio = inicio
        self.tamanho = tamanho

class BlocoAlocado:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final

class GerenciadorDeHeap:
    def __init__(self, tamanho, estrategia):
        self.heap = [0] * tamanho  # 0 = livre, 1 = ocupado
        self.livres = [BlocoLivre(0, tamanho)]
        self.alocados = []
        self.capacidade = tamanho
        self.numLivres = 1
        self.numAlocados = 0
        self.ultimaPosicao = 0
        self.estrategia = estrategia

    def definir_estrategia(self, estrategia):
        self.estrategia = estrategia
        print(f"Estratégia definida para: {estrategia}")

    def encontrar_bloco_livre(self, tamanho):
        indiceEscolhido = -1
        if self.estrategia == "best":
            menorTamanho = self.capacidade + 1
            for i, bloco in enumerate(self.livres):
                if bloco.tamanho >= tamanho and bloco.tamanho < menorTamanho:
                    menorTamanho = bloco.tamanho
                    indiceEscolhido = i
        elif self.estrategia == "worst":
            maiorTamanho = -1
            for i, bloco in enumerate(self.livres):
                if bloco.tamanho >= tamanho and bloco.tamanho > maiorTamanho:
                    maiorTamanho = bloco.tamanho
                    indiceEscolhido = i
        elif self.estrategia == "first":
            for i, bloco in enumerate(self.livres):
                if bloco.tamanho >= tamanho:
                    indiceEscolhido = i
                    break
        elif self.estrategia == "next":
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
            self.alocados.append(BlocoAlocado(bloco.inicio, bloco.inicio + tamanho - 1))
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
        self.livres.append(BlocoLivre(inicio, tamanho))
        self.numLivres += 1

    def exibe(self):
        print("\nEstado do Heap:")
        print("Legenda: [X] = Ocupado, [ ] = Livre\n")

        for bloco in self.heap:
            print("[X]" if bloco else "[ ]", end=" ")

        print("\n\nBlocos Alocados:")
        for i, bloco in enumerate(self.alocados, start=1):
            print(f"Bloco {i}: Início = {bloco.inicio}, Final = {bloco.final}")

# Programa principal
if __name__ == "__main__":
    gerenciador = GerenciadorDeHeap(10, "best")
    
    gerenciador.exibe()
    gerenciador.alocar(5)
    gerenciador.exibe()
    gerenciador.alocar(3)
    gerenciador.exibe()
    gerenciador.desalocar()
    gerenciador.exibe()

    gerenciador.definir_estrategia("next")
    gerenciador.alocar(8)
    gerenciador.exibe()

    gerenciador.definir_estrategia("best")
    gerenciador.alocar(2)
    gerenciador.exibe()
