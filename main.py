def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    characters = get_count_characters(text)
    sorted_chars_list = chars_dict_to_sorted_list(characters)


    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


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
    return dict["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_dictionary_values(dict):
    dict.sort(reverse=True, key=sort_on)
    return dict


def get_word_count(received_text):
    words = received_text.split()
    return len(words)


main()
