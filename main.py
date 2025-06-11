from stats import get_word_count

# Function to get the contents of a book and return it as a string
def get_book_text(filepath):
    book_content = ""
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def main():
    filepath = "books/frankenstein.txt"
    book = get_book_text(filepath)
    word_count = get_word_count(book)
    print(f"{word_count} words found in the document")
    return None
main()