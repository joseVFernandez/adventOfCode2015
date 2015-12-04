'''
Created on Dec 4, 2015

@author: jose.fernandez
'''

import hashlib
import itertools


def find_minimum_number_for_md5(input_string):
    for i in itertools.count():
        test_string = "".join([input_string, str(i)])
        if "00000" == hashlib.md5(test_string).hexdigest()[:5]:
            break
    return i
