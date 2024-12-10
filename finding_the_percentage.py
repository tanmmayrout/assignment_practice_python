# This code calculates the average marks for a student based on user input.

def main():

    n = int(input("Enter the number of students: "))  # To accept the number of students.
    student_marks = {}  # Dictionary to store student names and scores

    for _ in range(n): # For loop to make sure the entries are within the range and accept the needed values
        print("Enter student name followed by their marks (space-separated):")
        name, *line = input().split() #Accept the name and then the number of marks  that come after
        scores = list(map(float, line))  # Convert marks to a list of floats.
        student_marks[name] = scores  # Stores the scores in student_marks

    query_name = input("Enter the name of the student to calculate the average marks: ")

    # Calculate and print the average marks
    if query_name in student_marks:  # Ensure the queried student exists in the dictionary
        marks = student_marks[query_name]
        mean_marks = sum(marks) / len(marks)  # Average
        print(f"Average marks for {query_name}: {mean_marks:.2f}")  # Output with 2 float places
    else:
        print("Student not found!")  #Case where the student does not exist.

if __name__ == '__main__':
    main() #Call main
