#random number using computer just
import random
def game(n):
    rand_number = random.randint(1, n)
    guess=0
    while guess != rand_number:
        guess = int(input(f"Guess a number between 1 and {n}: "))
        if guess < rand_number:
            print("Too low")
        elif guess > rand_number:
            print("Too high")
    print(f"Congratulations! You guessed the number {rand_number} correctly.")
