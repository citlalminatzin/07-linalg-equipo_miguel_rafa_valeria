# Práctica 7: Diagonalización por Método de Gauss, Factorización LU y Factorización QR

## Integrantes

- Domínguez León José Miguel  
- Lazcano Flores Valeria  
- Sánchez García Rafael  

---

## Introducción

En esta práctica implementamos métodos fundamentales del álgebra lineal que permiten transformar matrices y entender su estructura.

Trabajamos con:

### 1. Eliminación Gaussiana

Algoritmo iterativo que simplifica una matriz mediante operaciones elementales por filas:
- Intercambio de filas  
- Suma de múltiplos de filas  
- Escalamiento de filas  

Se obtiene una **matriz triangular superior**, y mediante eliminación hacia atrás (Gauss-Jordan), se puede llegar a una matriz diagonal o identidad.

Para estabilidad numérica se usa **pivoteo parcial**, que consiste en colocar el mayor elemento (en valor absoluto) como pivote.

---

### 2. Factorización LU

Descompone una matriz cuadrada en:

$$
A = LU
$$

donde:
- $L$: triangular inferior con unos en la diagonal  
- $U$: triangular superior  

Con pivoteo:

$$
PA = LU
$$

donde $P$ es una matriz de permutación.

---

### 3. Factorización QR

Descompone:

$$
A = QR
$$

donde:
- $Q$: matriz ortogonal  
- $R$: triangular superior  

Se obtiene mediante el proceso de **Gram-Schmidt**.

---

## Uso e instalación

Se requiere:

- `numpy`

Archivos:

- `gaussian_elimination.py`: eliminación gaussiana con pivoteo parcial  
- `gram_schmidt.py`: implementación de Gram-Schmidt  
- `lu.py`: factorización LU  
- `qr.py`: factorización QR  
- `main.py`: ejecución de los ejercicios  

---

## Ejercicio 1: Diagonalización por método de Gauss

### Matriz triangular superior

$$
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
\rightarrow
\begin{bmatrix}
a & b & c \\
0 & e' & f' \\
0 & 0 & i'
\end{bmatrix}
$$

Operaciones:
- `rowswap`
- `rowsum`

---

### Matriz diagonal

$$
\begin{bmatrix}
a & b & c \\
0 & d & e \\
0 & 0 & f
\end{bmatrix}
\rightarrow
\begin{bmatrix}
a & 0 & 0 \\
0 & d & 0 \\
0 & 0 & f
\end{bmatrix}
$$

---

## Ejercicio 2: Factorización LU

### Sin pivoteo — $A = LU$

$$
A =
\begin{bmatrix}
2 & 1 & 1 \\
4 & 3 & 3 \\
8 & 7 & 9
\end{bmatrix}
$$

$$
L =
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
4 & 3 & 1
\end{bmatrix}
,\quad
U =
\begin{bmatrix}
2 & 1 & 1 \\
0 & 1 & 1 \\
0 & 0 & 2
\end{bmatrix}
$$

$$
L \cdot U = A
$$

---

### Con pivoteo parcial — $PA = LU$

$$
P =
\begin{bmatrix}
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0
\end{bmatrix}
$$

---

## Ejercicio 3: Factorización QR

### Proceso de Gram-Schmidt

$$
u_k = v_k - \sum_{j=1}^{k-1} \frac{\langle v_k, u_j \rangle}{\|u_j\|^2} u_j
$$

$$
e_k = \frac{u_k}{\|u_k\|}
$$

---

## Resultados

### Matriz $2 \times 2$

$$
A =
\begin{bmatrix}
0.04 & 0.28 \\
0.29 & 0.98
\end{bmatrix}
$$

$$
Q =
\begin{bmatrix}
0.12 & 0.99 \\
0.99 & -0.12
\end{bmatrix}
,\quad
R =
\begin{bmatrix}
0.29 & 1.01 \\
0 & 0.16
\end{bmatrix}
$$

$$
Q \cdot R =
\begin{bmatrix}
0.04 & 0.28 \\
0.29 & 0.98
\end{bmatrix}
= A
$$

---

### Matriz $3 \times 3$

$$
A =
\begin{bmatrix}
0.79 & 0.57 & 0.52 \\
0.26 & 0.17 & 0.91 \\
0.23 & 0.57 & 0.38
\end{bmatrix}
$$

$$
Q =
\begin{bmatrix}
0.91 & -0.23 & -0.33 \\
0.30 & -0.14 & 0.94 \\
0.27 & 0.96 & 0.05
\end{bmatrix}
,\quad
R =
\begin{bmatrix}
0.86 & 0.73 & 0.85 \\
0 & 0.39 & 0.12 \\
0 & 0 & 0.71
\end{bmatrix}
$$

$$
Q \cdot R =
\begin{bmatrix}
0.79 & 0.57 & 0.52 \\
0.26 & 0.17 & 0.91 \\
0.23 & 0.57 & 0.38
\end{bmatrix}
= A
$$

---

## Conclusiones

Esta práctica permitió implementar algoritmos fundamentales del álgebra lineal numérica.

- La **eliminación gaussiana con pivoteo parcial** mejora la estabilidad numérica  
- La **factorización LU** reutiliza los multiplicadores y optimiza la resolución de sistemas  
- La **factorización QR** construye bases ortonormales y facilita cálculos como eigenvalores  

Estos métodos son clave en simulación, machine learning y cómputo científico.