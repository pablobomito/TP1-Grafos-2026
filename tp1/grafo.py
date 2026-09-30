from collections import deque
from math import inf


def ler_grafo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        n = int(arquivo.readline().strip())
        matriz = [[0.0] * n for _ in range(n)]

        for linha in arquivo:
            if not linha.strip():
                continue

            v1, v2, peso = linha.split()
            v1 = int(v1) - 1
            v2 = int(v2) - 1
            peso = float(peso)

            if peso <= 0:
                raise ValueError("O peso da aresta deve ser positivo.")
            if v1 == v2:
                raise ValueError("O grafo nao pode ter laco.")
            if not (0 <= v1 < n and 0 <= v2 < n):
                raise ValueError("Vertice fora do intervalo do grafo.")

            matriz[v1][v2] = peso
            matriz[v2][v1] = peso

    return matriz


def validar_vertice(grafo, vertice):
    if vertice < 1 or vertice > len(grafo):
        raise ValueError("Vertice invalido.")


def ordem(grafo):
    return len(grafo)


def tamanho(grafo):
    total = 0
    n = len(grafo)

    for i in range(n):
        for j in range(i + 1, n):
            if grafo[i][j] != 0:
                total += 1

    return total


def densidade(grafo):
    n = ordem(grafo)
    if n < 2:
        return 0.0

    m = tamanho(grafo)
    return (2 * m) / (n * (n - 1))


def vizinhos(grafo, vertice):
    validar_vertice(grafo, vertice)
    linha = grafo[vertice - 1]
    resultado = []

    for i in range(len(linha)):
        if linha[i] != 0:
            resultado.append(i + 1)

    return resultado


def grau(grafo, vertice):
    return len(vizinhos(grafo, vertice))


def busca_em_largura(grafo, inicio):
    validar_vertice(grafo, inicio)

    visitados = set([inicio])
    fila = deque([inicio])
    sequencia = []
    arestas_arvore = []

    while fila:
        atual = fila.popleft()
        sequencia.append(atual)

        for vizinho in vizinhos(grafo, atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                arestas_arvore.append((atual, vizinho))

    arestas_arvore_normalizadas = set()
    for a, b in arestas_arvore:
        arestas_arvore_normalizadas.add(tuple(sorted((a, b))))

    arestas_fora = []
    n = len(grafo)

    for i in range(n):
        for j in range(i + 1, n):
            if grafo[i][j] != 0:
                a = i + 1
                b = j + 1
                if a in visitados and b in visitados:
                    if (a, b) not in arestas_arvore_normalizadas:
                        arestas_fora.append((a, b))

    return sequencia, arestas_arvore, arestas_fora


def componentes_conexas(grafo):
    n = len(grafo)
    visitados = set()
    componentes = []

    for inicio in range(1, n + 1):
        if inicio in visitados:
            continue

        componente = []
        fila = deque([inicio])
        visitados.add(inicio)

        while fila:
            atual = fila.popleft()
            componente.append(atual)

            for vizinho in vizinhos(grafo, atual):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

        componente.sort()
        componentes.append(componente)

    return componentes


def possui_ciclo(grafo):
    n = len(grafo)
    visitado = [False] * n

    def dfs(atual, pai):
        visitado[atual] = True

        for proximo in range(n):
            if grafo[atual][proximo] == 0:
                continue

            if not visitado[proximo]:
                if dfs(proximo, atual):
                    return True
            elif proximo != pai:
                return True

        return False

    for i in range(n):
        if not visitado[i] and dfs(i, -1):
            return True

    return False


def vertices_articulacao(grafo):
    n = len(grafo)
    tempo = 0
    descoberta = [-1] * n
    menor = [-1] * n
    pai = [-1] * n
    resultado = set()

    def dfs(atual):
        nonlocal tempo

        descoberta[atual] = tempo
        menor[atual] = tempo
        tempo += 1
        filhos = 0

        for proximo in range(n):
            if grafo[atual][proximo] == 0:
                continue

            if descoberta[proximo] == -1:
                pai[proximo] = atual
                filhos += 1
                dfs(proximo)
                menor[atual] = min(menor[atual], menor[proximo])

                if pai[atual] == -1 and filhos > 1:
                    resultado.add(atual + 1)
                elif pai[atual] != -1 and menor[proximo] >= descoberta[atual]:
                    resultado.add(atual + 1)

            elif proximo != pai[atual]:
                menor[atual] = min(menor[atual], descoberta[proximo])

    for i in range(n):
        if descoberta[i] == -1:
            dfs(i)

    return sorted(resultado)


def eh_articulacao(grafo, vertice):
    validar_vertice(grafo, vertice)
    return vertice in vertices_articulacao(grafo)


def dijkstra(grafo, origem):
    validar_vertice(grafo, origem)

    n = len(grafo)
    distancias = [inf] * n
    anterior = [None] * n
    visitado = [False] * n
    distancias[origem - 1] = 0

    for _ in range(n):
        atual = -1
        menor_distancia = inf

        for i in range(n):
            if not visitado[i] and distancias[i] < menor_distancia:
                menor_distancia = distancias[i]
                atual = i

        if atual == -1:
            break

        visitado[atual] = True

        for proximo in range(n):
            peso = grafo[atual][proximo]
            if peso == 0 or visitado[proximo]:
                continue

            nova_distancia = distancias[atual] + peso
            if nova_distancia < distancias[proximo]:
                distancias[proximo] = nova_distancia
                anterior[proximo] = atual

    return distancias, anterior


def montar_caminho(anterior, origem, destino):
    if origem == destino:
        return [origem]

    caminho = []
    atual = destino - 1

    while atual is not None:
        caminho.append(atual + 1)
        if atual == origem - 1:
            break
        atual = anterior[atual]

    caminho.reverse()

    if not caminho or caminho[0] != origem:
        return []

    return caminho


def caminhos_minimos(grafo, origem):
    distancias, anterior = dijkstra(grafo, origem)
    resultado = {}

    for destino in range(1, len(grafo) + 1):
        if distancias[destino - 1] == inf:
            resultado[destino] = (inf, [])
        else:
            caminho = montar_caminho(anterior, origem, destino)
            resultado[destino] = (distancias[destino - 1], caminho)

    return resultado
