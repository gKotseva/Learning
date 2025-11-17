# 1. Create a class called Person that stores a name and age. Create an object and print its attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

me = Person('Gabi', 27)
print(me.name)
print(me.age)

# 2. Create a class Dog with attributes name and breed. Create two dogs and print their names.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog('Kodi', 'Yorkshire Terrier')
dog2 = Dog('Reya', 'Staffordshire Bull Terrier')
print(dog1.name)
print(dog2.name)

# 3. Create a class Car that stores brand, model, and year. Create a method that returns the car's full description.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def full_description(self): 
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

car1 = Car('Audi', 'A3', 2001)
print(car1.full_description())


# 4. Create a class Student with attributes name and grades (a list). Add a method to calculate the average grade.

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = list(grades)
    
    def average_grade(self): 
        return sum(self.grades) / len(self.grades)

student1 = Student('Gabi', [4, 6, 3, 2, 5, 6, 4])
print(student1.average_grade())

# 5. Create a class Rectangle with width and height. Add a method that returns its area.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self): 
        return self.width * self.height

rectangle1 = Rectangle(20, 1)
print(rectangle1.get_area())

# 6. Create a class Book with title and author. Add a method that returns a string like: "Title by Author".

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def getTitleAndAuthor(self): 
        return f"{self.title} by {self.author}"

book1 = Book('The Great Gatsby', 'F. Scott Fitzgerald')
print(book1.getTitleAndAuthor())

# 7. Create a class BankAccount that starts with balance 0. Add deposit and withdraw methods.

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, number): 
        self.balance += number
    
    def withdraw(self, number):
        self.balance -= number

accoun1 = BankAccount()
accoun1.deposit(10)
accoun1.withdraw(5)
print(accoun1.balance)

# 8. Create a class Product with name and price. Add a method that applies a discount percentage to the price.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount

p = Product("Laptop", 1000)
p.apply_discount(20)
print(p.price) 

# 9. Create a class Counter that starts at 0 and has methods increase() and decrease().

class Counter:
    def __init__(self):
        self.count = 0

    def increase(self, number): 
        self.count += number
    
    def decrease(self, number):
        self.count -= number

count1 = Counter()
count1.increase(10)
count1.decrease(5)
print(count1.count)

# 10. Create a class Movie with title, year, and rating. Add a method that checks if rating >= 8 and returns “Great movie”.

class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating
    
    def check_rating(self): 
        if self.rating >= 8:
            return f"Great movie"
        else:
            return "Not so great"

movie1 = Movie('The green mile', 1999, 8)
print(movie1.check_rating())

# 11. Create a class Laptop with brand, ram, storage. Add a method that upgrades the RAM.

class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def upgrade_ram(self, number): 
        self.ram += number

upgrade1 = Laptop('Dell', 4, 128)
upgrade1.upgrade_ram(10)
print(upgrade1.ram)

# 12. Create a class Circle with radius. Add a method that returns the circumference.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14 * self.radius

c = Circle(5)
print(c.circumference())

# 13. Create a class Playlist that stores a list of songs. Add method add_song and method total_songs.

class Playlist:
    def __init__(self, songs):
        self.songs = list(songs)

    def add_song(self, song): 
        self.songs.append(song)

    def total_songs(self): 
        return len(self.songs)

song1 = Playlist(['Fire', 'Mistletoe', 'Thinking out loud'])
song1.add_song('Sorry')
print(song1.total_songs())

# 14. Create a class Person with name and age. Add a method birthday() that increases age by 1.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age += 1

me = Person('Gabi', 27)
me.birthday()
print(me.age)

# 15. Create a class Animal with name and sound. Add a method speak() that prints the sound.

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        print(self.sound)

me = Animal('Dog', 'bark')
me.speak()

# 16. Create a class Temperature that stores Celsius. Add a method to convert it to Fahrenheit.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def convert_to_fahrenheit(self):
        return f"{self.celsius * 9 / 5 + 32}"

me = Temperature(32)
print(me.convert_to_fahrenheit())

# 17. Create a class Wallet that stores money. Add method spend(amount) that decreases money only if possible.

class Wallet:
    def __init__(self):
        self.money = 10

    def spend(self, number):
        if self.money >= number: self.money -= number
        else: return

accoun1 = Wallet()
accoun1.spend(9)
accoun1.spend(2)
print(accoun1.money)

# 18. Create a class Employee with name and salary. Add a method give_raise(amount).

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, number):
        self.salary += number

e = Employee('Gabi', 1000)
e.give_raise(2)
print(e.salary)

# 19. Create a class ShoppingCart with a list of items. Add methods add_item and item_count.

class ShoppingCart:
    def __init__(self, items):
        self.items = list(items)

    def add_item(self, item): 
        self.items.append(item)

    def item_count(self): 
        return len(self.items)

s = ShoppingCart(['apple', 'banana'])
s.add_item('bread')
print(s.item_count())

# 20. Create a class User with username and password. Add a method check_password(given_password) that returns True/False.

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password): 
        if password == self.password: return True
        else: return False
        
user1 = User('Gabi', '123')
print(user1.check_password('123'))
