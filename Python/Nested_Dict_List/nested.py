x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15
x[1][0] = 15
# print (x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
# print (students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
# print (sports_directory)

# Change the value 20 in z to 30
z[0]["y"] = 30
# print (z)

# Iterate Through a List of Dictionaries
def iterateDictionary(students):
    for dict in students:
        printText=""
        for key in dict:
            printText += key + " - " + dict[key]
            if (key == "first_name"):
                printText += ", "
        print(printText)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 

# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2("first_name", students)
iterateDictionary2('last_name', students)

# Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    printText=""
    for key in some_dict:
        printText += "\n" + key.upper() + ": " + str(len(some_dict[key]))
        for val in some_dict[key]:
            printText += "\n" + val
    print(printText)
    
printInfo(dojo)
