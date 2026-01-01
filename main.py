import sys
from stats import word_counter, char_counter, sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_list = book_text.split()

    # use your word_counter correctly: it expects the *text*, not the list
    word_num = word_counter(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_num} total words")
    print("--------- Character Count -------")

    # char_counter expects the list of words
    chars = char_counter(word_list)
    char_count = sorted_dict(chars)

    for item in char_count:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")

main()