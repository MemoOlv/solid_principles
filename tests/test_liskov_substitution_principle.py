from src.liskov_substitution_principle import Bird, make_bird_move, FlyingBird, FlightlessBird

def test_generic_bird():
    bird = Bird()
    obtained = make_bird_move(bird)
    expected = "I am moving"
    assert obtained == expected

def test_flying_bird():
    eagle = FlyingBird()
    obtained = make_bird_move(eagle)
    expected = "I am flying"
    assert obtained == expected

def test_flightless_bird():
    penguin = FlightlessBird()
    obtained = make_bird_move(penguin)
    expected = "I am walking"
    assert obtained == expected
