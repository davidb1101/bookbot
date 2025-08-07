def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1

    return char_count_dict