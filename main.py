import sys
from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_list


def get_book_text(path_to_file):
    content = ""

    with open(path_to_file) as f:
        content = f.read()

    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")


    words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {words} total words")

    dictionary = get_num_characters(book_text)

    lista = get_sorted_list(dictionary)

    print("--------- Character Count -------")
    for char in lista:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

main()


