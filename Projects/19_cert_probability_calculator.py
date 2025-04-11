import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.balls = kwargs

        '''
        equivalent to: for color, n in self.balls.items():
            for _ in range(n):
                self.contents.append(color)
        '''
        self.contents = [f'{color}' for color, n in self.balls.items() for _ in range(n)]

    def draw(self, n):
        balls_drawn = []

        if n > len(self.contents):
            balls_drawn = copy.copy(self.contents)
            self.contents = []
            return balls_drawn
               
        for _ in range(n):
            random_int = random.randint(0, len(self.contents) - 1)
            balls_drawn.append(self.contents[random_int])
            self.contents.pop(random_int)
        return balls_drawn

def is_subset(dict1, dict2):
    #Functions that check if dict1 is a subset of dict2
    #dict1 = expected_balls
    #dict2 = hat_copy_draw_dict

    #expected balls = {'red':2,'green':1,'yellow':2}
    #hat_copy_draw_dict = {'red':2}
    #False

    ##expected balls = {'red':2,'green':1}
    #hat_copy_draw_dict = {'red':3,'green':2,'black':2}
    #True
    for key, value in dict1.items():
        if key not in dict2:
            return False
        if value > dict2[key]:
            return False
    return True

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)    
        hat_copy_draw = hat_copy.draw(num_balls_drawn)
        hat_copy_draw_dict = {i: hat_copy_draw.count(i) for i in hat_copy_draw}
        if is_subset(expected_balls, hat_copy_draw_dict):
            M += 1
    return M/num_experiments        

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)