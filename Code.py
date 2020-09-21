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
