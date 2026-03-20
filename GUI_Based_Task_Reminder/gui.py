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

    refresh_task_list()  # update View Tasks tab instantly
tk.Button(tab_add, text="Add Task", width=20, command=submit_task).grid(
    row=4, column=1, pady=15, sticky="e")


#Tab 2 (View Task)
columns = ("Name", "Deadline", "Status", "Email")
tree = ttk.Treeview(tab_view, columns=columns, show="headings", height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=140)

tree.pack(fill="both", expand=True, padx=10, pady=10)

def refresh_task_list():

    # Clear current rows
    for row in tree.get_children():
        tree.delete(row)

    # Re-insert from file
    for task in load_tasks():
        tree.insert("", tk.END, values=(
            task["name"],
            task["deadline"],
            task["status"],
            task["email"]
        ))

def delete_selected():

    selected = tree.selection()

    if not selected:
        messagebox.showwarning("No Selection", "Please select a task to delete.")
        return
    task_name = tree.item(selected[0])["values"][0]
    confirm = messagebox.askyesno("Confirm Delete", f'Delete task "{task_name}"?')

    if confirm:
        delete_task(task_name)
        refresh_task_list()

#Creates buttons 
btn_frame = tk.Frame(tab_view)

btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Refresh",       width=15, command=refresh_task_list).pack(side="left", padx=5)
tk.Button(btn_frame, text="Delete Selected", width=15, command=delete_selected).pack(side="left", padx=5)

refresh_task_list()  # load tasks when app opens


# Tab 3 (Deadlines)

dl_columns = ("Name", "Deadline", "Urgency", "Email")
dl_tree = ttk.Treeview(tab_deadlines, columns=dl_columns, show="headings", height=12)

for col in dl_columns:
    dl_tree.heading(col, text=col)
    dl_tree.column(col, width=145)

dl_tree.pack(fill="both", expand=True, padx=10, pady=10)

#Logic GUI for deadlines

def check_and_show_deadlines():
    for row in dl_tree.get_children():
        dl_tree.delete(row)

    flagged = check_deadlines()
    if not flagged:
        messagebox.showinfo("All Clear", "No tasks approaching deadlines.")
        return

    for task in flagged:
        dl_tree.insert("", tk.END, values=(
            task["name"],
            task["deadline"],
            task["urgency"],
            task["email"]
        ))

tk.Button(tab_deadlines, text="Check Deadlines", width=20,
          command=check_and_show_deadlines).pack(pady=10)


#This runs the Gui
root.mainloop()