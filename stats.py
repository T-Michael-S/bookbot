def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_letters(text):
    words = text.lower()
    dict = {}
    for letter in words:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict