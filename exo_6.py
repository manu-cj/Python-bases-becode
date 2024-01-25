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
    # Your code
    return bool
