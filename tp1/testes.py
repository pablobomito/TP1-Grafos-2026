from math import isclose, inf
from pathlib import Path

from grafo import (
    ler_grafo,
    ordem,
    tamanho,
    densidade,
    vizinhos,
    grau,
    busca_em_largura,
    componentes_conexas,
    possui_ciclo,
    vertices_articulacao,
    caminhos_minimos,
)


PASTA = Path(__file__).parent / "instancias"


def testar_instancia_1():
    grafo = ler_grafo(PASTA / "instancia1_pequeno_conexo.txt")

    assert ordem(grafo) == 10
    assert tamanho(grafo) == 12
    assert isclose(densidade(grafo), 24 / 90)
    assert vizinhos(grafo, 1) == [2, 3]
    assert grau(grafo, 1) == 2
    assert vertices_articulacao(grafo) == [3, 4, 7, 9]
    assert possui_ciclo(grafo)

    sequencia, _, fora = busca_em_largura(grafo, 1)
    assert sequencia == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert fora == [(2, 3), (5, 6), (8, 9)]

    caminhos = caminhos_minimos(grafo, 1)
    assert isclose(caminhos[10][0], 16.0)
    assert caminhos[10][1] == [1, 2, 3, 4, 7, 9, 10]


def testar_instancia_2():
    grafo = ler_grafo(PASTA / "instancia2_desconexo.txt")

    assert ordem(grafo) == 12
    assert tamanho(grafo) == 11
    assert componentes_conexas(grafo) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert vertices_articulacao(grafo) == [3, 6, 7]
    assert possui_ciclo(grafo)

    caminhos = caminhos_minimos(grafo, 1)
    assert caminhos[4][1] == [1, 3, 4]
    assert caminhos[8][0] == inf
    assert caminhos[8][1] == []


def testar_instancias_maiores():
    grafo_3 = ler_grafo(PASTA / "instancia3_esparso_80.txt")
    grafo_4 = ler_grafo(PASTA / "instancia4_denso_500.txt")

    assert ordem(grafo_3) == 80
    assert tamanho(grafo_3) == 109
    assert len(componentes_conexas(grafo_3)) == 1

    assert ordem(grafo_4) == 500
    assert tamanho(grafo_4) == 10498
    assert len(componentes_conexas(grafo_4)) == 1
    assert densidade(grafo_4) > densidade(grafo_3)


if __name__ == "__main__":
    testar_instancia_1()
    testar_instancia_2()
    testar_instancias_maiores()
    print("Testes concluidos sem erros.")
