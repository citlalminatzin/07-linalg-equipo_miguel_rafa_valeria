import numpy as np


def rowsum(M: list[list[float]], i: int, j: int, factor: float):
    return [ai + (bi * factor) for ai, bi in zip(M[i], M[j])]


def rowmult(M: list[list[float]], i: int, factor: float):
    return [ai * factor for ai in M[i]]


def rowswap(M: list[list[float]], i: int, j: int):
    temp = M[i]
    M[i] = M[j]
    M[j] = temp
    return M


def gaussian_elimination(M: list[list[float]]):
    """Dada una matriz M, regresa una matriz triangular superior"""
    n = len(M)
    U = [row for row in M]

    for i in range(n):
        # Encuentra el indice del pivote maximo
        pivotes = []
        for pivot in range(i, n):
            pivotes.append(U[pivot][i])
        max_pivot = max(pivotes, key=abs)
        max_index = pivotes.index(max_pivot) + i
        if max_pivot == 0:
            print("Ay...")
            return None

        # Intercambia la fila con el pivote maximo con la actual
        U = rowswap(U, i, max_index)

        # Elimina los valores debajo de la diagonal
        for j in range(i + 1, n):
            aji = U[j][i]
            pivot = U[i][i]
            U[j] = rowsum(U, j, i, -aji / pivot)

    return U


def triang_sup_to_diag(M: list[list[float]]):
    """
    Dada una matriz M traingular superior
    regresa una matriz diagonal
    """
    n = len(M)
    D = [row for row in M]

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pivote = D[-i][-i]
            aji = D[-j][-i]
            D[-j] = rowsum(D, -j, -i, -aji / pivote)

    return D


def diag(M: list[list[float]]):
    """Dada una matriz regresa una matriz diagonalizada"""
    D = [row for row in M]

    gauss = gaussian_elimination(D)
    if gauss is not None:
        return triang_sup_to_diag(gauss)
    else:
        print("Algun pivote es cero...")
        return None


def main(): ...


if __name__ == "__main__":
    main()
