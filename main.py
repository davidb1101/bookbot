import sys

from stats import word_count
from stats import character_count
from stats import sorted_character_count


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def print_report(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for item in sorted_character_count(character_count(book_text)):
        if not item['name'].isalpha():
            continue
        print(f"{item['name']}: {item['num']}")

    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_report(sys.argv[1])



main()

