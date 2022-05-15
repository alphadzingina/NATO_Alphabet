import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data)

phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#print(phonetic_dict)




