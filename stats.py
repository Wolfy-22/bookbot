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
    dict_list = [{"char":"a", "num":dict["a"]}, 
                 {"char":"b", "num":dict["b"]}, 
                 {"char":"c", "num":dict["c"]}, 
                 {"char":"d", "num":dict["d"]}, 
                 {"char":"e", "num":dict["e"]},  
                 {"char":"g", "num":dict["g"]}, 
                 {"char":"h", "num":dict["h"]}, 
                 {"char":"i", "num":dict["i"]}, 
                 {"char":"j", "num":dict["j"]}, 
                 {"char":"k", "num":dict["k"]}, 
                 {"char":"l", "num":dict["l"]}, 
                 {"char":"m", "num":dict["m"]}, 
                 {"char":"n", "num":dict["n"]}, 
                 {"char":"o", "num":dict["o"]}, 
                 {"char":"p", "num":dict["p"]}, 
                 {"char":"q", "num":dict["q"]}, 
                 {"char":"r", "num":dict["r"]}, 
                 {"char":"s", "num":dict["s"]}, 
                 {"char":"t", "num":dict["t"]}, 
                 {"char":"u", "num":dict["u"]}, 
                 {"char":"v", "num":dict["v"]}, 
                 {"char":"w", "num":dict["w"]}, 
                 {"char":"x", "num":dict["x"]}, 
                 {"char":"y", "num":dict["y"]},
                 {"char":"z", "num":dict["z"]}]
    dict_list.sort(reverse=True)
    return dict_list

    