# Práctica 7: Diagonalización por Método de Gauss, Factorización LU y Factorización QR

## Integrantes

- Domínguez León José Miguel  
- Lazcano Flores Valeria  
- Sánchez García Rafael  


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
Se implementó la diagonalización de una matriz cuadrada en dos etapas.

### Etapa 1 — Triangularización (eliminación hacia adelante)

Partiendo de una matriz $A$ de $n \times n$, se aplica eliminación gaussiana con **pivoteo parcial**: en cada columna $i$ se busca el elemento de mayor valor absoluto entre las filas $i, i+1, \dots, n$ y se intercambia con la fila $i$. Esto evita divisiones entre valores cercanos a cero y mejora la estabilidad numérica. Luego se eliminan todos los elementos por debajo del pivote sumando múltiplos apropiados de la fila pivote.

Aplicado sobre la matriz del problema:

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

Esto se realiza con las operaciones:
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

Para matrices donde no se requiere intercambio de filas, el algoritmo construye simultáneamente $L$ y $U$: la matriz $U$ se obtiene escalando la matriz original mediante eliminación gaussiana, y los multiplicadores usados en cada paso ($c = a_{ji}/a_{ii}$) se colocan en las posiciones correspondientes de $L$. Como $L$ comienza como la identidad y se llena con los multiplicadores, resulta triangular inferior con unos en la diagonal.

**Resultado** con una matriz $3 \times 3$:

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
**Verificación:**
$$
L \cdot U = A
$$

### Con pivoteo parcial — $PA = LU$
Cuando la matriz requiere intercambio de filas para garantizar estabilidad numérica, se incorpora una matriz de permutación $P$ que registra los intercambios. La factorización toma la forma $PA = LU$, donde $P \cdot A$ es la matriz original con sus filas reordenadas.

Aplicado sobre la misma matriz del Ejercicio 1, la matriz de permutación obtenida fue:

$$
P =
\begin{bmatrix}
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0
\end{bmatrix}
$$


Indicando que las filas fueron reordenadas en orden inverso, y la $U$ resultante coincide con la triangular superior obtenida en el Ejercicio  1
---

## Ejercicio 3: Factorización QR

Se implementó la factorización QR mediante el proceso de Gram-Schmidt y se verificó que $Q \cdot R = A$ en dos matrices aleatorias generadas con `np.random.random`.
### Proceso de Gram-Schmidt

Dadas las columnas $v_1, \dots, v_n$ de la matriz $A$, se construye una base ortonormal $e_1, \dots, e_n$ mediante:


$$
u_k = v_k - \sum_{j=1}^{k-1} \frac{\langle v_k, u_j \rangle}{\|u_j\|^2} u_j
$$


$$
e_k = \frac{u_k}{\|u_k\|}
$$


Las columnas $e_1, \dots, e_n$ forman la matriz $Q$, y $R = Q^T A$ resulta triangular superior.

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

En ambos casos se observa que $Q$ tiene columnas ortonormales y $R$ es triangular superior con valores positivos en la diagonal, cumpliendo con las propiedades teóricas de la factorización QR.


---

## Conclusiones


Esta práctica nos permitió implementar desde cero tres de los algoritmos más importantes del álgebra lineal numérica, lo que nos dio una comprensión profunda de su funcionamiento interno en lugar de simplemente usarlos como cajas negras.

En el caso de la **eliminación gaussiana**, la incorporación del pivoteo parcial resultó fundamental: sin él, la presencia de un cero en la diagonal detiene el algoritmo por completo, mientras que con él se garantiza tanto la continuidad del proceso como la estabilidad numérica del resultado.

La **factorización LU** demostró ser una extensión natural de la eliminación gaussiana. Los multiplicadores usados durante la eliminación no se descartan sino que se reutilizan para construir $L$, lo que hace que la factorización sea muy eficiente. La variante con pivoteo parcial ($PA = LU$) amplía el alcance del método a matrices que de otra forma generarían divisiones entre cero.

La **factorización QR** vía Gram-Schmidt mostró cómo construir bases ortonormales de manera sistemática a partir de cualquier conjunto de vectores linealmente independientes. La verificación $QR = A$ en ambas matrices aleatorias confirmó la correctitud de la implementación. Una ventaja clave de esta factorización es que $Q$ es ortogonal, lo que convierte operaciones costosas (como calcular $Q^{-1}$) en operaciones triviales (calcular $Q^T$), con aplicaciones directas en la solución de sistemas de ecuaciones y el cálculo de eigenvalores.