import tkinter as tk
from tkinter import ttk, messagebox
from task_manager import add_task, load_tasks, delete_task, check_deadlines


#  MAIN WINDOW

root = tk.Tk()
root.title("Task Reminder System")
root.geometry("650x520")
root.resizable(False, False)

#Tabs

notebook = ttk.Notebook(root) # linking noteebook to make everything coherant
notebook.pack(fill="both", expand=True, padx=10, pady=10)

#This creates all the tabs 
tab_add       = ttk.Frame(notebook)
tab_view      = ttk.Frame(notebook)
tab_deadlines = ttk.Frame(notebook)

#This applies the text in the tab created 
notebook.add(tab_add,       text="  Add Task  ")
notebook.add(tab_view,      text="  View Tasks  ")
notebook.add(tab_deadlines, text="  Deadlines  ")





#This runs the Gui
root.mainloop()