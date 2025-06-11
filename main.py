from stats import get_word_count
from stats import get_character_count
from stats import sort_characters
import sys

# Function to get the contents of a book and return it as a string
def get_book_text(filepath):

    book_content = ""
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def print_report(filepath, word_count, char_count):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}t...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in range(0, len(char_count)):
        if char_count[i]["char"].isalpha():
            print(f"{char_count[i]["char"]}: {char_count[i]["num"]}")
    print("============= END ===============")

    return None

def main():

    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    
    book = get_book_text(filepath)
    word_count = get_word_count(book)
    char_count = get_character_count(book)
    sorted_chars = sort_characters(char_count)
    print_report(filepath, word_count, sorted_chars)
    return None

main()