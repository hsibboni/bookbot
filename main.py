def main():
    book_path = "books/frankenstein.txt"
    print (f"--- Begin report of {book_path} ---")
    file_contents = get_book_text(book_path)
    words_count = get_words_count(file_contents)
    print(f"{words_count} words found in the document")
    chars_dict = get_chars_dict(file_contents)
    print("")
    char_dict_list = []
    for char in chars_dict:
        char_dict_list.append({'char': char, 'count': chars_dict[char]})
    char_dict_list.sort(reverse=True, key=sort_by_count)
    for char_dict in char_dict_list:
        if not char_dict["char"].isalpha():
            continue
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

    print("--- End report ---")
    

def sort_by_count(dict):
    return dict['count']

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_words_count(contents):
    words = contents.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()