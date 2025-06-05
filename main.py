from heap import Heap
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_heap(heaps: dict) -> None:
    if not heaps:
        print("\nNenhum heap criado ainda.")
        input("\nPressione <Enter> para continuar...")
        return

    limpar_tela()
    print("Heaps disponíveis:")
    for nome in heaps:
        print(f"- {nome}")

    alvo = input("\nDigite o nome do heap que deseja exibir: ")
    if alvo in heaps:
        heaps[alvo].exibe()
    else:
        print("\n Heap não encontrado.")
    input("\nPressione <Enter> para continuar...")


def criar_heap(heaps: dict) -> None:
    
    limpar_tela()
    print("Antes de criar seu heap informe o tipo:\n\n")
    print("1-Best Heap\n2-worst Heap\n3-First Heap\n4-Next Heap\n")

    tipo = (input("Digite da opção desejada: "))

    nome, tamanho = input("Digite o nome do heap e o número de alocações, respectivamente: ").split()
    tamanho = int(tamanho)
    heaps[nome] = Heap(tamanho, tipo)  
    
    heaps[nome].exibe()
   

def alocar_heap(heaps: dict):
    limpar_tela()
    if not heaps:
        print("\nNenhum heap criado ainda.")
        input("\nPressione <Enter> para continuar...")
        return

    limpar_tela()
    print("Heaps disponíveis:")
    for nome in heaps:
        print(f"- {nome}")

    alvo = input("\nDigite o nome do heap para alocar: ")
    if alvo not in heaps:
        print("\n Heap não encontrado.")
        input("\nPressione <Enter> para continuar...")
        return

    try:
        tamanho = int(input("Quantos blocos deseja alocar? "))
    except ValueError:
        print("\n Valor inválido.")
        input("\nPressione <Enter> para continuar...")
        return

    heaps[alvo].alocar(tamanho)
    input("\nPressione <Enter> para continuar...")


def menu_principal():
    
    heaps: dict[str, Heap] = {}

    while True:
        limpar_tela()
        print("---------------------- Menu ----------------------\n")
        print("1 - Novo Heap")
        print("2 - Deletar Heap")
        print("3 - Exibir Heap")
        print("4 - Alocar")
        print("5 - Sair\n")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            criar_heap(heaps)
        elif opcao == "2":
            deletar_heap(heaps)
        elif opcao == "3":
            exibir_heap(heaps)
        elif opcao == "4":
            alocar_heap(heaps)
        elif opcao == "5":
            print("Saindo...\n")
            break
        else:
            print("\nOpção inválida.")
            input("\nPressione <Enter> para continuar...")

if __name__ == "__main__":
    menu_principal()
    





