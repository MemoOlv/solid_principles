from src.nothing import nothing
def tests_nothing():
    obtained = nothing()
    assert isinstance(obtained, str)
