# Task 1:
# Create a list of 5 fruits and print the second and the last fruit.

list = ['apple', 'banana', 'orange', 'kiwi', 'cherry']
print(list[1])
print(list[-1])

# Task 2:
# Create an empty list and fill it with 4 numbers of your choice, then print the list.

list = []
list.append(1)
list.append(4)
list.append(15)
list.append(5)
print(list)

# Task 3:
# Create a string with several words separated by spaces and turn it into a list. Print the number of elements.

text = 'cat dog parrot'
list = text.split(' ')
print(len(list))

# Task 4:
# Combine a list of 4 colors into one string separated by dashes and print it.

colors = ['orange', 'purple', 'black', 'white']
print('-'.join(colors))

# Task 5:
# Create a list of 5 cities. Remove the city at index 2 and print the updated list.

cities = ['Sofia', 'Madrid', 'Amsterdam', 'Rome', 'Plovdiv']
cities.remove(cities[2])
print(cities)

# Task 6:
# Create a list of numbers [10, 20, 30, 40, 50]. Check if 30 is in the list and print an appropriate message.

list = [10, 20, 30, 40, 50]

if 30 in list: 
    print('30 is in the list')
else:
    print('30 is not in the list')


# Task 7:
# Create a list of names and check if your name is not in the list. If not, add it and print the list.

names = ['Mariya', 'Kameliya', 'Plamena', 'Martin']

if 'Gabriela' not in names:
    names.append('Gabriela')
    print(names)

# Task 8:
# Create a list of words from a sentence. Print the first and last word in the list.

list = ["Hello", "from", "Python", "learning", "experience"]
print(list[0])
print(list[-1])

# Task 9:
# Create a list of 5 numbers. Remove the smallest number and add a new one at the end.

numbers = [83, 44, 28, 92, 93]
small = numbers[0]

for x in numbers:
    if x < small: 
        small = x

numbers.remove(small)
numbers.append(62)
print(numbers)

# Task 10:
# Create a list of 5 colors and print only the first three.

colors = ['orange', 'purple', 'black', 'white', 'pink']

for i in range(len(colors)):
    if i == 3: break
    print(colors[i])

# Task 11:
# Create a list of your favorite movies and print each one on a new line.

movies = ['Southpaw', 'The Green Mile', 'Enemy at the Gates']

for x in movies:
    print(x)

# Task 12:
# Create a list of numbers. If the number 5 is in the list, remove it; otherwise, add it. Print the final list.

numbers = [1, 2, 6, 3, 10, 23]

if 5 in numbers: numbers.remove(5)
else: numbers.append(5)

print(numbers)

# Task 13:
# Create two lists of equal length and combine them into a single list containing all elements.

list1 = ['apple', 'pear', 'kiwi']
list2 = ['black', 'white', 'gold']

final_list = list1 + list2
print(final_list)

# Task 14:
# Create a list with mixed data types and print the type of the first and last element.

list = [1, 'text', ['1', '2', '3'], {'name': 'Gabriela', 'age': 27}]
print(type(list[0]))
print(type(list[-1]))

# Task 15:
# Create a list of 6 animals. Replace the third animal with a new one.

list = ['cat', 'dog', 'parrot', 'snake', 'bear', 'bunny']
list[2] = 'mouse'

# Task 16:
# Create a list of 10 numbers. Print the middle element.

numbers = [22, 57, 29, 91, -1, 7, 83, 20, 773, 201]
print(numbers[(len(numbers) // 2)])

# Task 17:
# Create a list of car brands. If a brand “Audi” exists in the list, print “Audi is present”; otherwise print “Audi not found”.

brands = ['Skoda', 'Seat', 'Renault', 'BMW']
if 'Audi' in brands: print('Audi is present')
else: print('Audi not found')

# Task 18:
# Create a list of numbers and print how many elements it contains.

numbers = [22, 57, 29, 91, -1, 7, 83, 20, 773, 201]
print(len(numbers))

# Task 19:
# Create a list of 5 countries and sort them alphabetically. Print the sorted list.

countries = ['Bulgaria', 'Netherlands', 'USA', 'Italy', 'Spain']
print(sorted(countries))

# Task 20:
# Create a list of words. Turn it into a single string where the words are separated by spaces, and print the result.

words = ['Hello', 'from', 'Python', 'learning']
print(' '.join(words))
