'''
Created on Dec 4, 2015

@author: jose.fernandez
'''


def is_it_nice(string_input):
    number_of_vowels = 0
    not_contains_naughty_combo = True
    has_two_identical_letters_in_a_row = False

    for index in range(len(string_input)):
        char = string_input[index]

        if (char == "a" or char == "e" or char == "i" or
                char == "o" or char == "u"):
            number_of_vowels += 1

        upper_ceiling = len(string_input) - 1
        if index < upper_ceiling:
            next_index = index + 1
            next_char = string_input[next_index]
            combination = "".join([char, next_char])

            if (combination == "ab" or combination == "cd" or
                    combination == "pq" or combination == "xy"):
                not_contains_naughty_combo = False
                break

            if (combination[0] == combination[1]):
                has_two_identical_letters_in_a_row = True

    if (not_contains_naughty_combo and number_of_vowels >= 3 and
            has_two_identical_letters_in_a_row):
        result = True
    else:
        result = False

    return result


def is_it_nice_redux(string_input):
    pairs = {}
    three_letter_repeat = False

    for index in range(len(string_input)):
        char = string_input[index]

        upper_ceiling = len(string_input) - 2
        if index < upper_ceiling:
            next_index = index + 2
            chunk = string_input[index:next_index]
            if chunk in pairs:
                temp = pairs.get(chunk)
                temp.extend([index])
                pairs.update({chunk: temp})
            else:
                pairs.update({chunk: [index]})

        upper_ceiling2 = len(string_input) - 3
        if index < upper_ceiling2:
            two_ahead = index + 3
            two_ahead_char = string_input[two_ahead]
            if (char == two_ahead_char):
                three_letter_repeat = True

    multiple_pairs = False
    for key in pairs:
        array_of_indexes = pairs.get(key)
        for index2 in array_of_indexes:
            upper_ceiling = len(array_of_indexes) - 1
            if index2 < upper_ceiling:
                if array_of_indexes[index2 + 1] - array_of_indexes[index2] > 1:
                    multiple_pairs = True
                    break

    if (three_letter_repeat and multiple_pairs):
        result = True
    else:
        result = False

    return result


def count_number_of_nice(string_of_strings):
    list_of_strings = string_of_strings.split('\n')
    return sum(bool(is_it_nice(x.strip())) for x in list_of_strings)


def count_number_of_nice_redux(string_of_strings):
    list_of_strings = string_of_strings.split('\n')
    return sum(bool(is_it_nice_redux(x.strip())) for x in list_of_strings)
