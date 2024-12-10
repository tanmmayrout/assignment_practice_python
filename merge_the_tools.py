# This program splits a string into parts of a certain size and removes duplicate characters in each part

def merge_the_tools(string, k):
    s = string.upper()  # Converts the input string to uppercase
    for i in range(0, len(s), k):  # Iterate through size `i` by `k` each time
        segment = s[i: i + k]  # Extracts a substring of size `k`
        unique_segment = ""  # Empty string to store unique characters

        for char in segment:  # Loop through each character in the segment
            if char not in unique_segment:  # Add only if the character is not in unique statement
                unique_segment += char

        print(unique_segment) #Prints teh unique character string


def main():
    input_string = input("Enter the string: ")
    k = int(input("Enter the size of each segment (k): ")) # Accepts the size of each segment
    merge_the_tools(input_string, k)


if __name__ == '__main__':
    main()
