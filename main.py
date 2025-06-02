from stats import *

def get_book_text(File_path):
    with open(File_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    import sys
    

    try:
        book_length = get_book_length(get_book_text(sys.argv[1]))
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    char_count = char_number(get_book_text(sys.argv[1]))

    dict_sorted = sorted_dict(char_count)

    print("============ BOOKBOT ============")
    print("")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("")
    print("----------- Word Count ----------")
    print("")
    print(f"Found {book_length} total words")
    print("")
    print("-------- Character Count --------")
    print("")

    for dict in dict_sorted:
        print(f"{dict["char"]}: {dict["num"]} ")

    print("")
    print("============= END ==============")

main()