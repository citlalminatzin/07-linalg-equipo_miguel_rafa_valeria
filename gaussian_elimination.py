import numpy as np


def rowsum(M: list[list[float]], i: int, j: int, factor: float):
    return [ai + (bi * factor) for ai, bi in zip(M[i], M[j])]


def rowmul(M: list[list[float]], i: int, factor: float):
    return [ai * factor for ai in M[i]]


def gaussian_elimination(M: list[list[float]]):
    """Dada una matriz M, regresa una matriz triangular superior"""
    n = len(M)

    for i in range(n):
        pivot = M[i][i]
        if pivot != 0:
            M[i] = rowmul(M, i, 1 / pivot)
        else:
            print("Ay...")
        for j in range(i + 1, n):
            aij = M[j][i]
            M[j] = rowsum(M, j, i, -aij)
    return M


def triang_sup_to_diag(M: list[list[float]]):
    """
    Dada una matriz M traingular superior
    regresa una matriz diagonal
    """
    ...


def diag(M: list[list[float]]):
    """Dada una matriz regresa una matriz diagonalizada"""
    ...


def main():
    mat = [[1.0, 2.0, -1.0], [1.0, 0.0, 1.0], [0.0, -1.0, -1.0]]
    gaussian_elimination(mat)


if __name__ == "__main__":
    main()
