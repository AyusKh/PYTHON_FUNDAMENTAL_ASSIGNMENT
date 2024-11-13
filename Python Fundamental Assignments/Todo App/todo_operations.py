# todo_operations.py
def add_task(tasks, task):
    """Add a new task to the list."""
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks(tasks):
    """Display all tasks in the list."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(tasks, task_index):
    """Delete a task by its index."""
    try:
        task_index = int(task_index) - 1  # Convert to zero-based index
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task '{deleted_task}' deleted successfully!")
        else:
            print("Invalid index. No task deleted.")
    except ValueError:
        print("Please enter a valid number.")
