import random

while True:
    answers = {
    "1":"rock",
    "2":"paper",
    "3":"scissors"
    }

    again = {
        '1':'yes',
        '2':'no'
    }

    
    user_answer = input("1-rock, 2-paper, 3-scissors; choose: ")
    user_choice = answers.get(user_answer)

    computer_answer = random.choice(["rock","paper","scissors"])

    if user_choice:
        
        if (user_choice == "rock" and computer_answer == "rock") or  (user_choice == "paper" and computer_answer == "paper") or (user_choice == "scissors" and computer_answer == "scissors"):
            print("No one win")
        elif (user_choice == "paper" and computer_answer == "rock") or (user_choice == "scissors" and computer_answer == "paper") or (user_choice == "rock" and computer_answer == "scissors"):
            print(f"You won because you chose {user_choice} and computer chose {computer_answer}")
        else:
            print(f"You lost because you chose {user_choice} and computer chose {computer_answer}")

    else:
        print("Enter Valid Choice")

    user_preference = input("Do you wanna play again? 1-yes, 2-no: ")
    user_preference_n = again.get(user_preference)

    if user_preference_n:
        if user_preference_n == 'yes':
            pass
        else:
            break