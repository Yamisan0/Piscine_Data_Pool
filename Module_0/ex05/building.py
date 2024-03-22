import sys
import string


def check_input():
    """
    Checks input and number of arguments passed in the command line.
    If all requirements are filled, count_and_display() function is called
    """
    assert len(sys.argv) <= 2, "more than one argument provided"
    try:
        if (len(sys.argv) == 1):
            text = input('What is the text to count?\n')
            text = text + '\n'
        else:
            text = sys.argv[1]
    except EOFError:
        print("\nEOF detected. Exiting the program.")
        exit()
    count_and_display(text)


def count_and_display(text: str):
    """
    Counts all types of characters in a string and displays it in a certain order.
    iterates over each character thanks to a generator expression that applies directly
    in the Dictionnary.
    """

    counts = {
        "digits": sum(1 for i in text if i.isdigit()),
        "upper": sum(1 for i in text if i.isupper()),
        "lower": sum(1 for i in text if i.islower()),
        "space": sum(1 for i in text if i.isspace()),
        "punctuation": sum(1 for i in text if i in string.punctuation),
    }

    print(f'The text contains {len(text)} characters:')
    print(f'{counts["upper"]} upper letters')
    print(f'{counts["lower"]} lower letters')
    print(f'{counts["punctuation"]} punctuation marks')
    print(f'{counts["space"]} spaces')
    print(f'{counts["digits"]} digits')
    



def main():
    try:
        check_input()
    except AssertionError as error:
        print('AssertionError :', error)
    

if __name__ == '__main__':
    main()