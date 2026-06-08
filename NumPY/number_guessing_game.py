import random
correct_answer = random.randint(1, 100)
number_of_guess = 0
guess = int(input("Guess the number from 1 to 100 only: "))
while guess != correct_answer:
    number_of_guess += 1
    if guess > 100 or guess < 1:
        number_of_guess-=1
        print("Enter valild number")
    elif guess > correct_answer:
        print("Correct answer is lower")
    else:
        print("Correct answer is higher")
    
    guess = int(input("Guess the number from 1 to 100 only: "))
number_of_guess += 1
print(f"You got it correct! Congratulations! It took you {number_of_guess} guesses!")