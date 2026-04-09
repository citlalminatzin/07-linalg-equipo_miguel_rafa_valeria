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
            return None
        for j in range(i + 1, n):
            aij = M[j][i]
            M[j] = rowsum(M, j, i, -aij)
    return M


def triang_sup_to_diag(M: list[list[float]]):
    """
    Dada una matriz M traingular superior
    regresa una matriz diagonal
    """
    n = len(M)

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            aij = M[-j][-i]
            M[-j] = rowsum(M, -j, -i, -aij)
    return M


def diag(M: list[list[float]]):
    """Dada una matriz regresa una matriz diagonalizada"""
    gauss = gaussian_elimination(M)
    if gauss is not None:
        return triang_sup_to_diag(gauss)
    else:
        print("Algun pivote es cero...")
        return None


def main():
    mnp1 = np.random.randint(1, 10, size=(3, 3))
    print(mnp1)
    matriz1 = mnp1.tolist()
    diagonal1 = diag(matriz1)
    print(np.array(diagonal1))
    print()

    mnp2 = np.random.randint(1, 10, size=(4, 4))
    print(mnp2)
    matriz2 = mnp2.tolist()
    diagonal2 = diag(matriz2)
    print(np.array(diagonal2))

    # a veces regresa cosas mal por flotantes supongo.


if __name__ == "__main__":
    main()
