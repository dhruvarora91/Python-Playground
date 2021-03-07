alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo

print(logo)

def caesar(text, shift_number, type):
    if type == 'encode':
      caesar_text = ''
      for character in text:
        if character in alphabet:
          position = alphabet.index(character)
          new_position = position + shift_number
          caesar_text += alphabet[new_position]
        else:
          caesar_text += character
      print(caesar_text)
    elif type == 'decode':
      normal_text = ''
      for character in text:
        if character in alphabet:
          position = alphabet.index(character)
          new_position = position - shift_number
          normal_text += alphabet[new_position]
        else:
          normal_text += character
      print(normal_text)
    else:
      print('invalid choice')

is_game_over = False

while not is_game_over:
  direction = input('Type \'encode\' to encrpyt and \'decode\' to decrypt: ').lower().strip()
  if not (direction == 'encode' or direction == 'decode'):
    is_game_over = True
    print('Invalid option')
    break
  message = input('Enter message: ').lower()
  shift = int(input('Enter shift number: '))
  shift = shift % 26
  caesar(message, shift, direction)
  choice = input('Do you want to go again? Type \'yes\' to continue and \'no\' to stop: ').lower()
  if choice == 'no':
    is_game_over = True
    print('Thanks for playing')

