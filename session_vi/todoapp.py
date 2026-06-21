tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for i, t in enumerate(tasks, 1):
        print(i, t)

while True:
    choice = input("Add or Show or Exit: ").capitalize()
    print("Your choice", choice)
    if choice == "Add":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "Show":
        show_tasks()
    elif choice == "Exit":
        break