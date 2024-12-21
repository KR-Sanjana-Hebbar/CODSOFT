import json

# Global variable for tasks
tasks = []

def load_tasks():
    """Load tasks from a JSON file."""
    try:
        with open("task.json", "r") as file:
            global tasks
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    """Save tasks to a JSON file."""
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Add a new task."""
    description = input("Enter the task description: ").strip()
    if description:
        task_id = len(tasks) + 1
        tasks.append({"id": task_id, "description": description, "completed": False})
        save_tasks()
        print(f"Task {task_id} is added.")
    else:
        print("Please enter task description! Task description cannot be empty.")

def view_tasks():
    """View all tasks."""
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\nYour Tasks are:")
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        print(f"{task['id']}. {task['description']} [{status}]")

def complete_task():
    """Mark a task as completed."""
    try:
        task_id = int(input("Enter the task ID to mark it as completed: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks()
                print(f"Task {task_id} is marked as completed.")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input! Please enter a number.")

def delete_task():
    """Delete a task."""
    try:
        task_id = int(input("Enter the task ID to delete: "))
        global tasks
        task_to_delete = next((task for task in tasks if task["id"] == task_id), None)
        if task_to_delete:
            tasks = [task for task in tasks if task["id"] != task_id]
            save_tasks()
            print(f"Task {task_id} is deleted.")
        else:
            print("Task ID not found.")
    except ValueError:
        print("Invalid input! Please enter a number.")

def menu():
    """Display the menu and handle user input."""
    load_tasks()
    while True:
        print("\nTo-Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
