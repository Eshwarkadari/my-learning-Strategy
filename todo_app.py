import os # Import os module to check for file existence

# --- Functions for To-Do List Operations ---

def show_menu():
    """Displays the main menu options to the user."""
    print("\n---- TO-DO LIST MENU ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Quit")
    print("-------------------------")

def add_task():
    """Adds a new task to the 'tasks.txt' file."""
    task = input("Enter the new task: ").strip()
    if task: # Ensure task is not empty
        try:
            with open("tasks.txt", "a") as file:
                file.write(f"[ ] {task}\n") # Store task with a [ ] prefix for incomplete
            print(f"Task '{task}' added successfully.")
        except IOError as e:
            print(f"Error adding task: {e}")
    else:
        print("Task cannot be empty.")

def view_tasks():
    """Reads and displays all tasks from 'tasks.txt'."""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\n--- Your Tasks ---")
                for i, task_line in enumerate(tasks, start=1):
                    print(f"{i}. {task_line.strip()}") # .strip() removes newline characters
                print("------------------")
            else:
                print("\nNo tasks found. Add some tasks!") 
    except FileNotFoundError:
        print("\nNo tasks file found. Please add a task first.")
    except IOError as e:
        print(f"Error viewing tasks: {e}")

def mark_task_complete():
    """Marks a task as complete by modifying its prefix in the file."""
    view_tasks() # First, show tasks so user knows which one to pick

    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to mark complete.")
            return

        task_number_str = input("Enter the number of the task to mark as complete: ").strip()
        task_number = int(task_number_str)

        if 1 <= task_number <= len(tasks):
            task_index = task_number - 1 # Adjust for 0-based indexing
            current_task_line = tasks[task_index].strip()

            if current_task_line.startswith("[X]"):
                print(f"Task '{current_task_line[4:]}' is already complete.")
            else:
                # Mark as complete: replace '[ ]' with '[X]'
                tasks[task_index] = "[X] " + current_task_line[4:] + "\n" # Assuming original was "[ ] Task"

                # Write all tasks back to the file (overwriting)
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print(f"Task '{current_task_line[4:]}' marked as complete.")
        else:
            print("Invalid task number. Please enter a valid number from the list.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except FileNotFoundError:
        print("No tasks file found. Please add a task first.")
    except IOError as e:
        print(f"Error marking task complete: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- Main Application Loop ---
def run_todo_app():
    """Main function to run the To-Do List application."""
    while True: # Keep the application running
        show_menu()
        choice_str = input("Enter your choice (1-4): ").strip()

        try:
            choice = int(choice_str)

            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                print("Exiting the To-Do List. Goodbye!")
                break # Exit the while loop
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the application
if __name__ == "__main__":
    run_todo_app()