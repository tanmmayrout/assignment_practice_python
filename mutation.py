# This program modifies a string by replacing a character at a specified position.

def mutate_string(string, position, character):
    # string is the input string.
    # position is the index to replace the character.
    # character is the new character to insert.

    # Return the modified string
    return string[:position] + character + string[position + 1:]  #Slices the string from the start up to the position

def main():
    original_string = input("Enter the original string: ")
    position = int(input("Enter the position to modify (0-based index): "))
    new_character = input("Enter the new character to insert: ")
    modified_string = mutate_string(original_string, position, new_character)
    print(f"Modified string: {modified_string}")


if __name__ == '__main__':
    main()
