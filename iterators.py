from itertools import combinations  # Importing combinations function from itertools module

n = int(input())  # Read the number of elements in the list first input: the number of elements in the list


elements = input().split()  # Read the elements of the list and then read the size of the combinations The second input: space-separated elements for the list
r = int(input())  # size of each combination
result = list(combinations(elements, r)) # Generate all combinations of the given list with the size 'r'

# Initialize a counter ]
c = 0

for i in result: # Iterate over each combination and check if it contains the element
    if 'a' in i:
        c += 1

print(c / len(result))
