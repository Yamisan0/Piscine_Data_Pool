import sys
from string import punctuation
from ft_filter import ft_filter

def check_args(argv: list[str]):
    if len(argv) != 3 or not argv[1].isprintable() or any(char in argv[1] for char in punctuation) or not argv[2].isdigit() :
        raise AssertionError("the arguments are bad")
    
    


def main():
    try:
        check_args(sys.argv)
        words = sys.argv[1].split()
        limit = int(sys.argv[2])
        result = ft_filter(words, lambda element : len(element) > limit)
        print(result)
    except AssertionError as error:
        print("AssertionError:", error)
    except:
        print("An Unexpected error has occured")

if __name__ == "__main__":
    main()
        