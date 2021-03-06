#Password Generator Project
# import package
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# set inupt variables
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


easy_code = ''

# randomly get letter
for j in range(0,nr_letters):  
  random_num = random.randint(0,len(letters)-1)
  for i in letters:
    if i == letters[random_num]:
      easy_code += i


# randomly get number
for j in range(0,nr_numbers):  
  random_num = random.randint(0,len(numbers)-1)
  for i in numbers:
    if i == numbers[random_num]:
      easy_code += i

      
# randomly get symbol      
for j in range(0,nr_symbols):  
  random_num = random.randint(0,len(symbols)-1)
  for i in symbols:
    if i == symbols[random_num]:
      easy_code += i

# Lecturer's code
# for char in range(1,nr_letters +1):
#   easy_code += random.choice(letters)

# for char in range(1,nr_numbers +1):
#   easy_code += random.choice(numbers)

# for char in range(1,nr_symbols +1):
#   easy_code += random.choice(symbols)
  
# print(easy_code)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# create a list to contain the string we obtain
hard_code = []

for j in range(0,nr_letters):  
  random_num = random.randint(0,len(letters)-1)
  for i in letters:
    if i == letters[random_num]:
      hard_code += i
      
for j in range(0,nr_numbers):  
  random_num = random.randint(0,len(numbers)-1)
  for i in numbers:
    if i == numbers[random_num]:
      hard_code += i

for j in range(0,nr_symbols):  
  random_num = random.randint(0,len(symbols)-1)
  for i in symbols:
    if i == symbols[random_num]:
      hard_code += i
      
# rearrange the list
random.shuffle(hard_code)

hard_fin_code = ''

for i in hard_code:
  hard_fin_code += i

print(f"Your new password is: {hard_fin_code}") 

