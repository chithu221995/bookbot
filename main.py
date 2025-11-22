def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_counts = count_characters(text)
    
    print_report(book_path, word_count, char_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def print_report(book_path, word_count, char_counts):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    # Convert dictionary to list of tuples and sort by count (descending)
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "count": count})
    
    char_list.sort(reverse=True, key=sort_on)
    
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    
    print("--- End report ---")


def sort_on(dict):
    return dict["count"]


main()
