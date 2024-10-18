# Define an empty list to store tasks
todo_list = []

# Function to display the tasks
def show_tasks():
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task(task):
    todo_list.append(task)
    print(f"'{task}' has been added to your to-do list.")

# Function to remove a task
def remove_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"'{removed_task}' has been removed from your to-do list.")
    else:
        print("Invalid task number!")

# Main loop
while True:
    print("\nOptions: 1. Show tasks 2. Add task 3. Remove task 4. Exit")
    option = input("Choose an option: ")

    if option == '1':
        show_tasks()
    elif option == '2':
        task = input("Enter the task to add: ")
        add_task(task)
    elif option == '3':
        show_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif option == '4':
        print("Exiting the To-Do List application.")
        break
    else:
        print("Invalid option! Please try again.")
