import copy
import random

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        print(self.contents)

    def draw(self, num):
        balls_drawn = []
        if num > len(self.contents):
            return self.contents
        else:
             for i in range (num):
                balls_drawn.append(self.contents.pop(random.randrange(0, len(self.contents))))
        return balls_drawn
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    count = 0

    for i in range(num_experiments):
        #we have to make a copy of expected balls so that
        #we have the same expected balls each time
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_drawn)

        for color in colors_gotten:
            if(color in expected_copy):
                expected_copy[color] -= 1

        if(all(x <= 0 for x in expected_copy.values())):
            count += 1

    return count / num_experiments