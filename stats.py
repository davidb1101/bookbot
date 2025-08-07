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

def sort_on(items):
    return items["num"]

def sorted_character_count(char_count_dict):
    report_list = []
    for k, v in char_count_dict.items():
        report_list.append({"name": k, "num": v})
    report_list.sort(key=sort_on, reverse=True)
    return report_list