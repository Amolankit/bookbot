# main.py

import sys
from stats import get_num_words, get_char_count, sort_character_counts

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    try:
        book_text = get_book_text(path)
    except FileNotFoundError:
        print(f"Error: Could not find the file '{path}'.")
        sys.exit(1)

    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = get_char_count(book_text)
    sorted_counts = sort_character_counts(char_counts)

    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()