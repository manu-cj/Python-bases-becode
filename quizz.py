stringVar = "toto"
numberVar = 10

unicodeString = [ord(char) for char in stringVar]
floatNumber = float(numberVar)

reversedString = stringVar[::-1]
reversedNumber = float(str(numberVar)[::-1])

print(reversedNumber)


#List
firstList = [1, 3, 2, 7, 4, 10, 46]
print(firstList[:3])

secondList = [firstList[3], firstList[4], firstList[5]]
print(secondList)

thirdList = firstList + secondList
print(thirdList)

tuple_of_lists = list(zip(firstList, secondList))

print(tuple_of_lists)

firstList.append(5)
thirdList.append(None)

def concatList(my_list, n):
    return my_list * n

my_list = [1, 2, 3]
result = concatList(my_list, 2)
print(result)

def concatList2(my_list, n=2):
    return my_list * n


result2 = concatList2(my_list)
result3 = concatList2(my_list, 3) 
print(result2)
print(result3)

i = 0
while i < len(thirdList):
    print(thirdList[i])
    i += 1
    
count = 0
for num in firstList:
    if num % 2 == True:
        count += 1
        
print(count)

even_numbers = []
for element in firstList:
    if element % 2 == 0:
        even_numbers.append(element)

print(even_numbers)

stringInput = input("Enter a character string: ")

def firstLetter(param):
    for char in param:
        if char.isalpha() and len(char) == 1:
            return char
    return None

print(firstLetter(stringInput))

#Dictionaries

carDictionarie = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

