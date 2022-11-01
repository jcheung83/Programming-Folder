num1 = 42 #int number data type
num2 = 2.3 #float number data type
boolean = True #boolean data type
string = 'Hello World' #string data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #composite list initialization
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #composite dictionary initialization
fruit = ('blueberry', 'strawberry', 'banana') #composite tuple initialization
print(type(fruit)) #composite tuple type check and log statement
print(pizza_toppings[1]) #composite list access one value and log statement
pizza_toppings.append('Mushrooms') #composite list add vlue
print(person['name']) #composite dictionary access one value and log statement
person['name'] = 'George' #composite dictionary change value
person['eye_color'] = 'blue' #composite dictionary add value
print(fruit[2]) #composite tuple access one value

if num1 > 45: #conditional if
    print("It's greater") #log statement
else: #condisional else
    print("It's lower") #log statement

if len(string) < 5: #conditional if and length check
    print("It's a short word!") #log statement
elif len(string) > 15: #conditional else if and length check
    print("It's a long word!") #log statement
else: #conditional else
    print("Just right!") #log statement

for x in range(5): #for loop start
    print(x) #log statement
for x in range(2,5): #for loop start
    print(x) #log statement
for x in range(2,10,3): #for loop start
    print(x) #log statement
x = 0 #variable declaration
while(x < 5): #while loop start
    print(x) #log statement
    x += 1 #while loop increment

pizza_toppings.pop() #composite list delete value
pizza_toppings.pop(1) #composite list add value

print(person) #log statement
person.pop('eye_color') #composite dictionary delete value
print(person) #log statement

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #conditional if 
        continue #for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional if
        break #for loop break

def print_hello_ten_times(): #function definition 
    for num in range(10): #for loop start
        print('Hello') #log statement

print_hello_ten_times() #function call

def print_hello_x_times(x): #function definition
    for num in range(x): #for loop start
        print('Hello') #log statement

print_hello_x_times(4) #function call, with argument

def print_hello_x_or_ten_times(x = 10): #function definition
    for num in range(x): #for loop start
        print('Hello') #log statement

print_hello_x_or_ten_times() #function call, no argument
print_hello_x_or_ten_times(4) #function call, with argument


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)