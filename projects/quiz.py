#------------------------------------#
def new_game():
    guesses = []
    correct_guess = 0
    question_num = 1

    for key in questions:
        print("#-----------------------------------#")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter A, B, C, or D: ")
        guess = guess.upper() # sanitizes the input since string inputs are case sensitive
        guesses.append(guess) # add their answer to the empty list
        correct_guess += check_answer(questions.get(key),guess) # takes two arguments, the answer and the guess
        # ^^^^^^^ correct_guess is initially == 0, and the check_answer function returns a point that
        # is added to the correct_guess variable

        question_num+=1

    display_score(correct_guess, guesses) #takes in the points and the guesses made (letters inputted)
    

#------------------------------------#
def check_answer(answer, guess): # takes answer and guess 
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

#------------------------------------#
def display_score(correct_guess, guesses):
    print("#------------------------------------#")
    print("RESULTS:")
    print("#------------------------------------#")
    print("Answers: ", end="")
    for i in questions: # prints values of the dictionary, so these are the letters
        print(questions.get(i), end="")
    print()
    print("Guesses: ", end="")
    for i in guesses: 
        print(i, end="")
    print()

    score = int((correct_guess/len(questions))*100)
    print(f"Your got {score}% correct!")
    print(f"{correct_guess} out of {len(questions)}")
    


#------------------------------------#
def play_again():
    response = input("Do you want to play again? (Yes or No): ")
    response = response.upper()
    if response == 'YES':
        return True
    else:
        return False

#------------------------------------#

questions = {
    "What shape is round? ":"A",
    "What color is orange? ":"A",
    "What is a toothbrush for? ":"C",
    "What is the baby version of a goat? ":"B"
    }

options = [
    ["A. Circle","B. The Pyramids","C. Spongebob","D. Your mom"],
    ["A. Orange","B. Strawberry","C. Starfruit","D. Your mom"],
    ["A. Childbirth","B. Satan","C. Teeth","D. Your mom"],
    ["A. Poor people","B. Kid","C. Guppies","D. Your mom"]
    ]

#------------------------------------#

new_game()

while play_again():
    new_game()
print("Goodbye!")

# 3.35.39










#------------------------------------#

# just a function that produces the options because im lazy
# def options():
#     A = input("First option: ")
#     B = input("Second option: ")
#     C = input("Third option: ")
#     D = input("Fourth option: ")
#     print(f"[\"A. {A}\",\"B. {B}\",\"C. {C}\",\"D. {D}\"],")
# options()















