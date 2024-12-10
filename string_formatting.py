# This program prints the numbers from 1 to a given number in decimal, octal, hexadecimal, and binary formats.

def print_formatted(number):
    # Calculate the width of the binary representation of the largest number
    width = len(bin(number)[2:])  # Converts to binary and removes 0b (why?) Idk

    # Also Each column is aligned to match the width of the largest binary number in the range

    # Iterate through numbers from 1 to the number the user gives
    for i in range(1, number + 1):
        print(
            str(i).rjust(width),         # Decimal column
            oct(i)[2:].rjust(width),     # Octal colum
            hex(i)[2:].upper().rjust(width),  # Hexadecimal column
            bin(i)[2:].rjust(width)      # Binary column
        )

def main():
    n = int(input("Enter a number: "))
    print_formatted(n)

if __name__ == '__main__':
    main()
