# Task 1:
# Using list comprehension, create a list of the squares of numbers from 1 to 10.

squares = [x**2 for x in range(1, 11)]

# Task 2:
# From the list nums = [1, 2, 3, 4, 5, 6], create a new list with only the even numbers (list comprehension).

nums = [1, 2, 3, 4, 5, 6]
even = [num for num in nums if num % 2 == 0]

# Task 3:
# Using list comprehension, create a list with "even" or "odd" for each number in range(1, 11).

even_or_odd = ['Even' if num % 2 == 0 else 'Odd' for num in range(1, 11)]

# Task 4:
# Given a list of words, use list comprehension to create a list of their lengths.

words = ['apple', 'banana', 'cherry', 'pineapple']
word_lengths = [len(l) for l in words]

# Task 5:
# Using map(), convert a list of strings into integers: ["10", "20", "30"].

strings = ["10", "20", "30"]
integers = list(map(int, strings))

# Task 6:
# Using map() and lambda, multiply every number in a list by 3.

nums = [1, 2, 3, 4, 5, 6]
multiplied = list(map(lambda x: x*3, nums))

# Task 7:
# Using filter(), keep only negative numbers from a given list.

nums = [1, 2, 3, 4, -5, 6]
negative = list(filter(lambda x: x < 0, nums))

# Task 8:
# Sort a list of numbers in descending order using sorted() and a lambda.

nums = [99, 28, 266, 22, 1, 5]
sorted_list = sorted(nums, key=lambda x: -x)

# Task 9:
# Sort a list of strings alphabetically by their length.

words = ['apple', 'pineapple', 'banana', 'cherry']
sorted_list = sorted(words, key=lambda x: len(x))

# Task 10:
# Remove all occurrences of the number 3 from a list using a loop and remove().

nums = [99, 28, 3, 266, 3, 22, 1, 5, 3]
while 3 in nums:
    nums.remove(3)

# Task 11:
# Given a list, remove the last element using pop() and store the removed value.

nums = [99, 28, 266, 22, 1, 5]
deleted_number = nums.pop()

# Task 12:
# Using append(), create a list and add numbers from 1 to 5 to it.

numbers_list = list()
for x in range(1, 6):
    numbers_list.append(x)

# Task 13:
# Using extend(), merge two lists: [1, 2, 3] and [4, 5, 6].

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
merged_list = list1

# Task 14:
# Reverse a list using the reverse() method.

list1 = [1, 2, 3, 4, 5, 6]
list1.reverse()

# Task 15:
# Swap the first and last elements in a list of at least 3 numbers.

numbers = [1, 2, 3, 4, 5, 6]
numbers[0], numbers[-1] = numbers[-1], numbers[0]

# Task 16:
# Combine two lists using the + operator.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2

# Task 17:
# Extract only unique elements from a list with duplicates using set().

list1 = [1, 2, 3, 4, 5, 6, 2, 5, 3]
unique = list(set(list1))

# Task 18:
# Using list comprehension, create a list of only the first letters of each word in a given list.

words = ['apple', 'pineapple', 'banana', 'cherry']
first_letters = list(l[0] for l in words)

# Task 19:
# Using list comprehension, build a list of all even squares (x**2) for numbers 1 to 20.

even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]

# Task 20:
# Given a list of names, filter out only those that start with the letter 'A' using filter().

words = ['Apple', 'pineapple', 'banana', 'cherry']
sorted_list = list(filter(lambda w: w[0] == 'A', words))