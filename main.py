from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_characters(chars_dict)
    print_report(book_path, num_words, sorted_chars)

def get_book_text(path):
     with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["count"]

def sort_characters(chars):
    characters = []
    for char in chars:
        if char.isalpha():
            characters.append({"char": char, "count": chars[char]})
    characters.sort(reverse=True, key=sort_on)
    return characters

def print_report(path, words, sorted_chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()
    for char in sorted_chars:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print("--- End report ---")

main()