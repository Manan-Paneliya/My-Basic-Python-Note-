import random

n1 = random.randint(1,10)  # it return random from 1 to 10 number
print(n1)
n2 = random.randrange(1,10)  # it return random number from 1 to 9 , it does not consider 10
print(n2)
s = [10,20,30,40,50,60]
random.shuffle(s)   # it shuffle the items of list
print(s)
f = random.random()   # it returns a random float value between 0 and 1
print(f)
fb = random.uniform(4,8)  # it return a random float value between given two numbers
print(fb)
