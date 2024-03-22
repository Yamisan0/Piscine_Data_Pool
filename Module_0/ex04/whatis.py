from sys import argv


def is_odd_or_even(number: int):
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    if len(argv) == 1:
        exit()
    assert len(argv) == 2, "more than one argument is provided"

    try:
        number = int(argv[1])
    except ValueError:
        # If conversion fails, raise an AssertionError
        raise AssertionError("argument is not an integer")
    is_odd_or_even(number)


if __name__ == '__main__':
    try:
        main()
    except AssertionError as error:
        print(AssertionError.__name__, ':', error)
