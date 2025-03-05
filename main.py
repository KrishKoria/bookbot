import sys

def count_words(text):
    words = text.split()
    return len(words)

def count_each_letter(text):
    text = text.lower()
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def show_report(total_words, each_letter_count):
    print(f"Total words: {total_words}")
    for letter, count in each_letter_count:
        print(f"{letter}: {count}")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

with open(book_path) as f:
    content = f.read()
    num_words = count_words(content)
    # num_each_word = count_each_word(content)
    num_each_letter = count_each_letter(content)
    sorted_letters = sorted(num_each_letter.items(), key=lambda x: x[1], reverse=True) 
    show_report(num_words, sorted_letters)