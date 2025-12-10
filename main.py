import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_character_count_dict

def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    print("----------- Word Count ----------")
    word_count = get_word_count(get_book_text(file_path))
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    char_count = get_character_count(get_book_text(file_path))
    sorted_char_count = sort_character_count_dict(char_count)
    for count in sorted_char_count:
        if count["char"].isalpha():
            print(f"{count["char"]}: {count["num"]}")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()