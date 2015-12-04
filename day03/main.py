'''
Created on Dec 4, 2015

@author: jose.fernandez
'''


class Current_location:

    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return "{},{}".format(self.x, self.y)


def santa_moving(directions, get_houses):
    houses_visited = {"0,0": 1}
    current_location = Current_location()
    for movement in directions:
        if movement == "^":
            current_location.y += 1
        elif movement == "v":
            current_location.y += -1
        elif movement == ">":
            current_location.x += 1
        elif movement == "<":
            current_location.x += -1
        current_location_string = str(current_location)
        if current_location_string in houses_visited:
            temp = houses_visited.get(current_location_string)
            temp += 1
            houses_visited.update({current_location_string: temp})
        else:
            houses_visited.update({current_location_string: 1})
    if (get_houses):
        return houses_visited
    else:
        return len(houses_visited)


def santa_and_robot_santa(directions):
    directions_for_santa = directions[1::2]
    directions_for_robot_santa = directions[::2]

    santas_houses = santa_moving(directions_for_santa, True)
    robots_santa_houses = santa_moving(directions_for_robot_santa, True)

    merged_houses = santas_houses.copy()
    merged_houses.update(robots_santa_houses)

    return len(merged_houses)
