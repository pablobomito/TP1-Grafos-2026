from math import inf
import os
import sys

from grafo import (
    ler_grafo,
    ordem,
    tamanho,
    densidade,
    vizinhos,
    grau,
    eh_articulacao,
    busca_em_largura,
    componentes_conexas,
    possui_ciclo,
    caminhos_minimos,
)


def ler_vertice(mensagem, n):
    while True:
        try:
            valor = int(input(mensagem))
            if 1 <= valor <= n:
                return valor
            print(f"Digite um vertice entre 1 e {n}.")
        except ValueError:
            print("Digite um numero inteiro.")


def mostrar_menu():
    print("\n========================================")
    print("ANALISE DE REDE SOCIAL")
    print("========================================")
    print("1 - Informar ordem do grafo")
    print("2 - Informar tamanho do grafo")
    print("3 - Calcular densidade")
    print("4 - Informar vizinhos de um vertice")
    print("5 - Informar grau de um vertice")
    print("6 - Verificar se um vertice e articulacao")
    print("7 - Executar busca em largura")
    print("8 - Identificar componentes conexas")
    print("9 - Verificar existencia de ciclos")
    print("10 - Calcular caminhos minimos")
    print("0 - Sair")


def main():
    if len(sys.argv) > 1:
        nome_arquivo = sys.argv[1]
    else:
        nome_arquivo = input("Arquivo do grafo [entrada.txt]: ").strip()
        if not nome_arquivo:
            nome_arquivo = "entrada.txt"

    if not os.path.exists(nome_arquivo):
        print("Arquivo nao encontrado.")
        return

    try:
        grafo = ler_grafo(nome_arquivo)
    except Exception as erro:
        print(f"Nao foi possivel ler o grafo: {erro}")
        return

    n = ordem(grafo)

    while True:
        mostrar_menu()
        opcao = input("Digite a opcao: ").strip()

        if opcao == "0":
            break

        elif opcao == "1":
            print(f"Ordem do grafo: {ordem(grafo)}")

        elif opcao == "2":
            print(f"Tamanho do grafo: {tamanho(grafo)}")

        elif opcao == "3":
            print(f"Densidade: {densidade(grafo):.6f}")

        elif opcao == "4":
            v = ler_vertice("Vertice: ", n)
            print("Vizinhos:", vizinhos(grafo, v))

        elif opcao == "5":
            v = ler_vertice("Vertice: ", n)
            print(f"Grau de {v}: {grau(grafo, v)}")

        elif opcao == "6":
            v = ler_vertice("Vertice: ", n)
            if eh_articulacao(grafo, v):
                print(f"O vertice {v} e de articulacao.")
            else:
                print(f"O vertice {v} nao e de articulacao.")

        elif opcao == "7":
            inicio = ler_vertice("Vertice inicial: ", n)
            sequencia, arvore, fora = busca_em_largura(grafo, inicio)
            print("Sequencia visitada:", sequencia)
            print("Arestas da arvore BFS:", arvore)
            print("Arestas fora da arvore BFS:", fora)

        elif opcao == "8":
            componentes = componentes_conexas(grafo)
            print(f"Numero de componentes: {len(componentes)}")
            for i, componente in enumerate(componentes, start=1):
                print(f"Componente {i}: {componente}")

        elif opcao == "9":
            print("O grafo possui ciclo." if possui_ciclo(grafo) else "O grafo nao possui ciclo.")

        elif opcao == "10":
            origem = ler_vertice("Vertice de origem: ", n)
            resultado = caminhos_minimos(grafo, origem)

            for destino in range(1, n + 1):
                distancia, caminho = resultado[destino]
                if distancia == inf:
                    print(f"{origem} -> {destino}: sem caminho")
                else:
                    caminho_txt = " -> ".join(str(v) for v in caminho)
                    print(f"{origem} -> {destino}: distancia = {distancia:.2f} | caminho = {caminho_txt}")

        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
