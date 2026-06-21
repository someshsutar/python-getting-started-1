# ==========================================
# Python Functions Demonstration
# ==========================================

print("=== Python Functions Demo ===\n")

# ------------------------------------------
# 1. Simple Function
# ------------------------------------------

def greet():
    print("Hello, Welcome to Python!")

greet()

print()

# ------------------------------------------
# 2. Function with Parameters
# ------------------------------------------

def greet_user(name):
    print(f"Hello, {name}")

greet_user("Someshwar")

print()

# ------------------------------------------
# 3. Function Returning a Value
# ------------------------------------------

def add(a, b):
    return a + b

result = add(10, 20)

print(f"Addition Result: {result}")

print()

# ------------------------------------------
# 4. Function with Type Hints
# ------------------------------------------

def multiply(a: int, b: int) -> int:
    return a * b

print(f"Multiplication Result: {multiply(5, 6)}")

print()

# ------------------------------------------
# 5. Default Parameter
# ------------------------------------------

def welcome(name="Guest"):
    print(f"Welcome {name}")

welcome()
welcome("Someshwar")

print()

# ------------------------------------------
# 6. Named Arguments
# ------------------------------------------

def create_employee(name, age, city):
    print(f"Name: {name}")
    print(f"Age : {age}")
    print(f"City: {city}")

create_employee(
    city="Pune",
    age=40,
    name="Someshwar"
)

print()

# ------------------------------------------
# 7. Multiple Return Values
# ------------------------------------------

def calculate(a, b):
    return a + b, a - b, a * b

sum_value, diff_value, product_value = calculate(20, 10)

print(f"Sum     : {sum_value}")
print(f"Diff    : {diff_value}")
print(f"Product : {product_value}")

print()

# ------------------------------------------
# 8. Variable Arguments (*args)
# ------------------------------------------

def calculate_total(*numbers):
    return sum(numbers)

print("Total 1:", calculate_total(10, 20))
print("Total 2:", calculate_total(10, 20, 30))
print("Total 3:", calculate_total(10, 20, 30, 40))

print()

# ------------------------------------------
# 9. Keyword Arguments (**kwargs)
# ------------------------------------------

def display_details(**details):

    print("Employee Details")

    for key, value in details.items():
        print(f"{key}: {value}")

display_details(
    name="Someshwar",
    city="Pune",
    experience=17,
    technology=".NET"
)

print()

# ------------------------------------------
# 10. Lambda Function
# ------------------------------------------

square = lambda x: x * x

print(f"Square of 5 = {square(5)}")

print()

# ------------------------------------------
# 11. Function Calling Another Function
# ------------------------------------------

def calculate_bonus(salary, percentage):
    return salary * percentage / 100

def display_bonus(employee_name, salary):

    bonus = calculate_bonus(salary, 20)

    print(f"{employee_name} Bonus = {bonus}")

display_bonus("Someshwar", 120000)

print()

# ------------------------------------------
# 12. Recursion
# ------------------------------------------

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print("Factorial of 5 =", factorial(5))

print()

# ------------------------------------------
# 13. Nested Function
# ------------------------------------------

def company():

    print("ABC Corporation")

    def department():
        print("Engineering Department")

    department()

company()

print()

# ------------------------------------------
# 14. Practical Business Example
# ------------------------------------------

def evaluate_employee(name, experience, salary):

    if experience >= 15 and salary >= 100000:
        grade = "Senior Architect"

    elif experience >= 10:
        grade = "Technical Lead"

    elif experience >= 5:
        grade = "Senior Developer"

    else:
        grade = "Developer"

    return {
        "name": name,
        "experience": experience,
        "salary": salary,
        "grade": grade
    }

employee = evaluate_employee(
    "Someshwar",
    17,
    120000
)

print("Employee Evaluation")
print("-" * 25)

for key, value in employee.items():
    print(f"{key}: {value}")

print()

# ------------------------------------------
# 15. Main Function
# ------------------------------------------

def main():

    print("Application Started")

    total = add(100, 200)

    print(f"Total = {total}")

    print("Application Completed")

# Program Entry Point
if __name__ == "__main__":
    main()