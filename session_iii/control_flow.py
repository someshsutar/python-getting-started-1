# =====================================
# Control Flow & Comparison Operators
# =====================================

employee_name = "Someshwar"
experience = 17
salary = 120000
is_manager = True

print("Employee Evaluation")
print("-" * 30)

# -------------------------------------
# Comparison Operators
# -------------------------------------

print("Salary > 100000:", salary > 100000)
print("Salary < 50000:", salary < 50000)
print("Experience == 17:", experience == 17)
print("Experience != 10:", experience != 10)
print("Experience >= 15:", experience >= 15)
print("Experience <= 20:", experience <= 20)

print()

# -------------------------------------
# if / elif / else
# -------------------------------------

if salary >= 150000:
    grade = "A"
elif salary >= 100000:
    grade = "B"
elif salary >= 50000:
    grade = "C"
else:
    grade = "D"

print(f"Employee Grade: {grade}")

print()

# -------------------------------------
# Logical Operators
# -------------------------------------

if experience >= 10 and salary >= 100000:
    print("Eligible for Senior Architect role")

if is_manager or experience > 15:
    print("Eligible for Leadership Program")

if not is_manager:
    print("Individual Contributor")
else:
    print("Manager")

print()

# -------------------------------------
# Membership Operator
# -------------------------------------

skills = ["Python", ".NET", "Angular", "Azure"]

if "Python" in skills:
    print("Python skill found")

if "Java" not in skills:
    print("Java skill not found")

print()

# -------------------------------------
# For Loop
# -------------------------------------

print("Skills:")

for skill in skills:
    print(f" - {skill}")

print()

# -------------------------------------
# For Loop with continue
# -------------------------------------

print("Skipping Angular:")

for skill in skills:
    if skill == "Angular":
        continue

    print(skill)

print()

# -------------------------------------
# For Loop with break
# -------------------------------------

print("Stop when Azure found:")

for skill in skills:
    if skill == "Azure":
        print("Azure found. Stopping search.")
        break

    print(skill)

print()

# -------------------------------------
# While Loop
# -------------------------------------

count = 1

while count <= 5:
    print(f"Iteration: {count}")
    count += 1

print()

# -------------------------------------
# Chained Comparison
# -------------------------------------

age = 40

if 18 <= age <= 60:
    print("Working Age Group")

print()

# -------------------------------------
# List Comprehension
# -------------------------------------

numbers = list(range(1, 21))

even_numbers = [n for n in numbers if n % 2 == 0]

print("Even Numbers:")
print(even_numbers)

print()

# -------------------------------------
# Dictionary Iteration
# -------------------------------------

employee = {
    "name": employee_name,
    "experience": experience,
    "salary": salary
}

print("Employee Details:")

for key, value in employee.items():
    print(f"{key}: {value}")

print()

print("Program Completed Successfully")