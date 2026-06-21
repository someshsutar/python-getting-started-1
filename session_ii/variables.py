# A variable is simply a name that refers to a value.
# Python automatically determines the type.

name = "Someshwar"
age = 40
salary = 100000.50

print(name)

print("Name: "+name)

print(name,age,salary)

# Checking Variable Types

print(type(name),type(age),type(salary))

# print("Name: "+name,"Age: "+ age,"Salarey: "+salary)


# Primitive Data Types - int, float, str, bool, NoneType

is_active = True

print(is_active)

print(type(is_active))

customer = None

print(customer)

print(type(customer))


# Dynamic Typing - A variable can change type during execution.

value = 10

print(type(value))

value = "Hello"

print(type(value))

# Multiple Assignment - Python allows assigning multiple variables at once.

name, age, city = "Someshwar", 40, "Pune"

print(name)

print(age)

print(city)

# Variable Naming Rules

# Valid

first_name = "Someshwar"
_age = 40
salary2025 = 100000

# Invalid

# 2name = "John"      # Starts with digit
# first-name = "John" # Hyphen not allowed

# Non-Primitive and Collection Data Types

# List - ordered collection of items

fruits = ["Apple", "Mango", "Orange"]

fruits.append("Banana")

print(fruits[0])

fruits[0]="Greps"  #Can modify

print(fruits[0])

print(type(fruits))

# Tuple (tuple) – ordered collection, immutable but can store multiple items

coordinates = (10.0, 20.0)

print(coordinates[0])

# coordinates[0] = 5 #Cannot modify

print(type(coordinates))

# Set - Stores unique values.

numbers = [1,2,2,3,4]

unique_numbers = {1, 2, 2, 3, 4}

print(numbers)

print(unique_numbers)


# Dictionary - Key-value pairs.

employee = {
    "id": 101,
    "name": "Someshwar",
    "city": "Pune"
}

print(employee["name"])

print(employee["city"])


# Type Conversion

# Integer to String
age = 40
age_text = str(age)

print(type(age),type(age_text))

age = int("40")

print(type(age))

# Integer to Float

price = float(100)

print(type(price))

# Float to Integer

price = int(99.99)

print(price) #decimal part removed

print(type(price))

