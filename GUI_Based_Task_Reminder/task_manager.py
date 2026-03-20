import json
import os
from datetime import datetime

TASKS_FILES = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILES):
        with open(TASKS_FILES, "r") as f:
            content = f.read()
            if not content.strip():  # file is empty
                return []
            return json.loads(content)
    return []


##This function saves the full tasks list back to the JSON file when created
def save_tasks(tasks):
    with open(TASKS_FILES, "w") as f:
        json.dump(tasks, f, indent=4)

##Created a new task dict and append it to the saved list.
def add_task(name, description, deadline, email):
    tasks = load_tasks() #get what is alrady saved 

    #Now this dictionary takes the new tasks 
    new_task = {
        "name" : name,
        "description" : description,
        "deadline" : deadline, #Expected format 2026-0-25,
        "email" : email,
        "status": "pending"
    }


    tasks.append(new_task)
    save_tasks(tasks)  # write the updated list back to file

def delete_task(task_name):
    """Remove a task by its name."""
    tasks = load_tasks()

    # Keep every task that does NOT match the name
    updated = [t for t in tasks if t["name"] != task_name]

    save_tasks(updated)


def check_deadlines():
    """Return tasks that are overdue, due today, or due within 48 hours."""
    tasks = load_tasks()
    now = datetime.now()
    flagged = []

    for task in tasks:
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d")
        diff = (deadline - now).total_seconds() / 3600  # difference in hours

        if diff < 0:
            task["urgency"] = "overdue"
            flagged.append(task)
        elif diff <= 24:
            task["urgency"] = "due today"
            flagged.append(task)
        elif diff <= 48:
            task["urgency"] = "due soon"
            flagged.append(task)

    return flagged


