from stats import words_in_string, characters_in_string, sort_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    num_words = words_in_string(get_book_test(sys.argv[1]))
    num_chars = characters_in_string(get_book_test(sys.argv[1]))
    sorted_chars = sort_dict(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")



main()