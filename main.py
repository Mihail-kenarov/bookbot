def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    characters = get_count_characters(text)
    list = sort_dictionary_values(characters)

    print(num_words)
    print(characters)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(received_text):
    words = received_text.split()
    return len(words)

def get_count_characters(words):
    character_count = {}
    lowerd_words = words.lower()

    for char in lowerd_words:
        if char in character_count:
            character_count[char] +=1
        else:
            character_count[char] = 1
    
    return character_count 


def sort_on(dict):
    return dict["character"]


def sort_dictionary_values(dict):
    dict.sort(reverse=True, key=sort_on)
    return 0


def get_word_count(received_text):
    words = received_text.split()
    return len(words)


main()