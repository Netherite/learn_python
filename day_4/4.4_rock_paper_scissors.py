import random 

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors. "))

computer_choice = random.randint(0, 2)

#rock
if user_choice == 0:
    print("Your choice: Rock")
    if computer_choice == 0: 
        print("Computer choice: Rock. Tie")
    elif computer_choice == 1: 
        print("Computer choice: paper. You lose.")
    else: 
        print("Computer choice: scissors. You win")

#paper
if user_choice == 1:
    print("Your choice: paper")
    if computer_choice == 0: 
        print("Computer choice: Rock. You win")
    elif computer_choice == 1: 
        print("Computer choice: paper. Tie.")
    else: 
        print("Computer choice: scissors. You lose")

#scissors
if user_choice == 2:
    print("Your choice: Scissors")
    if computer_choice == 0: 
        print("Computer choice: Rock. You lose")
    elif computer_choice == 1: 
        print("Computer choice: paper. You win.")
    else: 
        print("Computer choice: scissors. You tie")