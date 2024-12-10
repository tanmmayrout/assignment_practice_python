
T = int(input())  # Input the number of test cases


for _ in range(T):
    n = int(input())  # Input the number of cubes in the current test case
    no_cube = list(map(int, input().split()))

    stackable = True  # Assume cubes can be stacked

    # Check if there is a peak in the middle of the list
    for i in range(1, n - 1):
        if no_cube[i - 1] < no_cube[i] > no_cube[i + 1]:  # Peak condition
            stackable = False  # non-stackable
            break  # Exit once a peak is found

    if stackable:
        print("Yes")  # Cubes can be stacked
    else:
        print("No")  # Cubes cannot be stacked
