import random
import string

print('GAMES BY CUBA')
print('NUMBER GUESSER')

print("Can You Tell what's on my mind?")
print('''
Select a Level of Difficulty

EASY
MEDIUM
HARD
''')


stage_choice = ''

stage_choice = input('> ').upper()
while stage_choice:

    try:
        if stage_choice == 'EASY':
            print('''
You have Chosen the Easy Stage
In this stage you have 6 chances to make a random guesses between 1 - 10
Take your best shot 😊
        ''')

            secret_number = random.randint(1, 10)
            guess_count = 0
            guess_limit = 6

            while guess_limit:
                guess = int(input("Take a Guess: \n>"))

                if guess != secret_number:
                    guess_limit -= 1
                    print('No 😔, Try again')
                    print('Chances left: \n' + str(guess_limit))
                    guess_count += 1

                elif guess < 1:
                    print('❌ Number cannot be less than 1')

                elif guess > 10:
                    print('❌ Number cannot be greater than 10')

                elif guess == secret_number:
                    print(f'Wow You Guessed Right 🎉')
                    break
            else:
                print('Cheers')

        elif stage_choice == 'MEDIUM':
            print('''
You have Chosen the Medium Stage
In this stage you have 4 chances to make a random guesses between 1 - 20
Take your best shot 😊
        ''')

            secret_number = random.randint(1, 20)
            guess_count = 0
            guess_limit = 4

            while guess_limit:
                guess = int(input("Take a Guess: \n>"))

                if guess != secret_number:
                    guess_limit -= 1
                    print('No 😔, Try again')
                    print('Chances left: \n' + str(guess_limit))
                    guess_count += 1

                elif guess < 1:
                    print('❌ Number cannot be less than 1')

                elif guess > 20:
                    print('❌ Number cannot be greater than 10')

                elif guess == secret_number:
                    print(f'Wow You Guessed Right 🎉')
                    break
            else:
                print('Cheers')

        elif stage_choice == 'HARD':
            print('''
You have Chosen the Hard Stage
In this stage you have 3 chances to make a random guesses between 1 - 50
Take your best shot 😊
        ''')

            secret_number = random.randint(1, 50)
            guess_count = 0
            guess_limit = 3

            while guess_limit:
                guess = int(input("Take a Guess: \n>"))

                if guess != secret_number:
                    guess_limit -= 1
                    print('No 😔, Try again')
                    print('Chances left: \n' + str(guess_limit))
                    guess_count += 1

                elif guess < 1:
                    print('❌ Number cannot be less than 1')

                elif guess > 50:
                    print('❌ Number cannot be greater than 10')

                elif guess == secret_number:
                    print('Wow You Guessed Right 🎉')
                    break
            else:
                print('Cheers')

        play_again = input('Play Again Y/N? \n')
        if play_again.upper() == 'N':
            stage_choice = False
        else:
            stage_choice = True

        print('Thanks for Playing')
    except ValueError:
        print('Invalid Value')









