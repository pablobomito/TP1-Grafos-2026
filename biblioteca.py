import sys

def main():

    nome_arquivo = sys.argv[1]

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        numero_vertices = int(arquivo.readline().strip())

        matrix = [[0 for _ in range(numero_vertices)]
                  for _ in range(numero_vertices)]


        #Lendo p arquivo e criando a matrix de valores
        for linha in arquivo:
            v1, v2, peso = linha.strip().split()

            v1 = int(v1)
            v2 = int(v2)
            peso = float(peso)

            matrix[v1 - 1][v2 - 1] = peso
            matrix[v2 - 1][v1 - 1] = peso

    for linha in matrix:
        print(linha)


if __name__ == "__main__":
    main()


#python biblioteca.py entrada.txt