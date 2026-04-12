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