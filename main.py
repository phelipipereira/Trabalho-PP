from heap import Heap
import os
from colorama import init, Back, Style
init(autoreset=True)

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
        print("\nHeap não encontrado.")
    input("\nPressione <Enter> para continuar...")


def criar_heap(heaps: dict) -> None:
    limpar_tela()
    print("Antes de criar seu heap informe o tipo:\n\n")
    print("1 - Best Heap (menor bloco disponível)")
    print("2 - Worst Heap (maior bloco disponível)")
    print("3 - First Heap (primeiro bloco disponível)")
    print("4 - Next Heap (aloca circularmente)")

    tipo = input("\nDigite a opção desejada (1-4): ")
    nome, tamanho = input("\nDigite o nome do heap e o número de alocações, respectivamente: ").split()
    tamanho = int(tamanho)
    heaps[nome] = Heap(tamanho, tipo)
    limpar_tela()
    print(f"Heap '{nome}' criado com tipo {tipo} e capacidade {tamanho}.")
    heaps[nome].exibe()
    input("\nPressione <Enter> para continuar...")


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
        print("\nHeap não encontrado.")
        input("\nPressione <Enter> para continuar...")
        return

    try:
        tamanho = int(input("\nQuantos blocos deseja alocar? "))
    except ValueError:
        print("\nValor inválido.")
        input("\nPressione <Enter> para continuar...")
        return

    label = input("\nDigite um nome para esta alocação: ")
    heaps[alvo].alocar(tamanho, label)
    input("\nPressione <Enter> para continuar...")


def desalocar_heap(heaps: dict) -> None:
    limpar_tela()
    if not heaps:
        print("\nNenhum heap criado ainda.")
        input("\nPressione <Enter> para continuar...")
        return

    limpar_tela()
    print("Heaps disponíveis:")
    for nome in heaps:
        print(f"- {nome}")

    alvo = input("\nDigite o nome do heap para desalocar: ")
    if alvo not in heaps:
        print("\nHeap não encontrado.")
        input("\nPressione <Enter> para continuar...")
        return

    limpar_tela()
    
    heap_obj = heaps[alvo]
    if not heap_obj.alocados:
        print("\nNenhuma alocação existente neste heap.")
        input("\nPressione <Enter> para continuar...")
        return
    heaps[alvo].exibe()

    nome_bloco = input("\nDigite o nome da alocação que deseja desalocar: ")
    result = heap_obj.desalocar(nome_bloco)
    if result:
        print(f"\nAlocação '{nome_bloco}' desalocada com sucesso.")
    else:
        print(f"\nAlocação '{nome_bloco}' não encontrada.")
    input("\nPressione <Enter> para continuar...")


def alterar_heap(heaps: dict) -> None:
    limpar_tela()
    if not heaps:
        print("\nNenhum heap criado ainda.")
        input("\nPressione <Enter> para continuar...")
        return

    limpar_tela()
    print("Heaps disponíveis:")
    for nome in heaps:
        print(f"- {nome}")

    alvo = input("\nDigite o nome do heap para alterar tipo: ")
    if alvo not in heaps:
        print("\nHeap não encontrado.")
        input("\nPressione <Enter> para continuar...")
        return

    novo_tipo = input("\nDigite o novo tipo (1-4): ")
    heaps[alvo].tipo = novo_tipo
    print(f"\nTipo do heap '{alvo}' alterado para {novo_tipo}.")
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
        print("5 - Alterar Tipo do Heap")
        print("6 - Desalocar")
        print("7 - Sair\n")

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
            alterar_heap(heaps)
        elif opcao == "6":
            desalocar_heap(heaps)
        elif opcao == "7":
            limpar_tela()
            print("Saindo...\n")
            break
        else:
            print("\nOpção inválida.")
            input("\nPressione <Enter> para continuar...")


if __name__ == "__main__":
    menu_principal()