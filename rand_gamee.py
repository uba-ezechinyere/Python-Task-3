import random

print('GAMES BY CUBA')
print('NUMBER GUESSER')


def initialize():
    print("Can You Tell what's on my mind?")
    print('''
Select a Level of Difficulty
    
EASY
MEDIUM
HARD
    ''')
    # A Tuple containing difficulty levels as strings
    difficulty = ("EASY", "MEDIUM", "HARD")
    stage_choice = ""

    # Check for the correct input
    while not stage_choice:
        # Convert all check choices to strings
        check_choice = str(input('> ').upper())
        if check_choice in difficulty:
            stage_choice = check_choice
        else:
            print("Please type 'easy','medium' or 'hard'")
    return difficulty_selector(stage_choice)


def difficulty_selector(stage_choice):
    if stage_choice == 'EASY':
        print('''
You have Chosen the Easy Stage
In this stage you have 6 chances to make a random guesses between 1 - 10
Take your best shot 😊
        ''')

        upper_limit = 10
        secret_number = random.randint(1, upper_limit)
        guess_count = 0
        guess_limit = 6

    elif stage_choice == 'MEDIUM':
        print('''
You have Chosen the Medium Stage
In this stage you have 4 chances to make a random guesses between 1 - 20
Take your best shot 😊
        ''')

        upper_limit = 20
        secret_number = random.randint(1, upper_limit)
        guess_count = 0
        guess_limit = 4

    else:
        print('''
You have Chosen the Hard Stage
In this stage you have 3 chances to make a random guesses between 1 - 50
Take your best shot 😊
        ''')

        upper_limit = 50
        secret_number = random.randint(1, upper_limit)
        guess_count = 0
        guess_limit = 3

    return validator(secret_number, guess_count, guess_limit, upper_limit)


def validator(secret_number, guess_count, guess_limit, upper_limit):
    while guess_limit:
        try:
            guess = int(input("Take a Guess: \n>"))
        except ValueError:
            print("Please Integers Only")
        else:
            if guess < 1:
                print('❌ Number cannot be less than 1')

            elif guess > upper_limit:
                print('❌ Number cannot be greater than {}'.format(upper_limit))

            elif guess == secret_number:
                print(f'Wow You Guessed Right 🎉')
                break
            else:
                guess_limit -= 1
                print('No 😔, Try again')
                print('Chances left: \n' + str(guess_limit))
                guess_count += 1

    if guess_limit == 0:
        print("You Lost")
    return play_again()


def play_again():
    play_again_input = input('Play Again Y/N? \n')
    if play_again_input.upper() == 'N':
        print("Bye and thanks for playing ")
        return
    else:
        initialize()


initialize()
