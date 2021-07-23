
print("created by hussainatphysics@gmail.com(hussainsha syed)")
print("welcome to passward generator")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


a =''
for i in range(1, nr_letters+1):
  a+= random.choice(letters)
b=''
for i in range(1, nr_numbers+1):
  b+= random.choice(numbers)
c=''
for k in range(1, nr_symbols+1):
  c+=random.choice(symbols)
print(f"your password is:{a}{b}{c}")



d = a+b+c
print(''.join(random.sample(d, len(d))))


print()
but1 = print(input("press enter for bye"))