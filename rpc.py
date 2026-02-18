#rock paper scissors game 
import random
def rps():
    user=input("Enter rock, paper, or scissors: ").lower()
    computer=random.choice(['rock','paper','scissors'])
    if user==computer:
        print("It's a tie!")
    elif (user=='rock' and computer=='scissors') or (user=='paper' and computer=='rock') or (user=='scissors' and computer=='paper'):
        print("You win!")
    else:
        print("Computer wins!")
    print(f"Computer chose: {computer}")
rps()           