# Function to get book as a string and return word count
def get_word_count(book):
    split_book = book.split()
    return len(split_book)

# Function to count every instance of every character
def get_character_count(book):
    lowercase_book = book.lower()
    character_count = {}
    for c in lowercase_book:
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] += 1
    return character_count