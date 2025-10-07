def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_character(text):
    char_counts = {}
    for i in text.lower():
        if i not in char_counts:
            char_counts[i] = 1
        else:
            char_counts[i] += 1
    return char_counts


def sort_on(item):
    return item["num"]


def sort_dictionary(char_dict):
    sorted_list = []
    for char, num in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": num})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
