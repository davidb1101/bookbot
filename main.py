from stats import word_count


def get_book_text(filepath):
    with open("books/frankenstein.txt") as f:
        text = f.read()
    return text



def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document.")


main()

