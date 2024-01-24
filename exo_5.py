students = [
    "Merouane",
    "Baptiste",
    "Caroline",
    "Joe",
    "Sophie",
    "Nathan",
    "Raphaël",
    "Axel",
    "Mathieu",
    "Adrien",
]

students_alphabet_order = sorted(students)
for student in students_alphabet_order:
    print(student)
    

print("First letter is M :")    
first_letter_m = [name for name in students if name.startswith("M")]
for name in first_letter_m:
    print(name)
    

for i in range(16):
    print(i)
    
for i in range(1, 11):
    print(i)
    if i == 5:
        print("break ")
        break
       
for i in range(1, 11):
    if i ==5 :
        continue
    print(i)
    

myList = [17,38,10,25,72]
print(myList)
sortedList = sorted(myList)
print(sortedList)
myList.append(12)
print(myList)
reversList = list(reversed(myList))
print(reversList)
index17 = reversList.index(17)
print(index17)
myList.remove(38)
print(myList)
subList2To3 = myList[1:3]
print(subList2To3)
subBeginTo2 = myList[:2]
print(subBeginTo2)
subListEndTo3 = myList[2:]
print(subListEndTo3)
completeSubLIst = myList[:]
print(completeSubLIst)
lastElemNegativeIndex = myList[-1]
print(lastElemNegativeIndex)

choiceNumber = int(input("choice a number: "))
while choiceNumber >= 0:
    print(choiceNumber, end=", ")
    choiceNumber -=1
    
import random


randomNumber = random.randint(1, 10)

while True:
    userChoice = int(input("Guess the number (between 1 and 10): "))
    if userChoice < randomNumber:
        print("It is more")
    elif userChoice > randomNumber:
        print("Is is less")
    else:
        print("you won")
        break
    
all_students = [
    ["David", "Justine", "Valentin", "Axel", "Redouane"],
    ["Julie", "Stéphane", "Mostapha", "Claudiu", "Son"],
]
for students in all_students:
    for studentName in students:
        print(f"{studentName} is an alumi")

languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]
for i, allLangages in enumerate(languages):
    for langage in allLangages:
        if i == 0:
            print(f"{langage} is a backend langage")
        elif i == 1:
            print(f"{langage} is a frontend langage")