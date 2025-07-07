import sys
from stats import numb_of_character
from stats import get_num_words

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_num_words(sys.argv[1])
    print("--------- Character Count -------")
    numb_of_character(sys.argv[1])

main()
