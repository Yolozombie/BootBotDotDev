import sys

print(sys.argv)

from stats import get_word_count, count_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    
    # Display header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    # Word count section
    print("----------- Word Count ----------")
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")
    
    # Character count section
    print("--------- Character Count -------")
    char_counts = count_chars(text)
    for char_count in char_counts:
        print(f"{char_count['character']}: {char_count['count']}")
    
    # Display footer
    print("============= END ===============")

main()

