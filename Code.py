import random 

numberOfMember = input("How many members in your group: ")
nameList = []
majorList = []
for i in range(int(numberOfMember)):
  name = input("What is your name? ")
  nameList.append(name)
  major = input("What is your Major? ")
  majorList.append(major)

for name,major in zip(nameList,majorList):
  print(name+"'s Major is: "+major)

guess = 0
number = random.randint(1, 10)
while guess < 5:
  user_number = int(input("Guess a number I'm thinking of between 1 and 10: "))
  guess += 1
  if user_number < number: 
    print("Too low! Try again.")
  elif user_number > number:
    print("Too high! Try again.")
  else:
    print("Congratulations! You guessed correctly. +10 Bonus points on next test.")
    break
