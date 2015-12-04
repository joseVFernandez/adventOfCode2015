'''
Created on Dec 4, 2015

@author: jose.fernandez
'''

import hashlib
import itertools


def find_minimum_number_for_md5(input_string, number_of_zeroes):
    result_string = "0" * number_of_zeroes
    for i in itertools.count():
        test_string = "".join([input_string, str(i)])
        if (result_string ==
                hashlib.md5(test_string).hexdigest()[:number_of_zeroes]):
            break
    return i
