from game_data import data

import random


def get_random_person():

    return random.choice(data)


def check_answer(a_followers, b_followers):

    if a_followers > b_followers:
        return 'a'

    elif a_followers < b_followers:
        return 'b'


def format_string(person):

    return f"{person['name']}, {person['description']}, from {person['country']}"


def play_game():

    continue_game = True
    first_person = get_random_person()
    second_person = get_random_person()
    score = 0

    while continue_game:

        if first_person == second_person:
            second_person = get_random_person()

        print(f"Compare A: {format_string(first_person)}")
        print(f"Against B: {format_string(second_person)}")
        print(first_person['follower_count'], second_person['follower_count'])  # remove this line

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct_answer = check_answer(first_person['follower_count'], second_person['follower_count'])

        if correct_answer == user_choice:
            continue_game = True
            score += 1
            print("\033[H\033[2J") # clear the screen
            print(f'Correct!! Your Current Score is: {score}')

        else:
            continue_game = False
            print(f'Wrong! Game Over. Your Final Score is: {score}')

        first_person = second_person
        second_person = get_random_person()


play_game()
