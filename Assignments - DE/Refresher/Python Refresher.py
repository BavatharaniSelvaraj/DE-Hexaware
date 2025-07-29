# 1. Writing and Running First Program
print("Welcome to Python World!")

# 2. Keywords and Identifiers
# Valid Identifiers
employee_id = 101
full_name = "Praveen"
_is_active = False

# 3. Variables and Operators
x = 15
y = 4

# Arithmetic Operations
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Remainder:", x % y)
print("Power:", x ** y)

# Comparison Operators
print("x equals y?", x == y)
print("x less than y?", x < y)

# Logical Operators
m = False
n = True
print("m and n:", m and n)
print("m or n:", m or n)
print("not n:", not n)

# 4. Data Types
# Numeric
num1 = 100
num2 = 45.67
num3 = 7 + 9j

print("Integer:", num1)
print("Float:", num2)
print("Complex:", num3)

# Sequence: String
message = "Learning Python"
print("Message:", message)

# List
vehicles = ["car", "bike", "bus"]
print("Vehicles:", vehicles)

# Tuple
seasons = ("summer", "rainy", "winter")
print("Seasons:", seasons)

# Boolean
is_online = True
has_permission = False
print("Online?", is_online)

# Type Checking
print("Type of vehicles:", type(vehicles))
print("Type of num2:", type(num2))

# Input and Output
user = input("What is your favorite language? ")
print("Nice choice,", user)

# Input with conversion
quantity = int(input("Enter quantity: "))
print("Quantity selected:", quantity)

# If Statement
temp = int(input("Enter temperature: "))
if temp > 30:
    print("It's hot outside.")

# If-Else
score = int(input("Enter your score: "))
if score >= 50:
    print("Congratulations, you passed!")
else:
    print("Better luck next time.")

# If-Elif-Else
rating = int(input("Rate our service (1-5): "))
if rating == 5:
    print("Excellent")
elif rating == 4:
    print("Very Good")
elif rating == 3:
    print("Good")
else:
    print("Needs Improvement")

# For Loop
print("Counting down from 5:")
for num in range(5, 0, -1):
    print(num)

# While Loop
print("Counting up to 5:")
i = 1
while i <= 5:
    print(i)
    i += 1

# Nested Loops
print("Pattern Grid:")
for row in range(1, 3):
    for col in range(1, 4):
        print(f"{row},{col}", end=" ")
    print()

# Break, Continue, Pass
print("Break at 4:")
for i in range(1, 7):
    if i == 4:
        break
    print(i)

print("Continue at 3:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("Pass Example:")
for i in range(1, 4):
    if i == 2:
        pass
    print("Value:", i)

# Lists
cities = ["Mumbai", "Delhi", "Chennai"]
print("Cities:", cities)
print("First City:", cities[0])
print("Slice:", cities[:2])

cities.append("Bangalore")
print("After Append:", cities)

cities.insert(1, "Hyderabad")
print("After Insert:", cities)

cities.remove("Delhi")
print("After Remove:", cities)

removed = cities.pop()
print("Popped:", removed)

print("List length:", len(cities))

# Dictionaries
employee = {
    "name": "Arun",
    "role": "Engineer",
    "experience": 3
}
print("Employee:", employee)
employee["salary"] = 50000
employee["experience"] = 4
del employee["role"]
print("Updated Employee:", employee)

# Sets
tools = {"hammer", "wrench", "drill"}
tools.add("screwdriver")
tools.remove("drill")
print("Tools Set:", tools)

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)

# Map with Lambda
values = [2, 4, 6, 8]
squares = list(map(lambda n: n**2, values))
print("Squares:", squares)

# Map with Function
def double(n):
    return n * 2

doubled = list(map(double, values))
print("Doubled:", doubled)

# Functions
def welcome_user(user):
    print("Hello", user)

welcome_user("Divya")

# Default Argument
def greet_user(name="Visitor"):
    print("Greetings,", name)

greet_user()
greet_user("Ramya")

# Keyword Arguments
def course_info(title, duration, trainer):
    print("Title:", title)
    print("Duration:", duration)
    print("Trainer:", trainer)

course_info(trainer="Priya", title="AI Basics", duration="6 weeks")

# *args
def total(*items):
    print("Items:", items)
    return sum(items)

print("Total:", total(10, 20, 30))

# **kwargs
def user_details(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

user_details(name="Arvind", age=28, city="Pune")

# Lambda
subtract = lambda a, b: a - b
print("Subtract:", subtract(10, 5))

# String Functions
text = "  Welcome to coding "
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Strip:", text.strip())
print("Replace:", text.replace("coding", "Python"))
print("Split:", text.split())

# Number Functions
print("abs(-7):", abs(-7))
print("round(7.567):", round(7.567, 1))
print("max(5, 2, 9):", max(5, 2, 9))
print("min(3, 1, 8):", min(3, 1, 8))

# Date and Time
import datetime

now = datetime.datetime.now()
print("Now:", now)

today = datetime.date.today()
print("Today:", today)

specific = datetime.date(2024, 5, 1)
print("Specific:", specific)
print("Formatted:", now.strftime("%Y-%m-%d %H:%M"))

# Class and Object
class Device:
    def operate(self):
        print("Device is operating")

d1 = Device()
d1.operate()

# Access Specifiers
class AccessTest:
    public_data = "Visible to all"
    _protected_data = "Visible to subclass"
    __private_data = "Hidden from outside"

    def display(self):
        print(self.public_data)
        print(self._protected_data)
        print(self.__private_data)

obj = AccessTest()
obj.display()
print(obj.public_data)
print(obj._protected_data)

# Constructor
class User:
    def __init__(self, username):
        self.username = username

    def show(self):
        print("Username:", self.username)

u = User("tharani")
u.show()

# Inheritance
class Vehicle:
    def run(self):
        print("Vehicle is running")

class Car(Vehicle):
    def horn(self):
        print("Car horn blowing")

c = Car()
c.run()
c.horn()

# Polymorphism
class Tool:
    def use(self):
        print("Using a tool")

class Hammer(Tool):
    def use(self):
        print("Using a hammer")

class Screwdriver(Tool):
    def use(self):
        print("Using a screwdriver")

t1 = Hammer()
t2 = Screwdriver()
t1.use()
t2.use()

# File Handling
with open("demo.txt", "w") as file:
    file.write("This is a sample document.\nEnjoy learning Python!\n")

with open("demo.txt", "r") as file:
    data = file.read()
    print("File Data:\n", data)

# Exception Handling
try:
    val1 = int(input("Enter value 1: "))
    val2 = int(input("Enter value 2: "))
    print("Result:", val1 / val2)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Only numeric input is allowed.")
finally:
    print("Execution complete.")

# Modules
def greet(name):
    return f"Hey, {name}!"

def multiply(x, y):
    return x * y

if __name__ == "__main__":
    print(greet("Kavin"))
    print("Multiplication:", multiply(6, 7))

# Standard Modules
import math
import random

print("Square root of 49:", math.sqrt(49))
print("Random number:", random.randint(1, 50))

# Simulated Package Utilities
def square(n):
    return n ** 2

def echo_upper(text):
    return text.upper()

print("Square of 9:", square(9))
print("Echo Upper:", echo_upper("python"))

__all__ = ['greet', 'multiply', 'square', 'echo_upper']
print("Simulated package functions:", __all__)
