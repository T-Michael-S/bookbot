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

def new_dicts(dictionary):
    new_list =[]
    for character in dictionary:
        new_dict = {"char": character, "num": dictionary[character]}
        new_list.append(new_dict)

    def sort_dict(single_dict):
        return single_dict["num"]
        
    new_list.sort(reverse=True, key=sort_dict)

    return new_list