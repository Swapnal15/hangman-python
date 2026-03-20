# list = [1,2,4,5,43,131,232,54]


# var = 0
# for x in list:
#     if x > var:
#         var = x
#     else:
#         var

# print(var)

# for number in range(1,11):
#     print(number)

import random
import string

symbols = ['!', '@', '#', '$', '%', '&', '*']
numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']

print("Welcome to password generator")

pass_length = int(input("what should be lenght of your password?"))
pass_symbol = int(input("How many symbol do you want your password to be?"))
pass_number = int(input("How many number do you want your password to be?"))
capital_letter = (input("Do you want a capital letter? y/n"))
password = []

char_length = pass_length - pass_symbol - pass_number

# add symbols
for i in range(pass_symbol):
    password.append(random.choice(symbols))

# add numbers
for i in range(pass_number):
    password.append(random.choice(numbers))

# add letters
for i in range(char_length):
    password.append(random.choice(letters))

# shuffle password
random.shuffle(password)

# capitalize one random letter if user wants
if capital_letter == "y":
    letter_positions = []

    for i in range(len(password)):
        if password[i] in letters:
            letter_positions.append(i)

    if letter_positions:
        index = random.choice(letter_positions)
        password[index] = password[index].upper()

# convert list to string
final_password = "".join(password)

print("Your generated password is:", final_password)

