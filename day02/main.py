'''
Created on Dec 4, 2015

@author: jose.fernandez
'''


def calculate_wrapping_paper(l, w, h):
    area_one = l * w
    area_two = w * h
    area_three = h * l
    result = 2 * area_one + 2 * area_two + 2 * area_three
    values = [area_one, area_two, area_three]
    result += min(values)
    return result


def calculate_total(dimensions):
    total = 0
    array_of_dimensions = dimensions.split('\n')
    for present in array_of_dimensions:
        array_of_dimension = present.split("x")
        l = int(array_of_dimension[0].strip())
        w = int(array_of_dimension[1].strip())
        h = int(array_of_dimension[2].strip())
        total += calculate_wrapping_paper(l, w, h)
    return total

if __name__ == '__main__':
    pass
