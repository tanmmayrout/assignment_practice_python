import numpy as np  # Importing the numpy library as np


x, y = map(int, input().split()) # Taking input for dimensions

# Taking input for the matrix
data = [list(map(int, input().split())) for _ in range(x)]  # Reading x rows of y integers each

data = np.array(data) # Converting the list of lists into a NumPy array

result = np.min(data, axis=1) # Calculating the minimum value in each row

print(np.max(result))  # Printing the maximum value of the row-wise minimums
