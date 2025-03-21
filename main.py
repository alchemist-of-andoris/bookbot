#!/usr/bin/python3

from stats import count_words, count_chars

def get_book_text(file_path):
    with open(file_path) as b:
        book_text = b.read()
    return book_text

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    word_count = count_words(frankenstein)
    char_count = count_chars(frankenstein)
    print(word_count, "words found in the document")
    for key in char_count:
        print("\'" + key + "\': " + str(char_count[key]))
    return None

main()
