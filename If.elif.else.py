# Write a program that asks the user for their age.
# If they are under 13 → print “Child”
# If 13–19 → print “Teen”
# If 20 or older → print “Adult”

age = int(input("What is your age?(in numbers only): "))

if age <13:
    print("You're a child")
elif age >= 20:
    print("You're an adult")
else:
    print("You're a teen")
