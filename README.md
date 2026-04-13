# Práctica 7  Diagonalización Por Método De Gauss, Factorización LU y Factorización QR

## Integrantes

- Domínguez León José Miguel 
- Lazcano Flores Valeria
- Sánchez García Rafael 

## Introducción
En esta práctica estamos implementando métodos de álgebra lineal, los cuales permiten transformar matrices y entender su estructura.
En particular, trabajamos con:
1. Eliminación gaussiana: 
un algoritmo iterativo que simplifica una matriz mediante operaciones elementales por filas: sumar múltiplos de una fila a otra, intercambiar filas y escalar filas. A través de este proceso se lleva la matriz a una forma triangular superior, y aplicando el mismo proceso en sentido inverso (eliminación hacia atrás o Gauss-Jordan) se puede llegar a una forma diagonal o incluso a la identidad. Para garantizar estabilidad numérica se incorpora el pivoteo parcial, que consiste en intercambiar filas para colocar el elemento de mayor valor absoluto en la posición del pivote antes de cada paso de eliminación.

2. Factorización LU:
Que descompone una matriz cuadrada $A$ en el producto de una matriz triangular inferior $L$ y una triangular superior $U$, de forma que $A = LU$. Esta descomposición es especialmente útil para resolver múltiples sistemas de ecuaciones con la misma matriz de coeficientes, ya que la factorización se calcula una sola vez. Cuando la matriz requiere intercambio de filas para garantizar estabilidad, se incorpora una matriz de permutación $P$ y la descomposición toma la forma $PA = LU$.

3. Factorización QR: 
Descompone una matriz $A$ en el producto de una matriz ortogonal $Q$ (cuyas columnas forman una base ortonormal) y una matriz triangular superior $R$, de forma que $A = QR$. Esta factorización se construye mediante el proceso de Gram-Schmidt aplicado a las columnas de $A$. Sus aplicaciones incluyen el cálculo de valores propios (eigenvalores), la solución de sistemas de ecuaciones lineales y la interpolación polinomial.
Estos tres métodos constituyen la base de gran parte del álgebra lineal computacional moderna y tienen aplicaciones directas en simulación física, aprendizaje automático, criptografía y graficación por computadora, entre otros campos.


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
.


## Ejercicio 1
Diagonalización por método de Gauss
Implementamos el método de eliminación gaussiana para transformar una matriz en forma más simple.
El proceso tiene dos estapas:
1. Matriz triangular superior 

[a b c
d e f
g h i]
→
[a b c
0 e' f'
0 0 i']

Esto se realiza con:
- `rowswap`: intercambiar filas
- `rowsum`: sumar múltiplos de filas

2. Matriz diagonal
Posteriormente eliminamos los valores arriba de la diagonal
[a b c
0 d e
0 0 f]
→
[a 0 0
0 d 0
0 0 f]

Obtenemos una matriz diagonal equivalente a la original.

## Ejercicio 2: Factorización LU

Se implementó la factorización LU en dos modalidades: sin pivoteo y con pivoteo parcial.

### Sin pivoteo — $A = LU$

Para matrices donde no se requiere intercambio de filas, el algoritmo construye simultáneamente $L$ y $U$: la matriz $U$ se obtiene escalando la matriz original mediante eliminación gaussiana, y los factores usados en cada paso de eliminación ($c = a_{ji}/a_{ii}$) se colocan directamente en las posiciones correspondientes de $L$.

Dado que $L$ comienza como la identidad y se va llenando con los multiplicadores, se garantiza que $L$ es triangular inferior con unos en la diagonal.

**Verificación** con la matriz:

$$A = \begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix}$$

Se obtiene:

$$L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{bmatrix}, \quad U = \begin{bmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{bmatrix}$$

Y se verifica que $L \cdot U = A$ con error máximo de $0.0$.

### Con pivoteo parcial — $PA = LU$

Cuando la matriz requiere intercambio de filas para garantizar estabilidad numérica, la factorización toma la forma $PA = LU$, donde $P$ es una **matriz de permutación** que registra los intercambios realizados. Esto permite factorizar matrices que de otro modo generarían divisiones entre cero o resultados numéricamente inestables.

Para la matriz $A$ del ejercicio 1:

$$P = \begin{bmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{bmatrix}$$

La matriz $P$ indica que la fila 1 pasó al lugar de la fila 4, la fila 3 al lugar de la 2, y así sucesivamente. La $U$ resultante coincide con la triangular superior obtenida en el Ejercicio 1.

---
## Ejercicio 3: Factorización QR

Se implementó la factorización QR mediante el proceso de Gram-Schmidt y se verificó que $Q \cdot R = A$ en dos matrices aleatorias generadas con `np.random.random`.

### Proceso de Gram-Schmidt

Dadas las columnas $v_1, \dots, v_n$ de la matriz $A$, se construye una base ortonormal $e_1, \dots, e_n$ mediante:

$$u_k = v_k - \sum_{j=1}^{k-1} \frac{\langle v_k, u_j \rangle}{\|u_j\|^2} u_j, \qquad e_k = \frac{u_k}{\|u_k\|}$$

Las columnas $e_1, \dots, e_n$ forman la matriz $Q$, y $R = Q^T A$ resulta triangular superior.

### Resultados

**Matriz $2 \times 2$:**

$$A = \begin{bmatrix} 0.04 & 0.28 \\ 0.29 & 0.98 \end{bmatrix}$$

$$Q = \begin{bmatrix} 0.12 & 0.99 \\ 0.99 & -0.12 \end{bmatrix}, \quad R = \begin{bmatrix} 0.29 & 1.01 \\ 0 & 0.16 \end{bmatrix}$$

$$Q \cdot R = \begin{bmatrix} 0.04 & 0.28 \\ 0.29 & 0.98 \end{bmatrix} = A \checkmark$$

**Matriz $3 \times 3$:**

$$A = \begin{bmatrix} 0.79 & 0.57 & 0.52 \\ 0.26 & 0.17 & 0.91 \\ 0.23 & 0.57 & 0.38 \end{bmatrix}$$

$$Q = \begin{bmatrix} 0.91 & -0.23 & -0.33 \\ 0.30 & -0.14 & 0.94 \\ 0.27 & 0.96 & 0.05 \end{bmatrix}, \quad R = \begin{bmatrix} 0.86 & 0.73 & 0.85 \\ 0 & 0.39 & 0.12 \\ 0 & 0 & 0.71 \end{bmatrix}$$

$$Q \cdot R = \begin{bmatrix} 0.79 & 0.57 & 0.52 \\ 0.26 & 0.17 & 0.91 \\ 0.23 & 0.57 & 0.38 \end{bmatrix} = A \checkmark$$

En ambos casos se observa que $Q$ tiene columnas ortonormales y $R$ es triangular superior con valores positivos en la diagonal, cumpliendo con las propiedades teóricas de la factorización QR.

---

## Conclusiones

Esta práctica nos permitió implementar desde cero tres de los algoritmos más importantes del álgebra lineal numérica, lo que nos dio una comprensión profunda de su funcionamiento interno en lugar de simplemente usarlos como cajas negras.

En el caso de la **eliminación gaussiana**, la incorporación del pivoteo parcial resultó fundamental: sin él, la presencia de un cero en la diagonal detiene el algoritmo por completo, mientras que con él se garantiza tanto la continuidad del proceso como la estabilidad numérica del resultado.

La **factorización LU** demostró ser una extensión natural de la eliminación gaussiana. Los multiplicadores usados durante la eliminación no se descartan sino que se reutilizan para construir $L$, lo que hace que la factorización sea muy eficiente. La variante con pivoteo parcial ($PA = LU$) amplía el alcance del método a matrices que de otra forma generarían divisiones entre cero.

La **factorización QR** vía Gram-Schmidt mostró cómo construir bases ortonormales de manera sistemática a partir de cualquier conjunto de vectores linealmente independientes. La verificación $QR = A$ en ambas matrices aleatorias confirmó la correctitud de la implementación. Una ventaja clave de esta factorización es que $Q$ es ortogonal, lo que convierte operaciones costosas (como calcular $Q^{-1}$) en operaciones triviales (calcular $Q^T$), con aplicaciones directas en la solución de sistemas de ecuaciones y el cálculo de eigenvalores.




