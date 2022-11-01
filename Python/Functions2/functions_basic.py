# Countdown - Create a function that accepts a number as an input. Return a new list that 
# counts down by one, from the number (as the 0th element) down to 0 (as the last element).

# number = input("Please enter a number: ")
# i = int(number)
# while i >= 0:
#     print(i)
#     i -= 1

# Print and Return - Create a function that will receive a list with two numbers. Print the 
# first value and return the second.

def print_and_return(a):
    print(a[0])
    return a[1]
example = [99,50]
print(print_and_return(example))

# First Plus Length - Create a function that accepts a list and returns the sum of the first 
# value in the list plus the list's length.

def first_plus_length(a):
    sum = a[0] + len(a)
    return sum
example = [1,2,3,4,5]
print(first_plus_length(example))

# Values Greater than Second - Write a function that accepts a list and creates a new list 
# containing only the values from the original list that are greater than its 2nd value. Print 
# how many values this is and then return the new list. If the list has less than 2 elements, 
# have the function return False

def values_greater_than_second(a):
    if len(a) < 2:
        return False
    else:
        b = []
        print(len(a))
        for i in range(len(a)):
            if  a[i] > a[1]:
                b.append(a[i])
        return b
        
example = [1,2,3,4,5,6,1,7,8,9,1,10]
example2 = [3]
print(values_greater_than_second(example))
print(values_greater_than_second(example2))

# This Length, That Value - Write a function that accepts two integers as parameters: size and 
# value. The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.

def this_length_that_value(size, value):
    a = []
    for i in range(size):  
        a.append(value)
    return a

print(this_length_that_value(1,1))
print(this_length_that_value(100,10))