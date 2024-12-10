import numpy  # Importing the numpy library for numerical operations

from numpy import linalg   # Importing the linalg module from numpy for matrix operations
n = int(input())  # Taking the input for the size of the square matrix n is the number of rows/columns in the square matrix (Only Square matrix )
a = numpy.array([list(map(float, input().split())) for i in range(n)])
# Calculating the determinant of the matrix using numpy linear algebra module
b = round(numpy.linalg.det(a), 2)  # The determinant is calculated and rounded to 2 decimal places
# b det value
print(b)
