def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    """Returns a dictionary with counts of each character (lowercased) in the text."""
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_character_counts(char_counts):
    """Returns a sorted list of dictionaries like {'char': 'a', 'num': 1234}, by count descending."""
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():  # Skip non-alphabet characters
            sorted_list.append({"char": char, "num": count})

    # Sort by 'num' descending
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list