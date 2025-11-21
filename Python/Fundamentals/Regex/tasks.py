import re

# 1. Check if the string starts with "Hello" using regex.
text = 'Hello from Python!'
result = re.search(r"^Hello", text)
print(result)


# 2. Find all digits in the string "My phone is 12345 and zip is 67890".
text = "My phone is 12345 and zip is 67890"
result = re.findall(r"\d", text)
print(result)


# 3. Check if the string ends with ".com".
text = "example.com"
result = re.search(r"\.com$", text)
print(result)


# 4. Find all words that start with a capital letter in the sentence.
text = "My friend Peter Went To London"
result = re.findall(r"\b[A-Z][a-zA-Z]*\b", text)
print(result)


# 5. Replace all digits in the string with "*".
text = "I have 2 cats and 3 dogs."
result = re.sub(r"\d", "*", text)
print(result)


# 6. Split the string "apple,banana;orange grape" by commas, semicolons, or spaces.
text = "apple,banana;orange grape"
result = re.split(r"[,; ]", text)
print(result)


# 7. Check if a string contains only letters (a–z, A–Z).
text = "HelloWorld"
result = bool(re.fullmatch(r"[A-Za-z]+", text))
print(result)


# 8. Find all occurrences of "cat" or "dog" in a given sentence.
text = "The cat chased the dog while another cat watched the dog."
result = re.findall(r"cat|dog", text)
print(result)


# 9. Extract the first number from the string "Order number: 5487, date: 2024".
text = "Order number: 5487, date: 2024"
result = re.search(r"\d+", text)
print(result.group())


# 10. Check if a string contains exactly 5 digits in a row.
text = "My code is 12345."
result = bool(re.search(r"\b\d{5}\b", text))
print(result)


# 11. Validate if a string is a valid email (simple version).
text = "test@example.com"
result = bool(re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}", text))
print(result)


# 12. Find all sequences of one or more spaces in a string.
text = "This   sentence  has   many spaces."
result = re.findall(r"\s+", text)
print(result)


# 13. Replace multiple spaces with a single space.
text = "This   sentence  has   many spaces."
result = re.sub(r"\s+", " ", text)
print(result)


# 14. Check if a password contains at least one digit.
password = "Passw0rd"
result = bool(re.search(r"\d", password))
print(result)


# 15. Check if a password contains at least one uppercase and one lowercase letter.
password = "PassWord"
result = bool(re.search(r"[A-Z]", password) and re.search(r"[a-z]", password))
print(result)


# 16. Extract all three-letter words from "The fox ran far and was sly".
text = "The fox ran far and was sly"
result = re.findall(r"\b[a-zA-Z]{3}\b", text)
print(result)


# 17. Check if a string contains only numbers and letters (no symbols).
text = "Hello123"
result = bool(re.fullmatch(r"[A-Za-z0-9]+", text))
print(result)


# 18. Find all non-digit characters in a string.
text = "A1B2C3D4"
result = re.findall(r"\D", text)
print(result)


# 19. Match any word that ends with "ing".
text = "I am running and jumping while singing."
result = re.findall(r"\b\w+ing\b", text)
print(result)


# 20. Using grouping: extract the area code and the number from "Phone: (359) 888-1234".
text = "Phone: (359) 888-1234"
result = re.search(r"\((\d+)\)\s+(\d+-\d+)", text)
print(result.group(1), result.group(2))