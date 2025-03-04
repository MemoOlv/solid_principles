class Bird:
    def fly(self):
        return "I can fly"

class Penguin(Bird):
    def fly(self):
        return "I can't fly"

def make_bird_fly(bird):
    return bird.fly()
