# 1. Create a dictionary with keys "name", "age", and "city". Print the value of "city".

task = {"name": 'Gabi', "age": 27, "city": 'Sofia'}
print(task['city'])

# 2. Add a new key "country" to an existing dictionary with any value you choose.

task = {"name": 'Gabi', "age": 27, "city": 'Sofia'}
task['country'] = 'Bulgaria'

# 3. Given a dictionary {"a": 1, "b": 2, "c": 3}, change the value of key "b" to 10.

task = {"a": 1, "b": 2, "c": 3}
task['b'] = 10

# 4. Write a program that checks whether the key "price" exists in a dictionary.

task = {"a": 1, "b": 2, "c": 3, 'price': 0}

if "price" in task:
    print('Price is in the dic')
else: print('Price is not in the dic')

# 5. Given a dictionary of student grades, print all keys (subjects).

task = {'math': 3, 'biology': 5, 'english': 6}
for subject in task.keys():
    print(subject)


# 6. Print all values from a dictionary that contains product prices.

task = {'jeans': 3, 'tops': 5, 'dresses': 6}
for value in task.values():
    print(value)


# 7. Print all key–value pairs from a dictionary that stores car information.

task = {'audi': 2022, 'bmw': 2013, 'volvo': 2017}
for (key, value) in task.items():
    print(f"{key} {value}")

# 8. Given a dictionary {1: "one", 2: "two", 3: "three"}, delete the pair with key 2.

task = {1: "one", 2: "two", 3: "three"}
del task[2]

# 9. Remove the last inserted item from a dictionary.

task = {1: "one", 2: "two", 3: "three"}
task.popitem()

# 10. Create a dictionary representing a student, then add a new key-value pair to it.

task = {'student1': {}}
task['student1'] = {'math': 4, 'english': 5}

# 11. Convert the list ["Peter", "Amy", "John"] into a dictionary where the key is the index and the value is the name.

names = ["Peter", "Amy", "John"]
result = {}

index = 0
for name in names:
    result[index] = name
    index += 1

print(result)

# 12. Count how many times each word appears in the list ["apple", "banana", "apple", "orange", "banana"] using a dictionary.

words = ["apple", "banana", "apple", "orange", "banana"]
counts = {}

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

print(counts)

# 13. Merge two dictionaries into a new one.

task1 = {"a": 1, "b": 2}
task2 = {"c": 3, "d": 4}

merged = task1.copy()
merged.update(task2)

print(merged)

# 14. Create a dictionary that maps numbers 1 to 5 to their squares.

result = {}

for num in range(1, 6):
    result[num] = num * num

print(result)

# 15. Write a program that checks whether a given value exists in a dictionary.

task = {"a": 10, "b": 20, "c": 30}

if 20 in task.values():
    print("Value exists")
else:
    print("Value does not exist")

# 16. Swap the keys and values in a dictionary (values are unique).

original = {"a": 1, "b": 2, "c": 3}
swapped = {}

for key in original:
    value = original[key]
    swapped[value] = key

print(swapped)

# 17. Create a nested dictionary for three students, each containing name and age. Print the age of one student.

students = {
    1: {"name": "Peter", "age": 22},
    2: {"name": "Amy", "age": 21},
    3: {"name": "John", "age": 20}
}

print(students[2]["age"])  # prints Amy's age


# 18. Add a new nested item to an existing nested dictionary.

students = {
    1: {"name": "Peter", "age": 22},
    2: {"name": "Amy", "age": 21}
}

students[3] = {"name": "John", "age": 20}

print(students)

# 19. Iterate through a nested dictionary and print all values inside it.

students = {
    1: {"name": "Peter", "age": 22},
    2: {"name": "Amy", "age": 21}
}

for student_id, info in students.items():
    for key, value in info.items():
        print(value)

# 20. Use dictionary comprehension to create a dictionary where keys are letters in a string and values are how many times each letter appears.

text = "banana"
letter_count = {letter: text.count(letter) for letter in text}

print(letter_count)