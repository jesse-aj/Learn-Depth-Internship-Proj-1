import tkinter as tk
from tkinter import ttk, messagebox
from task_manager import add_task, load_tasks, delete_task, check_deadlines


#  MAIN WINDOW

root = tk.Tk()
root.title("Task Reminder System")
root.geometry("650x520")
root.resizable(False, False)

#Tabs

notebook = ttk.Notebook(root) 
notebook.pack(fill="both", expand=True, padx=10, pady=10)

#This creates all the tabs 
tab_add       = ttk.Frame(notebook)
tab_view      = ttk.Frame(notebook)
tab_deadlines = ttk.Frame(notebook)

#This applies the text in the tab created 
notebook.add(tab_add,       text="  Add Task  ")
notebook.add(tab_view,      text="  View Tasks  ")
notebook.add(tab_deadlines, text="  Deadlines  ")

#Tab 1 - Add Task

tk.Label(tab_add, text="Task Name:").grid(row=0, column=0, padx=10, pady=8, sticky="w")
entry_name = tk.Entry(tab_add, width=40)
entry_name.grid(row=0, column=1, padx=10, pady=8)

tk.Label(tab_add, text="Description:").grid(row=1, column=0, padx=10, pady=8, sticky="w")
entry_desc = tk.Entry(tab_add, width=40)
entry_desc.grid(row=1, column=1, padx=10, pady=8)

tk.Label(tab_add, text="Deadline (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=8, sticky="w")
entry_deadline = tk.Entry(tab_add, width=40)
entry_deadline.grid(row=2, column=1, padx=10, pady=8)

tk.Label(tab_add, text="Email:").grid(row=3, column=0, padx=10, pady=8, sticky="w")
entry_email = tk.Entry(tab_add, width=40)
entry_email.grid(row=3, column=1, padx=10, pady=8)

#This cleans the entries when submit is clicked 
def submit_task():
    name     = entry_name.get().strip()
    desc     = entry_desc.get().strip()
    deadline = entry_deadline.get().strip()
    email    = entry_email.get().strip()

    #Validation(No-empty feilds)
    if not all([name, desc, deadline, email]):
        messagebox.showwarning("Missing Info", "Please fill in all feilds!")
        return
    
    #Validate deadline format
    try:
        from datetime import datetime
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Invalid Date", "Use format YYYY-MM-DD e.g 2026-03-25")
        return
    
    
    add_task(name, desc, deadline, email)
    messagebox.showinfo("Success", f'Task "{name}" added successfully!')

     # Clear fields after saving
    entry_name.delete(0, tk.END)
    entry_desc.delete(0, tk.END)
    entry_deadline.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    # refresh_task_list()  # update View Tasks tab instantly
tk.Button(tab_add, text="Add Task", width=20, command=submit_task).grid(
    row=4, column=1, pady=15, sticky="e")





#This runs the Gui
root.mainloop()