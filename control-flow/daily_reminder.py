# daily_reminder.py
# Provides customized reminders for a single task based on priority and time sensitivity

# Get task details from user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task with match-case and conditionals
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is high priority. Address it soon.")
    
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' should be completed today as it's time-sensitive.")
        else:
            print(f"\nReminder: Consider working on '{task}' this week.")
    
    case "low":
        if time_bound == "yes":
            print(f"\nNote: '{task}' has a deadline but is low priority.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    case _:
        print("\nPlease enter a valid priority level (high/medium/low).")