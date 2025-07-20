task = input("Enter a task description: ")
priority = input("Insert task priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time bound (yes/no): ").strip().lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that require immediate attention today")
        else:
            print(f"Note: '{task}' is a high priority task but doesn't require immediate attention ")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that require immediate attention today")
        else:
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time")
    case "low":
        if time_bound == "yes":
            print(f"Note '{task}' is a low priority task, but still require attention ")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
