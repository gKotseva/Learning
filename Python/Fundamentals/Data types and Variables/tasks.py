# Task 1:
# Create an integer variable and print its type using type().

a = int(2)
print(type(a))

# Task 2:
# Create a float variable and check if it is an instance of float using isinstance().

a = float(2.2)
print(isinstance(a, float))

# Task 3:
# Create a string variable and print its length using len().

a = str("Hello")
print(len(a))

# Task 4:
# Create a boolean variable and print its value.

a = 2 ==2
print(a)

# Task 5:
# Create a list containing 5 items of different data types and print it.

a = [1, '1', 1.2, True, {'1', '2', '3'}]
print(a)

# Task 6:
# Create a tuple with 4 items and print the first item.

a = ('a', 'b', 'c', 'd')
print(a[0])

# Task 7:
# Create a set with 3 items and print it.

a = {"a", "b", "c"}
print(a)

# Task 8:
# Create a dictionary with keys "name" and "age" and print the value of "name".

a = {"name": 'Gabi', "age": 27}
print(a['name'])

# Task 9:
# Add a new key-value pair to the dictionary with key "city" and any value.

a = {"name": 'Gabi', "age": 27}
a['city'] = 'Sofia'

# Task 10:
# Change the value of the "age" key in the dictionary to a new number.

a = {"name": 'Gabi', "age": 27}
a['age'] = 26

# Task 11:
# Check if a variable is None using "is None" and print a message.

a = None
print(a is None)

# Task 12:
# Check if a variable is None using "== None" and print a message.

a = None
print(a == None)

# Task 13:
# Create a list of numbers and calculate its length using len().

a = [1, 2, 3, 4, 5]
print(len(a))

# Task 14:
# Create a string with your full name and check if it is an instance of str.

a = 'Gabriela Kotseva'
print(isinstance(a, str))

# Task 15:
# Create a dictionary of 3 items and print all its keys.

a = {"name": 'Gabriela', "age": 27, "city": 'Sofia'}

for x in a:
    print(x)

# Task 16:
# Create a tuple of 5 numbers and print the last number.

a = (1, 2, 3, 22, 7)
print(a[-1])

# Task 17:
# Create a list of 5 numbers and print the sum of the first and last number.

a = [22, 5, 92, 33, 49]
print(a[0] + a[-1])

# Task 18:
# Create an integer variable and a float variable, then print their types.

a = 1
b = 1.1

print(type(a))
print(type(b))

# Task 19:
# Create a boolean variable with value False and check if it is an instance of bool.

a = False
print(isinstance(a, bool))

# Task 20:
# Create a list, tuple, set, and dictionary, then print the type of each.

a = ['1', '2', '3']
b = ('1', '2', '3')
c = {'1', '2', '3'}
d = {'number1': '1', 'number2': '2', 'number3': '3'}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
