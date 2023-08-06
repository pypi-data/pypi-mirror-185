# Matmul 0.0.2

Matmul is a Python package that can be used for matrix multiplication involving 2 matrices.
This version (matmul 0.0.2) has some added improvisation to the README.md file of the package. 

## Installation

To install Matmul, run the following command:

pip install matmul


## Usage
There are 2 modules in the package which can be imported after installation and called according to use:

1. matinput.py : takes input matrices from the user #matinput(rows,columns)
2. matmul.py : uses input matrices and performs matrix multiplication resulting in output #matmul(matrix1,matrix2)

The test.py (with the following code) can be used as a whole by itself to test the package :

#for example
from matmul import matinput as i
from matmul import matmul as m
a = int(input('enter number of rows in mat1 '))
b = int(input('enter number of columns in mat1 '))
mat1 = i.getInputMatrix(a, b)
c = int(input('enter number of rows in mat2 '))
d = int(input('enter number of columns in mat2 '))
mat2 = i.getInputMatrix(c, d)
result = m.matrixMultiplication(mat1, mat2)

Otherwise, 
Terminal (cmd) can be used -

>>> from matmul import matinput as i
>>> from matmul import matmul as m
>>> mat1 = i.getInputMatrix(1,2)
enter numbers row wise
enter number 1
enter number 2
1
2
>>> mat2 = i.getInputMatrix(2,3)
enter numbers row wise
enter number 1
enter number 2
enter number 3
enter number 4
enter number 5
enter number 6
1
2
3
4
5
6
>>> result = m.matrixMultiplication(mat1,mat2)
[[9, 12, 15]]

## Known Issues
My Package does not support Python 3.7 or earlier.

## Contributor
Dhruv Gupta (author)

## License
My Package is released under the MIT License. See the LICENSE file for more information.