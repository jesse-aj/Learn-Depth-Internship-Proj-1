import tkinter as tk
from tkinter import ttk, messagebox
from task_manager import add_task, load_tasks, delete_task, check_deadlines


#  MAIN WINDOW

root = tk.Tk()
root.title("Task Reminder System")
root.geometry("650x520")
root.resizable(False, False)