from words import words
import random
def get_word():
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()
def hangman():
    word=get_word()
    word_letters=set(word)
    alphabet=set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters=set()
    while len(word_letters)>0:
        print('You have used these letters: ',' '.join(used_letters))
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))
        user_letter=input('Guess a letter: ').upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')
        else:
            print('Invalid character. Please try again.')
    print(f'Congratulations! You guessed the word {word} correctly!')
hangman()