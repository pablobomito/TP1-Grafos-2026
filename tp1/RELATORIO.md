# Trabalho I - Teoria e Modelo de Grafos

**Disciplina:** CCF-331 - Teoria e Modelo de Grafos  
**Professor:** Marcus Henrique Soares Mendes  
**Integrantes:** preencher nomes e matriculas

## 1. Objetivo

O objetivo do trabalho foi implementar uma biblioteca para manipulacao de grafos nao direcionados e ponderados. A representacao usada foi uma matriz de adjacencia, em que o valor armazenado corresponde ao peso da aresta e o valor zero indica que nao existe ligacao entre os vertices.

## 2. Leitura do grafo

A primeira linha do arquivo informa a quantidade de vertices. As linhas seguintes seguem o formato:

```text
v1 v2 peso
```

Como o grafo e nao direcionado, cada aresta e colocada nas duas posicoes correspondentes da matriz.

## 3. Funcoes implementadas

Foram implementadas as seguintes operacoes:

- ordem do grafo;
- tamanho do grafo;
- densidade;
- vizinhos de um vertice;
- grau de um vertice;
- verificacao de vertice de articulacao;
- busca em largura;
- componentes conexas;
- deteccao de ciclos;
- caminhos minimos.

A densidade foi calculada por:

`2m / (n(n-1))`

onde `n` e o numero de vertices e `m` e o numero de arestas.

Na busca em largura foi usada uma fila. Alem da ordem de visita, o programa informa as arestas da arvore de busca e as arestas da componente que nao entraram na arvore.

Para encontrar componentes conexas, foi feita uma busca em largura a partir de cada vertice ainda nao visitado.

A deteccao de ciclos foi feita com busca em profundidade. Quando a busca encontra um vertice ja visitado que nao e o pai do vertice atual, existe um ciclo.

Os vertices de articulacao foram encontrados com uma DFS que guarda o tempo de descoberta e o menor tempo de descoberta que pode ser alcancado a partir de cada subarvore.

Para caminhos minimos foi usado o algoritmo de Dijkstra, ja que os pesos das arestas sao positivos. Alem da distancia, o programa guarda o vertice anterior para conseguir montar o caminho encontrado.

## 4. Instancias de teste

Foram usadas quatro instancias diferentes.

### Instancia 1 - grafo pequeno e conexo

- 10 vertices
- 12 arestas
- densidade aproximada de 0,2667
- possui ciclos
- vertices de articulacao: 3, 4, 7 e 9

Na BFS iniciada no vertice 1, a sequencia obtida foi:

`1, 2, 3, 4, 5, 6, 7, 8, 9, 10`

O menor caminho de 1 ate 10 foi:

`1 -> 2 -> 3 -> 4 -> 7 -> 9 -> 10`

com distancia total igual a 16.

### Instancia 2 - grafo desconexo

A instancia possui 12 vertices e 3 componentes:

- 1, 2, 3, 4
- 5, 6, 7, 8
- 9, 10, 11, 12

Ela foi usada principalmente para testar componentes conexas e caminhos entre vertices que nao pertencem a mesma componente.

### Instancia 3 - grafo esparso

- 80 vertices
- 109 arestas
- densidade aproximada de 0,0345

A quantidade pequena de arestas em relacao ao numero de possibilidades permite observar o funcionamento da biblioteca em um grafo esparso.

### Instancia 4 - grafo maior

- 500 vertices
- 10498 arestas
- densidade aproximada de 0,0842

Essa instancia foi usada para verificar o funcionamento das funcoes com uma entrada maior e mais densa que a instancia anterior.

## 5. Validacao

Foi criado o arquivo `testes.py` com casos conhecidos das instancias menores e algumas verificacoes das instancias maiores.

Entre os valores conferidos estao ordem, tamanho, densidade, vizinhos, grau, componentes, articulacoes, ciclos, BFS e Dijkstra.

A execucao dos testes termina com a mensagem:

```text
Testes concluidos sem erros.
```

## 6. Conclusao

A biblioteca implementa as operacoes pedidas para grafos nao direcionados ponderados representados por matriz. As quatro instancias permitem testar situacoes diferentes, incluindo grafo conexo, desconexo, esparso e uma entrada maior.
