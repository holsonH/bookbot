from stats import get_num_words
from stats import get_num_characters
from stats import sorted_list

def get_book_text(path_to_file):
    content = ""

    with open(path_to_file) as f:
        content = f.read()

    return content

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")


    words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {words} total words")

    dictionary = get_num_characters(book_text)

    lista = sorted_list(dictionary)

    print("--------- Character Count -------")
    print(dictionary)


main()


