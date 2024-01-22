name = "Alan Turing"
age = 42
person = [name, age,  "mathematician"]
text = "Hello, my name is {0}, I am {1} years old and I am a {2}.".format(*person)
age_type = type(age)
print(age_type)

