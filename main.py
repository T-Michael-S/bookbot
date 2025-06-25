from stats import count_words
from stats import count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    write = get_book_text("books/frankenstein.txt")
    print(f"{count_words(write)} words found in the document")
    print(count_letters(write))
    print()
    
main()