# Task 1:
# Create a function called say_hello that prints “Hello, World!”.
# Call it once.

def say_hello():
    print("Hello, World!")

say_hello()

# Task 2:
# Create a function called greet that takes a name as a parameter and prints “Hello, <name>!”.

def greet(name):
    print(f"Hello, {name}!")

greet('Gabi')

# Task 3:
# Create a function called add that takes two numbers and prints their sum.

def add(a, b):
    print(a+b)

add(1, 6)

# Task 4:
# Create a function called multiply that takes two numbers and returns their product.
# Print the returned result.

def multiply(a, b):
    return a * b

print(multiply(1, 6))

# Task 5:
# Create a function called square that returns the square of a given number.

def square(num):
    return num ** 2

# Task 6:
# Create a function called even_or_odd that takes a number and prints whether it is even or odd.

def even_or_odd(a):
    if a % 2 == 0: print('Even')    
    else: print('Odd')

even_or_odd(6)

# Task 7:
# Create a function called average that takes three numbers and returns their average.

def average(a, b, c):
    result = (a + b + c) / 3
    return result

print(average(6, 7, 2))

# Task 8:
# Create a function called get_max that takes three numbers and returns the largest one.

def get_max(a, b, c):
    result = max(a, b, c)
    return result

print(get_max(6, 7, 2))

# Task 9:
# Create a function called repeat_text that takes a string and a number and prints the string that many times.

def repeat_text(string, number_of_times):
    for x in range(number_of_times):
        print(string)

repeat_text('Gabi', 5)

# Task 10:
# Create a function called full_name that takes a first name and a last name and returns them combined as a single string.

def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

full_name('Gabi', 'Kotseva')

# Task 11:
# Create a function called area_of_rectangle that takes width and height (default = 1) and returns the area.

def area_of_rectangle(width, height=1):
    return width * height

# Task 12:
# Create a function called welcome that takes two parameters: name and language.
# If language is 'en' print “Hello, <name>”, if 'es' print “Hola, <name>”, otherwise print “Hi, <name>”.

def welcome(name, language):
    if language == 'en': print(f"Hello, {name}")
    elif language == 'es': print(f"Hola, {name}")
    else: print(f"Hi, {name}")
    
welcome('Gabriela', 'es')

# Task 13:
# Create a function called factorial that takes one number and returns its factorial (without using math library).

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Task 14:
# Create a function called find_min that takes a list of numbers and returns the smallest one.

def find_min(list):
    result = min(list)
    return result

print(find_min([6, 7, 2]))

# Task 15:
# Create a function called is_in_list that takes a list and an element, and returns True if the element is in the list.

def is_in_list(lst, element):
    return element in lst

is_in_list(['apple', 'cherry'], 'kiwi')

# Task 16:
# Create a function called count_vowels that takes a string and returns how many vowels it contains.

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Gabriela"))

# Task 17:
# Create a function called reverse_string that returns the reversed version of a given string.

def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))

# Task 18:
# Create a function called sum_list that takes a list of numbers and returns the sum.

def sum_list(list):
    result = sum(list)
    return result

print(sum_list([6, 7, 2]))

# Task 19:
# Create a lambda function that takes two numbers and returns their difference. Print the result of calling it.

difference = lambda a, b: a - b
print(difference(10, 4))

# Task 20:
# Create a lambda function that takes a name and returns a greeting string like “Hi, <name>!”.
# Call and print it with your name.

greet = lambda a: f'Hi, {a}!'
print(greet('Gabi'))
