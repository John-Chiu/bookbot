from stats import get_num_of_words, num_of_chars, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_num_of_words(book_text)
    num_chars = num_of_chars(book_text)
    sorted_num_chars = sort_dict(num_chars)

    ### Report Start
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in sorted_num_chars:
        key = dict["char"]
        val = dict["num"]
        if key.isalpha():
            print(f"{key}: {val}")

    print("============= END ===============")
    ### Report End

main()
