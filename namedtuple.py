# Import the following for lightweight data structure
from collections import namedtuple

import statistics

if __name__ == '__main__':
    total_students = int(input()) #total number of students as an integer

    # Define a 'namedtuple' called 'studnet' to add fields
    student = namedtuple('student', list(map(str, input().split())))

    # Calculate and print the mean of the 'MARKS' for all students
    print(f'{statistics.mean([int(student(*(input().split())).MARKS) for _ in range(total_students)]):.2f}')
