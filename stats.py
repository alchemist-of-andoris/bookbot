#!/usr/bin/python3

def count_words(text_string):
    string_array = text_string.split()
    array_length = len(string_array)
    return array_length

def count_chars(text_string):
	char_dict = {}
	for character in text_string:
		character = character.lower()
		if character not in char_dict:
			char_dict[character] = 1
		else:
			char_dict[character] += 1
	return char_dict

def sort_dict(unsorted_dict):
	dict_list = []
	for key in unsorted_dict:
		if key.isalpha():
			list_item = {"char":key, "count":unsorted_dict[key]}
			dict_list.append(list_item)
	dict_list.sort(key=lambda dictionary: dictionary["count"], reverse=True)
	return dict_list
