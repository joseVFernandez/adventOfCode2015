'''
Created on Dec 4, 2015

@author: jose.fernandez
'''


class Decoration ():
    dimension = 0
    lights_setup = []

    def __init__(self):
        dimension = 1000
        self.lights_setup = [x[:] for x in [[False] * dimension] * dimension]

    def sum_up_lights_on(self):
        return sum(sum(self.lights_setup, []))

    def toggle_light(self, x, y):
        self.lights_setup[x][y] = not self.lights_setup[x][y]

    def toggle_rect(self, x1, y1, x2, y2):
        for j in range(y1, y2 + 1):
            for i in range(x1, x2 + 1):
                self.toggle_light(i, j)

    def turn_on_light(self, x, y):
        self.lights_setup[x][y] = True

    def turn_on_rect(self, x1, y1, x2, y2):
        for j in range(y1, y2 + 1):
            for i in range(x1, x2 + 1):
                self.turn_on_light(i, j)

    def turn_off_light(self, x, y):
        self.lights_setup[x][y] = False

    def turn_off_rect(self, x1, y1, x2, y2):
        for j in range(y1, y2 + 1):
            for i in range(x1, x2 + 1):
                self.turn_off_light(i, j)

    def process_instruction(self, instruction):
        instruction = instruction.strip()
        parts = instruction.split(" ")
        if len(parts) == 4:  # toogle
            start = parts[1].split(",")
            end = parts[3].split(",")

            self.toggle_rect(
                int(start[0]), int(start[1]), int(end[0]), int(end[1]))
        else:
            start = parts[2].split(",")
            end = parts[4].split(",")

            if parts[1] == "on":
                self.turn_on_rect(
                    int(start[0]), int(start[1]),
                    int(end[0]), int(end[1]))
            else:  # turn off
                self.turn_off_rect(
                    int(start[0]), int(start[1]),
                    int(end[0]), int(end[1]))

    def process_multiple_instructions(self, instructions):
        array_of_instructions = instructions.split('\n')
        for instruction in array_of_instructions:
            self.process_instruction(instruction)
        return self.sum_up_lights_on()

if __name__ == "__main__":
    pass
