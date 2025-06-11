# Function to get the contents of a book and return it as a string
def get_book_text(filepath):
    book_content = ""
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def main():
    path = "books/frankenstein.txt"
    book = get_book_text(path)
    print(book)
    return None
main()