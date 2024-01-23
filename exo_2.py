age = 32 
age += 10
divAge = age/7
textDiv = age  , "divisé par 7 = ", divAge
restDiv = divAge
expDiv = restDiv ** 3



try:

    inputInteger = input("enter integer ")
    useInputInteger = int(inputInteger)
    
    print(f"Enterd value: {useInputInteger}")
    print(f"Type of entered: {type(useInputInteger).__name__}")
except ValueError:
    print("Error: Please enter a valid integer")
    
bottlesOfMilk = 0.45
bottleOfRawCider = 3.85
bagOfFlour = 0.90
paquetOfButter = 0.77
jarOfNutella = 1.87

orderPrice = bottleOfRawCider + bottlesOfMilk + bagOfFlour + paquetOfButter + jarOfNutella

allowance_money = 7.84
price = orderPrice
Available_money = allowance_money - price

if allowance_money > orderPrice:
    print(f"You have spent {format(orderPrice, '.02f')} € you left {allowance_money - price} €")

elif orderPrice > allowance_money:
    print(f"sorry you're missing {format(orderPrice - allowance_money, '.02f')} €")
elif orderPrice > allowance_money and allowance_money - orderPrice == 0:
    print("Vous êtes fauché")

print(format(orderPrice, '.02f'))



#exo 7
def compareValues(value1, value2):
   
    
    if value1 > value2:
        print(f"Value 2 is inferior in value 1")
    if value1 < value2:
        print(f"Value 1 is inferior in value 2")
    elif value1 == value2:
        print("The values are equal")
        
        
        
value1 = input("Enter first value ")
value2 = input("Enter second value ")
compareValues(value1, value2)

def compareChain(chain1, chain2):
    
    if len(chain1) > len(chain2):
        print(f"Chain 2 ({len(chain2)} characters) is inferior in chain 1 ({len(chain1)} characters)")
    if len(chain1) < len(chain2):
        print(f"Chain  1 ({len(chain1)} characters) is inferior in chain 2 ({len(chain2)} characters)")
    elif len(chain1) == len(chain2):
        print(f"The values are equal ({len(chain1)} characters)")
        
chain1 = input("Enter first chain ")
chain2 = input("Enter second chain ")
compareChain(chain1, chain2)


#exo 12
studentsTuring = ["Redouane", "Justine", "Ruben", "Edouard"]
name = "Julie"

print(f"Current list {studentsTuring}") 

def nameInList():
    if name in studentsTuring:
        print("this name is in the list")
    else:
        print(f"{name} is not in the list")
        response =  input(f"Do you want to add {name} to the list ? (type yes or no) ")
        
        if response.capitalize() == "Yes" or response.capitalize() == "Oui":
            studentsTuring.append(name)
            print(f"{name} is add in to the list")
        if response.capitalize() == "no" or response.capitalize() == "no":
            print(f"{name} is not add in to the list")
            
            
nameInList()
print(studentsTuring) 

radius = 10
pi = 3.14
volume = (4/3) * pi * radius**3
print(f"the volume of the sphere with radius {radius} is : {volume}")
        
    
    