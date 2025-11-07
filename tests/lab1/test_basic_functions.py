from src.lab1.basic_functions import count_chars_in_two_ways, repeat_string


def test_repeat_string():
    assert repeat_string("ab", 3) == "ababab"

def test_count_chars():
    assert count_chars_in_two_ways("test")[0] == 4

