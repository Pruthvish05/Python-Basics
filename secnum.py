#random number using computer just
import random
def game(n):
    rand_number = random.randint(1, n)
    guess=0
    count=0
    while guess != rand_number:
        guess = int(input(f"Guess a number between 1 and {n}: "))
        count += 1
        if guess < rand_number:
            print("Too low")
        elif guess > rand_number:
            print("Too high")
    print(f"Congratulations! You guessed the number {rand_number} correctly in {count} attempts.")
game(8)
def computer_guess(n):
    guess = random.randint(1, n)
    count = 0
    print(f"Think of a number between 1 and {n} and I will try to guess it.")
    while True:
        count += 1
        print(f"My guess is: {guess} let me know high(h) or low(l) or crct(c)")
        feedback = input("Enter your feedback: ")
        if feedback == 'h':
            guess = random.randint(guess + 1, n)
        elif feedback == 'l':
            guess = random.randint(1, guess - 1)
        elif feedback == 'c':
            print(f"I guessed your number {guess} correctly in {count} attempts!").lower()
            break
        else:
            print("Invalid feedback. Please enter 'h', 'l', or 'c'.")
computer_guess(9)