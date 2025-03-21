#!/usr/bin/python3

from stats import count_words, count_chars, sort_dict

def get_book_text(file_path):
    with open(file_path) as b:
        book_text = b.read()
    return book_text

def main():
    book_file = "books/frankenstein.txt"
    frankenstein = get_book_text(book_file)
    word_count = count_words(frankenstein)
    char_count = count_chars(frankenstein)
    sorted_dict_list = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_file + "...")
    print("----------- Word Count ------------")
    print("Found " + str(word_count) + " total words")
    print("--------- Character Count ---------")
    for char_count in sorted_dict_list:
        print(char_count["char"] + ": " + str(char_count["count"]))
    return None

main()
