class Bird:
    def fly(self):
        return "I can fly"
    def move(self):
        return "I am moving"

class FlyingBird(Bird):
    def move(self):
        return "I am flying"

class Penguin(Bird):
    def fly(self):
        return "I can't fly"

def make_bird_fly(bird):
    return bird.fly()

def make_bird_move(bird):
    return bird.move()