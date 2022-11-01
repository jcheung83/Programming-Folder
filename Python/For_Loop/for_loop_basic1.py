# Basic - print all integers 0-150
for i in range (151):
    print(i)

# Multiples of 5 - from 5 to 1,000
for i in range (5, 1001, 5):
    print(i)

# Counting, the Dojo Way - Print integers 1 to 100. 
# If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo". 
for i in range (1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
x = 0
for i in range (500001):
    if i % 2 == 1:
        x += i
print(x)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
i = 2018
while i > 0:
    print(i)
    i -= 4

# Flexible Counter - Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the integers that are a multiple of 
# mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on 
# successive lines)

lowNum = 2
highNum = 1923
mult = 8

for i in range (lowNum, highNum + 1):
    if i % mult == 0:
        print (i)