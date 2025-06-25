from stats import count_words
from stats import count_letters
from stats import new_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    write = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(write)} total words")
    print("--------- Character Count -------")
    filter = new_dicts(count_letters(write))
    for dic in filter:
        if dic["char"].isalpha():
            print(f"{dic['char']}: {dic['num']}")
    print("============= END ===============")
    
main()