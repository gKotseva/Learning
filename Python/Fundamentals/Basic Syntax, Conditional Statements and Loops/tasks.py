# Task 1:
# Ask the user for their name and print "Hello, <name>!"

name = input('Enter name: ')
print ("Hello, " + name + '!')

# Task 2:
# Ask the user for two numbers and print their sum.

a = int(input('First number: '))
b = int(input('Second number: '))
print(a + b)

# Task 3:
# Ask the user for a number and print whether it is even or odd.

a = int(input('Enter number: '))
if a % 2 == 0: print('Even')
else: print('Odd')

# Task 4:
# Ask the user for a number and print whether it is positive or negative.

a = int(input('Enter number: '))
if a > 0:
    print('Positive')
elif a == 0:
    print('Zero')
else:
    print('Negative')

# Task 5:
# Ask the user for a number and print all numbers from 1 up to that number.

a = int(input('Enter number: '))
for x in range(1, a + 1):
    print(x)

# Task 6:
# Print all numbers from 10 down to 1 using a loop.

for x in range(10, 0, -1):
    print(x)

# Task 7:
# Ask the user for a number and print its multiplication table (from 1 to 10).

a = int(input('Enter number: '))
for x in range(1, 11):
    print(a * x)

# Task 8:
# Print all even numbers between 1 and 50 using a loop.

for x in range(1, 51):
    if x % 2 == 0: print(x)

# Task 9:
# Ask the user for a number N and calculate the sum of numbers from 1 to N.

a = int(input('Enter number: '))
sum = 0
for x in range(1, a + 1):
    sum += x
print(sum)

# Task 10:
# Use a loop to print your name 5 times.

for x in range(5):
    print('Gabi')

# Task 11:
# Ask the user for a word and print each letter on a new line.

a = str(input('Enter word: '))

for x in a:
    print(x)

# Task 12:
# Ask the user for a number and print its square (number * number).

a = int(input('Enter number: '))
print(a * a)

# Task 13:
# Ask the user for their age and print "You are an adult" if 18 or older, otherwise print "You are a minor".

a = int(input('Enter your age: '))
if a >= 18: print('You are an adult')
else: print('You are a minor')


# Task 14:
# Ask the user to enter a number and print "Small" if it's less than 10, "Big" if it's 10 or more.

a = int(input('Enter number: '))
if a >= 10: print('Big')
else: print('Small')

# Task 15:
# Use a while loop to print numbers from 1 to 10.

a = 1

while a <= 10: 
    print(a)
    a += 1

# Task 16:
# Use a while loop to print numbers from 10 down to 1.

a = 10
while a > 0:
    print(a)
    a -= 1


# Task 17:
# Ask the user for a password. Keep asking until they enter "python123".

password = ''
while password != 'python123':
    password = input('Enter password: ')
print('Correct password!')


# Task 18:
# Ask the user for 5 numbers and print their average.

a = int(input('Enter number: '))
b = int(input('Enter number: '))
c = int(input('Enter number: '))
d = int(input('Enter number: '))
e = int(input('Enter number: '))

print((a + b + c + d + e) / 5)

# Task 19:
# Ask the user for a number and print whether it is divisible by 3.

a = int(input('Enter number: '))
if a % 3 == 0:
    print('Divisible by 3')
else:
    print('Not divisible by 3')

# Task 20:
# Ask the user for two numbers and print the larger one.

a = int(input('Enter number: '))
b = int(input('Enter number: '))
if a > b:
    print(a)
else:
    print(b)