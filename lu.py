import numpy as np
from gaussian_elimination import rowmult, rowsum, rowswap


def lu(M: list[list[float]]):
    """Dada una matriz M regresa su factorización LU"""
    n = len(M)

    if np.linalg.det(M) != 0:
        print("Acepta factorización LU")

        # Inicializa la matriz L como la identidad
        L = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            L[i][i] = 1

        # Diagonaliza la matriz
        for i in range(n):
            for j in range(i + 1, n):
                aji = M[j][i]
                pivot = M[i][i]
                L[j][i] = aji / pivot
                M[j] = rowsum(M, j, i, -aji / pivot)

                U = M
    else:
        # En el caso de que no sea posible una factorización LU, crea una matriz P identidad
        P = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            P[i][i] = 1

    return L, U


def main():
    A = [[25.0, 5.0, 1.0], [64.0, 8.0, 1.0], [144.0, 12.0, 1]]
    print(np.array(A))
    print()
    L, U = lu(A)
    print(np.array(L))
    print()
    print(np.array(U))
    print()
    print(np.dot(L, U))


if __name__ == "__main__":
    main()
