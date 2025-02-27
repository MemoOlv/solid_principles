from src.open_closed_principle import Rectangle, calculate_area

def test_rectangle_area():
    rect = Rectangle(12, 8)
    obtained = calculate_area(rect)
    expected = 96
    assert obtained == expected
