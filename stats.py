def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}
    for c in text:
        c = c.lower()
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_character_count_dict(char_count):
    sorted_character_count = []
    for k,v in char_count.items():
        sorted_character_count.append({"char": k, "num": v})
    sorted_character_count.sort(reverse=True, key=sort_on)
    return sorted_character_count