
class Knot:
    def __init__(self, location):
        self.location = location
    
    def move(self, direction, distance=1):
        if direction == 'U':
            self.location = (self.location[0], self.location[1] + distance)
        elif direction == 'D':
            self.location = (self.location[0], self.location[1] - distance)
        elif direction == 'R':
            self.location = (self.location[0] + distance, self.location[1])
        elif direction == 'L':
            self.location = (self.location[0] - distance, self.location[1])
    
    def get_location(self):
        return self.location


class Head(Knot):
    def __init__(self, location=(0, 0)):
        super().__init__(location)
    

class Tail(Knot):
    def __init__(self, location=(0, 0)):
        super().__init__(location)
    
    def calculate_move(self, head_location):
        if (abs(self.location[0] - head_location[0]) <= 1) and (abs(self.location[1] - head_location[1]) <= 1):
            pass
        elif self.location[0] == head_location[0]:
            if self.location[1] < head_location[1]:
                self.location = (self.location[0], self.location[1] + 1)
            else:
                self.location = (self.location[0], self.location[1] - 1)
        elif self.location[1] == head_location[1]:
            if self.location[0] < head_location[0]:
                self.location = (self.location[0] + 1, self.location[1])
            else:
                self.location = (self.location[0] - 1, self.location[1])
        else:
            if self.location[0] < head_location[0]:
                self.location = (self.location[0] + 1, self.location[1])
            else:
                self.location = (self.location[0] - 1, self.location[1])
            if self.location[1] < head_location[1]:
                self.location = (self.location[0], self.location[1] + 1)
            else:
                self.location = (self.location[0], self.location[1] - 1)

with open('input.txt') as input:
    input_arr = []
    for line in input:
        input_arr.append(line.strip())

head = Head()
tail = Tail()
visited = {tail.get_location()}

for line in input_arr:
    direction, distance = line.split(' ')
    for i in range(int(distance)):
        head.move(direction)
        tail.calculate_move(head.get_location())
        visited.add(tail.get_location())

print(len(visited))