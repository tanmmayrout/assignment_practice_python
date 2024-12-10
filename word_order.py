from collections import Counter # Import Counter from the collections module

result = Counter(input() for _ in range(int(input()))) # Counter to count input strings

print(len(result.keys())) #Number of unique keys
print(*result.values()) #Counts of each unique input