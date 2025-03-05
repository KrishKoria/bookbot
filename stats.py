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