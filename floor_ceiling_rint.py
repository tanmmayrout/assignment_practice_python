import numpy as np  # Importing the NumPy library for numerical computing


np.set_printoptions(legacy='1.13') # Setting the NumPy print options to follow the behavior of NumPy version 1.13
# Saw on the internet to do this step

actions = ["floor", "ceil", "rint"] #Numpy functions


a = list(map(float, input().split())) #Convert to float

for action in actions:
    result = getattr(np, action)(a) # Using getattr to dynamically call the NumPy function based on the action name

    print(result)
