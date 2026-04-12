# Práctica 7  Diagonalización Por Método De Gauss, Factorización LU y Factorización QR


¡Adentrémonos en el increíble mundo del álgebra lineal numérica! OwO

## Integrantes

- Domínguez León José Miguel 
- Lazcano Flores Valeria
- Sánchez García Rafael 

## Uso e instalación
Lo que se necesita instalar para ejecutar el código es:
- `numpy`: el cual se importa como np; instalamos 
La manera y el orden en que se debe de ejecutar los archivos .py es:
- `gaussian_elimination.py`: el codigo implementa eliminación gaussiana con pivoteo parcial para llevar una matriz a su forma triangular superior, y posteriormente aplica operaciones tipo Gauss-Jordan para convertirla en una matriz diagonal mediante eliminación hacia atrás.
- `gram_schmidt.py`: en este archivo tenemos funciones como
1. dot: producto punto de dos vectores.
2. transponse: calcula la transpuesta de una matriz, i.e convierte filas en columnas.
3. matmul: multiplicación de matrices.
4. matvec: multiplicación matriz por vector.
5. norm: calcula la norma euclidiana.
6. proj: proyección de un vector.
7. normalize: convierte un vector en vector unitario.
8. gram_schimdt: convierte un conjunto de vectores l.i en vectores ortonormales.
- `lu.py`: dada una matriz M regresa su factorización LU.
- `qr.py`: realiza la factorización QR de una matriz.
- `main.py`: contiene el código para llamar e imprimir a las funciones para resolver los ejercicios 1, 2 y 3.

## Introducción
En esta práctica estamos implementando métodos de álgebra lineal, los cuales permiten transformar matrices y entender su estructura.
En particular, trabajamos con:
1. Eliminación gaussiana: simplifica matrices mediante operaciones por filas.
2. Factorización LU: descompone una matriz en producto de matrices más simples.
3. Factorización QR: contruimos bases ortogonales y descomponemos matrices.
Estos métodos nos permiten resolver sistemas de ecuaciones, y se pueden utilizar en modelación u optimización.


## Ejercicio 1
Diagonalización por método de Gauss
Implementamos el método de eliminación gaussiana para transformar una matriz en forma más simple.
El proceso tiene dos estapas:
1. Matriz triangular superior 

\[
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i 
\end{bmatrix}
\righttarrow
\begin{bmatrix}
a & b & c \\
0 & e' & f' \\
0 & 0 & i' 
\end{bmatrix}
\]


Esto se realiza con:
- `rowswap`: intercambiar filas
- `rowsum`: sumar múltiplos de filas

2. Matriz diagonal
Posteriormente eliminamos los valores arriba de la diagonal
\[
\begin{bmatrix}
a & b & c \\
0 & d & e \\
0 & 0 & f 
\end{bmatrix}
\righttarrow
\begin{bmatrix}
a & 0 & 0 \\
0 & d & 0 \\
0 & 0 & f
\end{bmatrix}
\]

Obtenemos una matriz diagonal equivalente a la original.

## Ejercicio 2

## Ejercicio 3

