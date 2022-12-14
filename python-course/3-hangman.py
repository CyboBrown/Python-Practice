import random
from words3 import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
    
# print(get_valid_word(words))

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
    elif user_letter in used_letters:
        print('You have already used that letter. Try again.')
    else:
        