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

def mixed_sum(arr):
    return sum(int(num) for num in arr)

result = mixed_sum(['5', '0', 9, 3, 2, 1, '9', 6, 7])
print(result) 

day = int(input("Choice a number sir : "))
def whatDayIsIt(numberDay):
    if numberDay == 1:
        print("Sunday")
    elif numberDay == 2:
        print("Monday")
    elif numberDay == 3:
        print("Tuesday")
    elif numberDay == 4:
        print("Wednesday")
    elif numberDay == 5:
        print("Thursday")
    elif numberDay == 6:
        print("Friday")
    elif numberDay == 7:
        print("Saturday")
    

whatDayIsIt(day)


def summation(number):
    return sum(range(1, number + 1))

result1 = summation(2)
print(result1)

result2 = summation(8)
print(result2)


def count_Vileplume(num):
    return ''.join(f"{i} Vileplume..." for i in range(1, num + 1)) +" Vileplume use sleeping powder"

result = count_Vileplume(3)
print(result)


def final_grade(exam_grade, completed_projects):
    if exam_grade > 90 or completed_projects > 10 :
        return 100
    if exam_grade> 75 and completed_projects >= 5:
        return 90
    if exam_grade > 50 and completed_projects >= 2:
        return 75
    else:
        return 0
    
print(final_grade(91, 0))
print(final_grade(9, 11))
print(final_grade(76, 5))
print(final_grade(75, 5))
print(final_grade(9, 2))

