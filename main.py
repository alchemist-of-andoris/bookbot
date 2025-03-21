#!/usr/bin/python3

from stats import count_words, count_chars, sort_dict

def get_book_text(file_path):
    with open(file_path) as b:
        book_text = b.read()
    return book_text

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    word_count = count_words(frankenstein)
    char_count = count_chars(frankenstein)
    sorted_dict_list = sort_dict(char_count)
    print(sorted_dict_list)
    return None

main()
