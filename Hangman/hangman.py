import random

from hangman_words import word_list
chosen_word = random.choice(word_list)

from hangman_art import stages, logo
print(logo)

display = []

for i in range(len(chosen_word)):
  display.append('_')

game_over = False
lives = 6

while not game_over:

  guess = input('Guess a letter: ').lower()

  if guess in display:
    print(f'{guess} is already guessed')

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if guess == letter:
      display[position] = letter

  if guess not in chosen_word:
    print(f'{guess} is not in the word. Try Again!')
    lives -= 1
    if lives == 0:
      game_over = True
      print(f'You lose! The correct word was {chosen_word}.')

  print(f"{' '.join(display)}")

  if '_' not in display:
    game_over = True
    print('You Win!')

  print(stages[lives])