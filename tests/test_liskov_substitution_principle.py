from src.liskov_substitution_principle import Bird, make_bird_fly

def test_flying_penguin():
    bird = Bird()
    obtained = make_bird_fly(bird)
    expected = "I can fly"
    assert obtained == expected
