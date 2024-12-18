"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""

def is_pangram(st):
    st = st.lower()
    letter_count = {}
    for letter in st:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1 
    return len(letter_count) == 26


def is_pangram(st):
    st = st.lower()
    res = set()
    for letter in st:
        if letter.isalpha():
            res.add(letter)
    return len(res) == 26 

