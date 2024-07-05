# Prompt for a single task
task = input("Please enter the task description: ")
priority = input("Please enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

    # Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Task: {task}\nPriority: High\nThis task is of high importance."
    case "medium":
        reminder = f"Task: {task}\nPriority: Medium\nThis task should be completed soon."
    case "low":
        reminder = f"Task: {task}\nPriority: Low\nThis task can be done at your convenience."
    case _:
        reminder = f"Task: {task}\nPriority: Unknown\nPlease ensure to check the priority."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

    # Provide a customized reminder
    print(f"Reminder:\n{reminder}")

