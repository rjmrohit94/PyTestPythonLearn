def echo_string():
    s = input("Enter text: ")
    print(s)
    return s

def sum_two_numbers(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return "Incorrect input"

def compare_types(x, y):
    return (type(x), type(y), type(x) == type(y))

def repeat_string(s, x):
    return s * x

def dict_lookup(dict_obj, k):
    return dict_obj.get(k, "Key not found")

def count_chars_in_two_ways(s):
    list_method = len(list(s))

    count_method = 0
    for _ in s:
        count_method += 1

    return list_method, count_method