stringVar = "toto"
numberVar = 10

unicodeString = [ord(char) for char in stringVar]
floatNumber = float(numberVar)

reversedString = stringVar[::-1]
reversedNumber = float(str(numberVar)[::-1])

print(reversedNumber)