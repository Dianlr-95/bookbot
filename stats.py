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

def sort_on(dict):
    return dict["num"]

# Transform a dictionary into a list of dictionaries and sort it
def sort_characters(dict):

    list = []

    for item in dict:
        aux = {}
        aux["char"] = item
        aux["num"] = dict[item]
        list.append(aux)

    list.sort(reverse=True, key=sort_on)

    return list