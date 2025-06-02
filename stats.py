def get_book_length(file_contents):
    book_length = file_contents.split()
    return len(book_length)

def char_number(file_contents):
    file_letter_count = {"a":0, "b":0, "c":0, "d":0, "e":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    alphabet = {"a", "b", "c", "d", "e", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    for i in file_contents.lower():
        if i in alphabet:
            file_letter_count[i] = file_letter_count[i] + 1

    return file_letter_count

def sorted_dict(dict):
    dict_list = []
    alphabet = {"a", "b", "c", "d", "e", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    
    for i in alphabet:
        dict_list.append({"char":i, "num":dict[i]})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["num"]
    