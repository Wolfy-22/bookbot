from stats import *

def get_book_text(File_path):
    with open(File_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    book_length = get_book_length(get_book_text("books/frankenstein.txt"))
    print(f"{book_length} words found in the document")

    char_count = char_number(get_book_text("books/frankenstein.txt"))
    print(char_count)

    dict_sorted = sorted_dict(char_count)
    print(dict_sorted)

main()