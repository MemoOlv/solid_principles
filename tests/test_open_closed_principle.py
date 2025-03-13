from src.open_closed_principle import Rectangle, calculate_area, Circle

from pytest import approx


def test_rectangle_area():
    rect = Rectangle(12, 8)
    obtained = calculate_area(rect)
    expected = 96
    assert obtained == expected


def test_circle_area():
    radius = 6.5
    circle = Circle(radius)
    obtained = calculate_area(circle)
    expected = 132.73
    assert obtained == approx(expected, abs=1e-2)
