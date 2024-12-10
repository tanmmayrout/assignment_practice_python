import numpy  # Importing the numpy library for numerical operations

print("Enter the array")
n, m = map(int, input().split())  # Taking the input for the dimensions of the array n and m
arr = [list(map(int, input().split()[:m])) for _ in range(n)]  # Each row is converted to a list of integers array


arr = numpy.array(arr)  #Converting the list into a NumPy array for easier numerical computations
print(numpy.mean(arr, axis=1))  # Calculating the mean of each row (axis=1 means we calculate the mean along rows)
print(numpy.var(arr, axis=0))  # Calculating the variance of each column (axis=0 means we calculate the variance along columns)
print(numpy.around(numpy.std(arr, axis=None), 11))  # Calculating the standard deviation of the entire array (axis=None means we consider all values in the array)
