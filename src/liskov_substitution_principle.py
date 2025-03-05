class Bird:
    def move(self):
        return "I am moving"

class FlyingBird(Bird):
    def move(self):
        return "I am flying"

class FlightlessBird(Bird):
    def move(self):
        return "I am walking"

def make_bird_move(bird):
    return bird.move()