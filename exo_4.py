translate_dictionarie = {
    "ordinateur " : "computer",
    "souris " : "mouse",
    "clavier " : "keyboard",
    "écran " : "screen",
    "soleil " : "sun"
}

translate_dictionarie["lumière "] = "light"

for word in translate_dictionarie :
    print(f"{word}: {translate_dictionarie[word]}")
    
sentence = "I am the master of the world"
sentence_list = sentence.split()
universal_number = "The_universal_number_is_42"
replace_underscore = universal_number.replace("_", " ")
##SPIDER-MAN IS NOT TONY PARKER, IS PETER PARKER !
heroes = {"Superman": "Clark Kent", "Batman": "Bruce Wayne", "Spiderman": "Tony Parker"}
value_dictionarie = list(heroes.values())
keys_dictionarie = list(heroes.keys())

import random

products = {
    "Laser sword ": 229.0,
    "Mitendo DX " : 127.30,
    "Linux cushion " : 74.50,
    "Goldorak briefs " : 29.90,
    "Nextpresso station " : 184.60
}

price_product = products.values()

for price in price_product:
    print(f"{price} €")
    
sum_price_product = sum(products.values())
print(sum_price_product)

random_product = random.choice(list(products.keys()))
deleted_item = products.pop(random_product, None)

print("updated list : ", products, random_product, deleted_item, "€ is deleted")




