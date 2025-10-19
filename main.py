from stats import count_words, count_chars, dicto_sortlist
import sys

def get_book_text(file_path):
    with open(file_path) as book:
        book_content = book.read()
    return book_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
    print(path_to_book)
    book_content = get_book_text(path_to_book)
    num_words = count_words(book_content)
    char_count = count_chars(book_content)
    sorted_list = dicto_sortlist(char_count)
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {path_to_book}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------""")
    for dict in sorted_list:
        if dict["char"].isalpha():
            print (f"{dict['char']}: {dict['count']}")


main()