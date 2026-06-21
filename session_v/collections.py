# ==========================================
# Python Collections Demonstration
# ==========================================

print("=== Python Collections Demo ===\n")

# ------------------------------------------------
# 1. LIST - Store multiple employees
# ------------------------------------------------

employees = [
    "Someshwar",
    "John",
    "Mary",
    "David",
    "John"  # Duplicate allowed
]

print("Employee List:")
print(employees)

print("\nTotal Employees:", len(employees))

# Add employee
employees.append("Alex")

print("\nAfter Adding Alex:")
print(employees)

# Iterate list
print("\nEmployees:")

for employee in employees:
    print(employee)

# ------------------------------------------------
# 2. TUPLE - Store fixed employee information
# ------------------------------------------------

print("\n" + "=" * 50)

employee_info = (
    101,
    "Someshwar",
    "Pune"
)

print("Employee Tuple:")
print(employee_info)

print("Employee Id :", employee_info[0])
print("Employee Name :", employee_info[1])
print("Employee City :", employee_info[2])

# ------------------------------------------------
# 3. SET - Remove duplicate technologies
# ------------------------------------------------

print("\n" + "=" * 50)

technologies = [
    "Python",
    ".NET",
    "Angular",
    "Python",
    ".NET",
    "React"
]

print("Original Technologies:")
print(technologies)

unique_technologies = set(technologies)

print("\nUnique Technologies:")
print(unique_technologies)

# Membership test
if "Python" in unique_technologies:
    print("\nPython skill found")

# ------------------------------------------------
# 4. DICTIONARY - Employee Profile
# ------------------------------------------------

print("\n" + "=" * 50)

employee = {
    "id": 101,
    "name": "Someshwar",
    "city": "Pune",
    "experience": 17,
    "salary": 120000
}

print("Employee Dictionary:")
print(employee)

print("\nEmployee Details:")

for key, value in employee.items():
    print(f"{key}: {value}")

# Update value
employee["salary"] = 140000

print("\nUpdated Salary:")
print(employee["salary"])

# ------------------------------------------------
# 5. NESTED COLLECTIONS
# ------------------------------------------------

print("\n" + "=" * 50)

employees_data = [
    {
        "id": 1,
        "name": "Someshwar",
        "skills": ["Python", ".NET", "Angular"]
    },
    {
        "id": 2,
        "name": "John",
        "skills": ["Java", "Spring"]
    },
    {
        "id": 3,
        "name": "Mary",
        "skills": ["Python", "React"]
    }
]

print("Employee Skill Matrix:\n")

for emp in employees_data:

    print(f"Employee: {emp['name']}")

    for skill in emp["skills"]:
        print(f"   - {skill}")

    print()

# ------------------------------------------------
# 6. LIST COMPREHENSION
# ------------------------------------------------

print("=" * 50)

salaries = [45000, 80000, 120000, 150000, 70000]

high_salaries = [
    salary
    for salary in salaries
    if salary >= 100000
]

print("All Salaries:")
print(salaries)

print("\nHigh Salaries:")
print(high_salaries)

# ------------------------------------------------
# 7. DICTIONARY COMPREHENSION
# ------------------------------------------------

print("\n" + "=" * 50)

salary_lookup = {
    employee["name"]: employee["salary"]
    for employee in [
        {"name": "Someshwar", "salary": 120000},
        {"name": "John", "salary": 90000},
        {"name": "Mary", "salary": 110000}
    ]
}

print("Salary Lookup:")
print(salary_lookup)

# ------------------------------------------------
# 8. PRACTICAL REPORT
# ------------------------------------------------

print("\n" + "=" * 50)

employees_report = [
    {
        "name": "Someshwar",
        "salary": 120000
    },
    {
        "name": "John",
        "salary": 80000
    },
    {
        "name": "Mary",
        "salary": 150000
    }
]

print("Employees earning more than 100000:\n")

for emp in employees_report:

    if emp["salary"] > 100000:
        print(
            f"{emp['name']} -> {emp['salary']}"
        )

print("\nProgram Completed Successfully")