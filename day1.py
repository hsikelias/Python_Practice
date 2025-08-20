# Write a program that asks the user for their age.
# If they are under 13 → print “Child”
# If 13–19 → print “Teen”
# If 20 or older → print “Adult”
"""
age = int(input("What is your age?(in numbers only): "))

if age <13:
    print("You're a child")
elif age >= 20:
    print("You're an adult")
else:
    print("You're a teen")

"""


""" 
# strings

name = input("What is your name?: ")
age = int(input("What is your age?: "))

message = f"Hello {name},next year you will be {age + 1} years old."
print(message)
"""

"""

n1 = int(input("What is your first number?: "))
n2 = int(input("Now, what is your second number?: "))

print(f"The sum of these two numbers is {n1 + n2}")
print(f"The difference of these two numbers is {n1 -n2}")
print(f"The product of these two numbers is {n1 * n2}")
print(f"The quotient of these two numbers is {n1%n2}")

"""

"""

num1 = float(input("Enter a decimal number: "))

int_num = int(num1)
str_num = str(num1)

print(f"Your decimal number,{num1} as integer is {int_num} and {str_num} for string.")

"""
"""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

int_sum = int(num1+num2)
int_dif = int(num1-num2)
int_prod = int(num1*num2)
int_div = int(num1/num2)
int_rem = int(num1%num2)

print(f"Your numbers as int in various arithmetic operations \n add:{int_sum}, dif: {int_dif},prod: {int_prod},div: {int_div}, rem:{int_rem}")
"""
"""
num = int(input("Enter a number to check if it's odd or even: "))

if num % 2 == 0:
    print("Number is even.")
else:
    print("Number is Odd.")    """


"""
print("Please enter your exam scores(0-100): ")
exam1 = int(input("Exam 1 score: "))
exam2 = int(input("Exam 2 score: "))
exam3 = int(input("Exam 3 score: "))

avg_score = round((exam1+exam2+exam3)/3)


if avg_score<70:
    print("F")
elif avg_score <= 89 and avg_score >= 80:
        print("B")
elif avg_score <= 79 and avg_score >=70:
        print("C") 
else: 
    print("A")
"""

num = int(input("Enter a number: "))

if num%3 == 0 and num%5 ==0:
    print("FizzBuzz")
elif num%3 ==0:
    print("Fizz")
elif num%5 ==0:
    print("Buzz")
else:
        print("Number is not divisible by both 3 and 5.")

