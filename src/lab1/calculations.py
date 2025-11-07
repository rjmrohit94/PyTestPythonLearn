PI = 3.14159

def count_words(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    words = [w for w in text.split(" ") if w.strip() != ""]
    return len(words)

def total_characters(word_list):
    return len("".join(word_list))

def area_circle(radius):
    return round(PI * (radius ** 2), 4)