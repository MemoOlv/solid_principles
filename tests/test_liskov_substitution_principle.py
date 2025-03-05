from src.liskov_substitution_principle import Bird, make_bird_fly, Penguin, make_bird_move, FlyingBird, FlightlessBird

def test_flying_penguin():
    bird = Bird()
    obtained = make_bird_fly(bird)
    expected = "I can fly"
    assert obtained == expected

    obtained = make_bird_move(bird)
    expected = "I am moving"
    assert obtained == expected

    eagle = FlyingBird()
    obtained = make_bird_move(eagle)
    expected = "I am flying"
    assert obtained == expected


    penguin = Penguin()
    obtained = make_bird_fly(penguin)
    expected = "I can't fly"
    assert obtained == expected

    penguin = FlightlessBird()
    obtained = make_bird_move(penguin)
    expected = "I am walking"
    assert obtained == expected
