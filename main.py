import sys
from stats import get_num_words, count_chars

def get_book_text(path_to_file):
    i=0
    with open(path_to_file) as f:
        file_contents = f.read()
    return (file_contents)

def main():
    import sys
    if len(sys.argv) !=2:
        print(f"Usage: python3 main.py <path_to_book>")        
        sys.exit(1)
    book_path = sys.argv[1]
    print(sys.argv)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    content = get_book_text(book_path)
    print(f"----------- Word Count ----------\nFound {get_num_words(content)} total words")
    print(f"--------- Character Count -------")
    char_count = count_chars(content)
    for char, count in char_count.items():
        print(f"{char}: {count}")
    print(f"============= END ===============")

main()
