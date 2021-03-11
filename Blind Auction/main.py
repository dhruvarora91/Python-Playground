from art import logo

print(logo)

players = {}
continue_game = True

def show_result():

  highest_bid = 0
  winner = ''
  for player in players:
    if players[player] > highest_bid:
      highest_bid = players[player]
      winner = player
  print(f'{winner} won with the bid of Rs {highest_bid}')

while continue_game:
  name = input('Enter player name: ')
  bid = int(input('Enter Bid amount: Rs '))

  players[name] = bid

  choice = input('Do you want to add new players? Type \'yes\' to add and \'no\' to get results: ').lower()

  if choice == 'yes' or choice == 'y':
    continue_game = True
  elif choice == 'no' or choice == 'n':
    continue_game = False
  else:
    print('Invalid choice!')
    break

  print("\033[H\033[2J")
  
if continue_game == False:
  show_result()
