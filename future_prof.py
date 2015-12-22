#this program takes three strings
#then print one string in output using random function

import random

profession = []

def future(x):
    i = 0
    while i < 3:
        ques = raw_input("Enter your favourite profession:")
        profession.append(ques)
        i += 1
future(profession)
prof = random.choice(profession)

print "you would be a %s when you grow up" %(prof)

