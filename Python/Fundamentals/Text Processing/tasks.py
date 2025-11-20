# 1. Assign a multiline string to a variable and print it.

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(text)

# 2. Convert a floating-point number to a string and print its type.

number = 5.3
text = str(number)

print(type(text))

# 3. Split the string "hello world from python" by spaces and print the resulting list.

text = 'hello world from python'
list = text.split(' ')

print(list)

# 4. Merge two strings using the + operator and print the result.

str1 = 'string1'
str2 = 'string2'
merged = str1 + str2

print(merged)

# 5. Repeat the string "Hi!" five times and print the result.

text = 'Hi!'

print(text * 5)

# 6. Format a sentence using the % operator with two words: "coffee" and "milk".

word1 = 'coffee'
word2 = 'milk'
result = "%s and %s" % (word1, word2)

print(result)

# 7. Format a sentence using the .format() method with two variables of your choice.

word1 = 'coffee'
word2 = 'milk'
result = "{} and {}".format(word1, word2)

print(result)

# 8. Format a sentence using an f-string with three variables.

word1 = 'coffee'
word2 = 'milk'
word3 = 'watter'
result = f"{word1}, {word2}, {word3}"

print(result)

# 9. Extract the last 4 characters from the string "Programming".

text = 'Programming'
result = text[slice(-4, len(text))]

print(result)

# 10. Check if the user input is a digit and print a message.

user_input = input("Enter something: ")

if user_input.isdigit():
    print("You entered a digit.")
else:
    print("This is NOT a digit.")

# 11. Ask the user for a letter and check if it is uppercase.

user_input = input("Enter letter: ")

if user_input.isupper():
    print("You entered a capital letter.")
else:
    print("This is NOT a capital letter.")

# 12. Convert the string "python is fun" to uppercase and print it.

text = 'python is fun'
result = text.upper()

print(result)

# 13. Remove leading and trailing spaces from the string "   clean me   " and print the result.

text = '   clean me   '
result = text.strip()

print(result)

# 14. Replace all occurrences of "cat" with "dog" in a sentence.

text = 'The curious cat carefully chased another cat across the garden, while three tiny kittens watched the catlike creature from the cat-covered porch'
result = text.replace('cat', 'dog')

print(result)

# 15. Replace only the first two occurrences of "test" in the string "test test test test".

text = "test test test test"
result = text.replace("test", "REPLACED", 2)

print(result)

# 16. Split the string "apple-banana-orange" using "-" and print the last element.

text = "apple-banana-orange"
result = text.split('-')

print(result[-1])

# 17. Use slicing to get every second character from the string "abcdefgh".

text = "abcdefgh"
result = text[slice(0, len(text), 2)]

print(result)

# 18. Count how many times the letter "a" appears in the string "bananas".

text = "bananas"
result = text.count('a')

print(result)

# 19. Check if the string "Hello123" contains only letters using an appropriate string method.

text = 'Hello123'

if text.isalpha():
    print("Only letters")
else:
    print("Not only letters")

# 20. Given a string, create a new string where the first letter is uppercase and the rest are lowercase.

text = 'bananas'
result = text.capitalize()

print(result)