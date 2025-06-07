from colorama import init, Back, Style
init(autoreset=True)

class Livre:
    def __init__(self, endereco, tamanho):
        self.inicio = endereco
        self.tamanho = tamanho

class Alocado:
    def __init__(self, label, inicio, final):
        self.label = label
        self.inicio = inicio
        self.final = final

class Heap:
    def __init__(self, tamanho, tipo):
        self.heap = [0] * tamanho
        self.livres = [Livre(0, tamanho)]
        self.alocados = []
        self.capacidade = tamanho
        self.numLivres = 1
        self.numAlocados = 0
        self.ultimaPosicao = 0
        self.tipo = tipo

    def encontrar_bloco_livre(self, tamanho):
        indiceEscolhido = -1
        if self.tipo == "1":  # Best
            menor = self.capacidade + 1
            for i, b in enumerate(self.livres):
                if b.tamanho >= tamanho and b.tamanho < menor:
                    menor = b.tamanho
                    indiceEscolhido = i
        elif self.tipo == "2":  # Worst
            maior = -1
            for i, b in enumerate(self.livres):
                if b.tamanho >= tamanho and b.tamanho > maior:
                    maior = b.tamanho
                    indiceEscolhido = i
        elif self.tipo == "3":  # First
            for i, b in enumerate(self.livres):
                if b.tamanho >= tamanho:
                    indiceEscolhido = i
                    break
        elif self.tipo == "4":  # Next
            start = self.ultimaPosicao
            for k in range(self.numLivres):
                i = (start + k) % self.numLivres
                b = self.livres[i]
                if b.tamanho >= tamanho:
                    indiceEscolhido = i
                    self.ultimaPosicao = (i + 1) % self.numLivres
                    break
        return indiceEscolhido

    def alocar(self, tamanho, label):
        idx = self.encontrar_bloco_livre(tamanho)
        if idx == -1:
            print(f"Erro: não foi possível alocar {tamanho} blocos.")
            return
        b = self.livres[idx]
        for i in range(b.inicio, b.inicio + tamanho):
            self.heap[i] = 1
        novo = Alocado(label, b.inicio, b.inicio + tamanho - 1)
        self.alocados.append(novo)
        self.numAlocados += 1
        if b.tamanho == tamanho:
            del self.livres[idx]
            self.numLivres -= 1
        else:
            b.inicio += tamanho
            b.tamanho -= tamanho
        print("Memória alocada com sucesso.")

    def desalocar(self, label) -> bool:
        for i, a in enumerate(self.alocados):
            if a.label == label:
                tamanho = a.final - a.inicio + 1
                for j in range(a.inicio, a.inicio + tamanho):
                    self.heap[j] = 0
                del self.alocados[i]
                self.numAlocados -= 1
                self.livres.append(Livre(a.inicio, tamanho))
                self.numLivres += 1
                return True
        return False

    def exibe(self) -> None:
        print("\nEstado do Heap:")
        print("Legenda: " + Back.RED + "[X]" + Style.RESET_ALL + " = Ocupado, "
              + Back.GREEN + "[ ]" + Style.RESET_ALL + " = Livre\n")
        for bit in self.heap:
            if bit:
                print(Back.RED + "[X]" + Style.RESET_ALL, end=" ")
            else:
                print(Back.GREEN + "[ ]" + Style.RESET_ALL, end=" ")
        print("\n\nBlocos Alocados:")
        for a in self.alocados:
            print(f"- {a.label}: Início = {a.inicio}, Final = {a.final}")