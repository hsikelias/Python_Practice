# Randomisaion and Python Lists

import random
"""
rando = random.random()
print(rando)"""


"""
random_float = random.uniform(5,6)
print(random_float) 

"""
"""
            #0        #1       #2        #3
fruits = ["apple", "corn", "orange", "tomato"]
            #-4      #-3      #-2         #-1   
print(fruits[-4]) """

"""
Lottery Simulator

Generate 6 random numbers between 1 and 49 (no repeats).

Store them in a list and print them sorted.

"""
"""
# convering a list into string

ran_num = random.sample(range(1,50),6)
result = ", ".join(str(item) for item in ran_num)
print(result)

"""

# for loop
"""
fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + "pear")
    print(fruit)

"""
"""
while True:
    for item in fruits:
        print(fruits) 
"""

#loops with range

for number in range(5,11):
    print(number)

