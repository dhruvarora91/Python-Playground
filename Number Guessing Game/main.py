import random


def choose_number():
    return random.randint(1, 100)


def play_game(attempts_given):
    number = choose_number()
    for attempts in reversed(range(0, attempts_given + 1)):
        if attempts == 0:
            print(f'You have {attempts} attempts remaining.\nGame Over. The answer was {number}.')
        else:
            user_choice = int(input(f'You have {attempts} attempts remaining.\nMake a Guess: '))
            if user_choice > number:
                print('Too High. Make another guess.')
            elif user_choice < number:
                print('Too Low. Make another guess.')
            else:
                print(f'You Guessed the number correctly. The answer is {number}.')
                break


print("Number Guessing Game")
print("I'm of thinking of a Number between 1 and 100")

difficulty_level = input("Choose a Difficulty. Type 'easy' or 'hard': ")

easy_level_turns = 10
hard_level_turns = 5

if difficulty_level == 'easy':
    play_game(easy_level_turns)
elif difficulty_level == 'hard':
    play_game(hard_level_turns)
else:
    print('Wrong Input')
