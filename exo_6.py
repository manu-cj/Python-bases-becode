def HelloSir(username):
    if username == "":
        print("Hello Anonymous")
    elif username != "":
        print(f"Hello {username}")
        if username == "Steve Jobs":
            print("What ! You are Steve Jobs ?")
    
    
name = input("Whats your name sir ? ")
HelloSir(name)

def sum_of_students(students):
    allStudents = sum(len(group) for group in students)
    print(f"{allStudents} students in the list")

sum_of_students([["Jean", "Alice", "Edwige", "Peter", "James"],
               ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]])


def is_divisible(n, x, y):
     return n % x == 0 and n % y == 0
    
print(is_divisible(3, 3, 3))

def name_to_initials(full_name):
    if full_name == "":
        full_name = "Mr Anonimous"
    words = full_name.split()
    initials = '.'.join(word[0] for word in words)

    return initials
print(name_to_initials(name))

def sum_of_positives(numbers):
    return sum(num for num in numbers if num > 0)

numbers = [1, -4, 7, 12]
result = sum_of_positives(numbers)
print(result)

