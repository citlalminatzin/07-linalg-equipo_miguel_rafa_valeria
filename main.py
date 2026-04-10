#!/usr/bin/env python

from gaussian_elimination import diag
from lu import lu

import numpy as np


def main():
    arr1 = np.random.random((2, 2))
    arr2 = np.random.random((3, 3))
    arrays = [arr1, arr2]

    print("===Ejericio1===")
    for array in arrays:
        with np.printoptions(precision=2):
            print("Matriz inicial")
            print(array, "\n")
            print("Diagonal")
            diagonal = diag(array)
            print(np.array(diagonal), "\n")

    print("===Ejercicio2===")
    for array in arrays:
        with np.printoptions(precision=2):
            print("Matriz inicial")
            print(array, "\n")
            L, U = lu(array)
            print("Matriz diagonal superior")
            print(np.array(U), "\n")
            print("Matriz inferior")
            print(np.array(L), "\n")
            print("Producto LU")
            print(np.array(np.dot(L, U)), "\n")


if __name__ == "__main__":
    main()
