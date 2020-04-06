# Review01
"""
intVal = 10
floatVal = 6.8
boolVal = False
print(boolVal)
boolVal = True
print(intVal)
print(floatVal)
print(boolVal)
"""

# Review02
import random

"""
# THIS IS A SINGLE LINE COMMENT

"""
"""
THIS IS
A MULTIPLE
LINE COMMENT
"""
"""
add = 6 + 89
sub = 76 - 12
div = 100 / 5
prod = 27 * 13
operators1 = 2
operators2 = 2
operators3 = 2
operators1 **= 2
operators2 //= 0.5
operators3 %= 1
print(add, sub, div, prod)
print(operators1, operators2, operators3)
"""

# Review03
"""
print ('singleQuotes')
print ("doubleQuotes")
print ("This should be \"in quotes\".")
String = "Alligator"
print (String[5])
print (String[:4])
print (String[5:8])
print (String[8:])
"""

# Review04
"""
print(len("Manchester United"))
print(str(12345)[2])
print("albania".upper())
print("BELGIUM".lower())
"""

# Review05
"""
name = input("What is your name?")
print("Your name is " + "%s" %(name))

# Review06
# F, T, F, F, F, T, T, T, F, F, T, T.

# Review07
# T, T, F, T.
"""

# Review08
"""
name = input("Please insert your name: ")
lenname = len(name)
if lenname < 4:
    print("Your name is less than 4 characters.")
elif 4 <= lenname < 10:
    print("Your name is at least 4 characters and less than 10 characters.")
else:
    print("Your name is very long.")
"""

# Review09
"""
def first():
    print('this is a function')
def second(int):
    return int * 2
def third(def2, int2):
    return second(def2) * int2
def forth(a, b, c):
    print(third(second(a), b) * c)

first()
forth(7, 4, 2)
"""

# Review10
"""
import random
from random import randint
from math import *
print(randint(5, 10))
print(factorial(4))
print(random.random())
"""

# Review11
"""
print(abs(-76))
print(type(-72.64))
print(max(1, 9, 2, 3, 20))
print(min("bca", "cde", "fgh"))
"""

# Review12
"""
list = [1, 2, 3, 4, 4, 6]
print(list)
list[4] = 5
print(list)
list.append(7)
print(list)
print(list[:4])
print(list[3:6])
print(list[6:])
print(list.index(7))
list.insert(0, 0)
print(list)
list.remove(3)
print(list)
print(list.pop(6))
print(list)
"""

# Review13
"""
tupleware = (1, 2, 3, 4)
int2 = tupleware[1]
print(int2)
print(tupleware[:2])
print(tupleware[1:3])
print(tupleware[2:])
for int in tupleware:
    print(int)
"""

# Review14
"""
emp = {}
emp[1] = "Matheus"
emp[2] = "Mark"
emp[3] = "Luke"
print(emp)
print(len(emp))
print(emp[3])
emp[3] = "John"
print(emp[3])
del emp[1]
print(emp)
"""

# Review15
"""
strings = ["just", "do", "it"]
def takelist(l):
    print(l[1])
    print("frog" + l[2])
    l.remove(l[0])
    print(l)
takelist(strings)
"""

# Reviwe16
"""
integers = [2, 4, 6, 8]
def printelem(a):
    for i in a:
        print(i)
range1 = range(3)
range2 = range(2, 5)
range3 = range(2, 13, 5)
def lists(r1, r2, r3):
    sum = []
    for i in range(0, max(len(r1), len(r2), len(r3))):
        sum.append(r1[i] + r2[i] + r3[i])
    return sum

def printlists(ll):
    for iten in ll:
        for val in iten:
            print(val)
printlists([[1,2], [0, 1], [3, 4]])
printelem(integers)
print(lists(range1, range2, range3))
"""

# Review17
"""
from random import randint
counter = 5
while counter < 10:
    print(counter)
    if counter == 7:
        print("counter is equal to 7")
        break
    counter = randint(5, 10)
else:
    print("counter is equal to 10")
"""

# Review18
"""
string = "Brian"
intlist = [11, 22, 33, 44]
dict = {"that": "isso", "is": "é", "crazy": "loucura"}
for l in range(0, len(string)):
    print(string[l])
for int in range(0, len(intlist)):
    if int == len(intlist) - 1:
        print(intlist[int], end="")
        break
    print(intlist[int], end=",")
print("")
for val in dict:
    print(dict[val], end=(""))
    print("")
integers = [23, 12, 57, 36]
for in1, in2 in zip(intlist, integers):
    print(max(in1, in2))
for int in intlist:
    print(int, end="_")
else: print(99)
"""

# Reviwe19
"""
print([a for a in range(1, 10, 2)])
print([b for b in range(3, 8)])
print([c for c in range(1, 10) if c % 2 != 0])
print([d for d in range(0, 100) if d > 2 and d < 8]) #or ...range(8) if d > 4])
"""

# Review20
"""
toSlice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(toSlice[1:18:2])
print(toSlice[::5])
print(toSlice[11:1:-3])
print(toSlice[::-1])
"""

# Review21
'''
from random import randint
inpint = input("Please insert a integer to be divide by a random integer:")
randint = randint(0, 5)
print('The rendom integer is {}'.format(randint))
try:
    inpint = int(inpint)
    if randint > inpint:
        print("Random integer is bigger than that you inserted: {} > {}".format(randint, inpint))
    elif randint == inpint:
        print('The integer inserted is equal to the integer generated {} = {}'.format(randint, inpint))
    else:
        print('The integer randomly generated is lesser than that you inserted: {1} > {0}'.format(randint, inpint))
except:
    print('You must insert a integer, run the program again!')
'''
