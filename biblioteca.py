import sys

def lerGrafo(nome_arquivo):

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        numero_vertices = int(arquivo.readline().strip())

        matrix = [[0 for _ in range(numero_vertices)]
                  for _ in range(numero_vertices)]

        for linha in arquivo:
            v1, v2, peso = linha.strip().split()

            v1 = int(v1)
            v2 = int(v2)
            peso = float(peso)

            matrix[v1 - 1][v2 - 1] = peso
            matrix[v2 - 1][v1 - 1] = peso

    return matrix

def getOrdem(nome_arquivo):

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        numero_vertices = int(arquivo.readline().strip())

    return numero_vertices

def getTamanho(nome_arquivo):

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        numero_arestas = 0
        
        for linha in arquivo:
            numero_arestas += 1
    
    return numero_arestas - 1

def getDensidade(nome_arquivo):

    densidade = getOrdem(nome_arquivo)/getTamanho(nome_arquivo)

    return densidade

def getVizinhos(nome_arquivo, vertice):
    grafo = lerGrafo(nome_arquivo)

    vizinhos = []
    i = 0

    for peso in grafo[vertice - 1]:
        i += 1
        if peso != 0:
            vizinhos.append(i)

    return vizinhos

def getGrau(nome_arquivo, vertice):
    grafo = lerGrafo(nome_arquivo)

    grau = 0

    for peso in grafo[vertice - 1]:
        if peso != 0:
            grau += 1

    return grau

#Aqui só para motivos de testes
def main():
    grafo = lerGrafo("entrada.txt")

    for linha in grafo:
        print(linha)

    print("\nOrdem:", getOrdem("entrada.txt"))
    print("Tamanho:", getTamanho("entrada.txt"))
    print("Densidade:", getDensidade("entrada.txt"))

    print("\nVizinhos do Vertice 2:", getVizinhos("entrada.txt", 2))
    print("Grau do Vertice 2:", getGrau("entrada.txt", 2))




if __name__ == "__main__":
    main()

#python biblioteca.py