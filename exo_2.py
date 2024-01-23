age = 32 
age += 10
divAge = age/7
textDiv = age  , "divisé par 7 = ", divAge
restDiv = divAge
expDiv = restDiv ** 3



try:

    inputInteger = input("enter integer")
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