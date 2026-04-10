import numpy as np
from gaussian_elimination import rowmult, rowsum, rowswap


def lu(M: list[list[float]], partial_pivot: bool = False):
    """Dada una matriz M regresa su factorización LU"""
    n = len(M)
    U = [row for row in M]

    print("Matriz inicial")
    print(np.array(M))
    print()

    # Inicializa la matriz L como la identidad
    L = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        L[i][i] = 1

    if partial_pivot:
        # Se hara la factorización de la forma PA = LU, con P una matriz de permutacion

        # Inicializa la matriz P como la identidad
        P = [[0.0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            P[i][i] = 1.0

        # Diagonaliza la matriz usando pivote parcial
        for i in range(n):
            # Encuentra el indice del pivote maximo
            pivotes = []
            for pivot in range(i, n):
                pivotes.append(U[pivot][i])
            max_pivot = max(pivotes, key=abs)
            max_index = pivotes.index(max_pivot) + i

            # Intercambia la fila del pivote maximo con la actual, y realiza la misma operacion para P
            U = rowswap(U, i, max_index)
            P = rowswap(P, i, max_index)

            # Elimina los valores debajo de la diagonal
            for j in range(i + 1, n):
                aji = U[j][i]
                L[max_index][i] = aji / max_pivot
                U[j] = rowsum(U, j, i, -aji / max_pivot)

        print("Matriz U")
        print(np.array(U))
        print()
        print("Matriz L")
        print(np.array(L))
        print()
        print("Matriz P")
        print(np.array(P))
        print()
        print("Producto PA")
        print(np.dot(P, M))
        print()
        print("Producto LU")
        print(np.dot(L, U))

        return L, U, P

    else:
        # Diagonaliza la matriz
        for i in range(n):
            for j in range(i + 1, n):
                aji = U[j][i]
                pivot = U[i][i]
                L[j][i] = aji / pivot
                U[j] = rowsum(U, j, i, -aji / pivot)

        return L, U


def main():
    B = [[0.0, 5.0, 22 / 3], [4.0, 2.0, 1.0], [2.0, 7.0, 9.0]]
    L, U, P = lu(B, True)


if __name__ == "__main__":
    main()
