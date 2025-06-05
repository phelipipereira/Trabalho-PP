from heap import Heap

def main(): 
    heaps = {}
    print("--------------------Olá--------------------\n\n")
    print("você deseja criar um heap?\n\n1-Sim\n2-Não")
    x = input("Digite: ")

    if x == "1":
        criar(heaps)

   
1
    

def criar(heaps):
    
    print("Antes de criar seu heap informe o tipo:\n\n")
    print("1-Best Heap\n2-worst Heap\n3-First Heap\n4-Next Heap\n")
    print("Digite o numero da opcao desejada: \n\n")
    tipo = (input("Digite um numero: "))
    nome, tamanho = input("Digite o nome do heap e o número de alocações: ").split()
    tamanho = int(tamanho)
    objeto = Heap(tamanho, tipo)  
    heaps[nome] = objeto 
    heaps[nome].exibe()
    

if __name__ == "__main__":
    main()
    





