task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "High":
        priority_message = "This task has high priority."
    case "Medium":
        priority_message = "This task has medium priority."
    case 'Low':
        priority_message = "This task has low priority."
    case _:
        priority_message = "Unknown priority."

# Check if the task is time-bound and modify the reminder accordingly
if time_bound == "yes":
    time_message = "That requires immediate attention today!"
else:
    time_message = "No immediate action is required."

# Provide a customized reminder
print(f"Task: {task}")
print(f'{priority_message} {time_message}')