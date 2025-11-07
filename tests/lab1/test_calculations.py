import pytest
from src.lab1.calculations import count_words, area_circle

@pytest.mark.parametrize("text, expected", [
    ("Hello World", 2),
    ("One two three", 3),
])
def test_count_words_valid(text, expected):
    assert count_words(text) == expected

def test_count_words_invalid():
    with pytest.raises(TypeError):
        count_words(123)

def test_area_with_mock(mocker):
    mocker.patch("src.lab1.calculations.PI", 3)
    assert area_circle(2) == 12