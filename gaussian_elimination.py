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

    for i in range(n):
        # Encuentra el indice del pivote maximo
        pivotes = []
        for pivot in range(i, n):
            pivotes.append(M[pivot][i])
        max_pivot = max(pivotes, key=abs)
        max_index = pivotes.index(max_pivot) + i
        if max_pivot == 0:
            print("Ay...")
            return None

        # Intercambia la fila con el pivote maximo con la actual
        M = rowswap(M, i, max_index)

        # Elimina los valores debajo de la diagonal
        for j in range(i + 1, n):
            aji = M[j][i]
            pivot = M[i][i]
            M[j] = rowsum(M, j, i, -aji / pivot)

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
    A_np = np.random.random((3, 3))
    print(A_np)
    print()
    A = A_np.tolist()
    A_diag = diag(A)
    print(np.array(A_diag))
    print()

    B_np = np.random.random((4, 4))
    print(B_np)
    print()
    B = B_np.tolist()
    B_diag = diag(B)
    print(np.array(B_diag))


if __name__ == "__main__":
    main()
