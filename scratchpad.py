from string import ascii_uppercase
from random import choice

def read_words_file(filename):
    f = open(filename)
    text = f.read().upper()
    words = text.splitlines()
    f.close()
    return words 

ALL_WORDS = read_words_file('proverbs.txt')


list_of_letters = [letter for letter in ascii_uppercase]
word = choice(ALL_WORDS)
word = word.upper()
blank_word = []
print(word)

guessed_letters=['I','A','V']


for i in word:
    if i in guessed_letters:
        blank_word.append(i)
    if i in list_of_letters:
        blank_word.append("_")
    else:
        blank_word.append(i)
blank_word = "".join(blank_word)
print(blank_word)









# for index,letter in enumerate(word):
#     print(index, letter)
        



# for letter in ascii_uppercase:
#     list_of_letters.append(letter)

# my_list = ['apple', 'banana', 'grapes', 'pear']
# for c, value in enumerate(my_list, 1):
#     print(c, value)



# # Example replacing an item in a string
# str = "this is string example....wow!!! this is really string"
# print(str.replace("is", "was"))
# print(str.replace("is", "was", 3))

