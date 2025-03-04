from src.liskov_substitution_principle import Bird, make_bird_fly, Penguin

def test_flying_penguin():
    bird = Bird()
    obtained = make_bird_fly(bird)
    expected = "I can fly"
    assert obtained == expected

    penguin = Penguin()
    obtained = make_bird_fly(penguin)
    expected = "I can't fly"
    assert obtained == expected
