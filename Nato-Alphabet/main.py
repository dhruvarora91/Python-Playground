import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows() }

def generate_phonetic():

  user_input = input('Enter word: ').upper()

  char_list = [char for char in user_input]

  try:
    code_list = [nato_dict[char] for char in char_list]
  except KeyError:
    print("Only Alphabets allowed")
    generate_phonetic()
  else: 
    print(code_list)

generate_phonetic()