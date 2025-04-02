from stats import word_count, char_count, sort_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count = word_count(text)
    chars = char_count(text)
    sorted_char = sort_characters(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_char:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()