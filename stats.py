def get_num_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    character_count = {}
    for char in text:
        character_count[char.lower()] = character_count.get(char.lower(), 0) + 1
    return character_count