import random as rnd

def game():
    choices = ["rock","paper","scissors"]
    computerChoice = rnd.choice(choices)
    playerChoice = None
    
    while playerChoice not in choices:
        playerChoice = input("Choose between rock, paper, scissors: ").lower()
    if playerChoice == computerChoice:
        print(f"Computer: {computerChoice}")
        print(f"Player: {playerChoice}")
        print("It's a tie")
    elif playerChoice == 'rock':
        if computerChoice == 'paper':
            print(f"Computer: {computerChoice}")
            print(f"Player: {playerChoice}")
            print("You lose.")
        if computerChoice == 'scissors':
            print(f"Computer: {computerChoice}")
            print(f"Player: {playerChoice}")
            print("You win!")
    elif playerChoice == 'paper':
        if computerChoice == 'rock':
            print(f"Computer: {computerChoice}")
            print(f"Player: {playerChoice}")
            print("You win!")
        if computerChoice == 'scissors':
            print(f"Computer: {computerChoice}")
            print(f"Player: {playerChoice}")
            print("You lose.")
    elif playerChoice == 'scissors':
        if computerChoice == 'rock':
            print(f"Computer: {computerChoice}")
            print(f"Player: {playerChoice}")
            print("You lose.")
        if computerChoice == 'paper':
            print(f"Computer: {computerChoice}")
            print(f"Player: {playerChoice}")
            print("You win!")

run = True
while run:
    game()
    play_again = None
    while play_again != 'y' or 'n':
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == 'y':
            game()
        if play_again == 'n':
            run = False
            break       
print("Bye!!")



# print(f"Computer: {computerChoice}")
# print(f"Player: {playerChoice}")

