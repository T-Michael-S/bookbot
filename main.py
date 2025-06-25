def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words


def main():
    write = get_book_text("books/frankenstein.txt")
    number_of_words = count_words(write)
    print(f"{number_of_words} words found in the document")
    
main()