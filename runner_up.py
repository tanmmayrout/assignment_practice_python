# This program calculates the runner-up score from a list of numbers.

def main():
    n = int(input("Enter the number of scores: "))  # Number of scores to process

    print("Enter the scores separated by spaces:")
    arr = map(int, input().split())  # Convert input into a map of integers and splits the entries

    sorted_scores = sorted(set(arr))  # set() removes duplicates, sorted() arranges in ascending order

    if len(sorted_scores) < 2:  # Check if there are at least two unique scores
        print("Not enough unique scores to determine a runner-up!")
    else:
        print(f"The runner-up score is: {sorted_scores[-2]}")  # Access the second-to-last element


if __name__ == '__main__':
    main()
