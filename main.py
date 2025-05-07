import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks! You're all done.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "❌"
            print(f"{idx}. {status} {task['task']}")

def add_task(tasks, description):
    tasks.append({"task": description, "done": False})
    save_tasks(tasks)
    print(f"Added: {description}")

def mark_done(tasks, index):
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked as done: {tasks[index]['task']}")
    except IndexError:
        print("Invalid task number.")

def delete_task(tasks, index):
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    except IndexError:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        show_tasks(tasks)
        print("\nCommands: add [task], done [num], del [num], quit")
        command = input("> ").strip()
        if command == "quit":
            break
        elif command.startswith("add "):
            add_task(tasks, command[4:])
        elif command.startswith("done "):
            mark_done(tasks, int(command[5:]) - 1)
        elif command.startswith("del "):
            delete_task(tasks, int(command[4:]) - 1)
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
