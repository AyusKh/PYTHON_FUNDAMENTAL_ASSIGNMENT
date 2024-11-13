# main.py
from todo_operations import add_task, view_tasks, delete_task
from utils import clear_screen, get_input

def display_menu():
    print("To-Do List Menu:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")

def main():
    tasks = []  # This will store tasks temporarily
    while True:
        clear_screen()  # Clear screen to make the menu more readable
        display_menu()
        
        choice = get_input("Choose an option (1-4): ")

        if choice == '1':
            task = get_input("Enter the task to add: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            task_index = get_input("Enter the index of the task to delete: ")
            delete_task(tasks, task_index)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
1