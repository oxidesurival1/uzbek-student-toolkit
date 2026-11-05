import pytest

from utils import (
    calculate_average,
    calculate_percentage,
    convert_length,
)


def test_calculate_average():
    assert calculate_average([5, 4, 5, 3]) == 4.25


def test_empty_grades():
    with pytest.raises(ValueError):
        calculate_average([])


def test_calculate_percentage():
    assert calculate_percentage(200, 25) == 50


def test_convert_length():
    assert convert_length(100, "cm", "m") == 1


def test_convert_km_to_m():
    assert convert_length(2, "km", "m") == 2000


def test_invalid_unit():
    with pytest.raises(ValueError):
        convert_length(10, "kg", "m")
