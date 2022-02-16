import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows() }

user_input = input('Enter word: ').upper()

char_list = [char for char in user_input]

code_list = [nato_dict[char] for char in char_list]

print(code_list)
