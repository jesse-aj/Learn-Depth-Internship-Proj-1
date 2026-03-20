# GUI-Based Task Reminder and Email Notification System

A Python desktop application for managing tasks and sending automated email
reminders when deadlines approach. Built as part of the LearnDepth Academy
Python Programming Internship.

## Features
- Add tasks with name, description, deadline, and email
- View and delete saved tasks in a clean table interface
- Mark tasks as completed directly from the interface
- Automatically detect overdue, due today, and due soon tasks
- Send email reminders via Gmail SMTP
- Auto-checks deadlines on startup and alerts user immediately
- Local JSON storage — no database required

## Project Structure
GUI_Based_Task_Reminder/
├── gui.py              # Main application and Tkinter interface
├── task_manager.py     # Core logic — task CRUD and deadline checking
├── email_notifier.py   # Email sending via smtplib
├── tasks.json          # Local task storage
└── README.md           # Project documentation

## Requirements
- Python 3.x (no external libraries needed)
- A Gmail account with 2-Step Verification enabled
- A Gmail App Password

## Setup
1. Clone or download the project
2. Open email_notifier.py and update these two lines with your credentials:
   SENDER_EMAIL = "yourgmail@gmail.com"
   SENDER_PASSWORD = "your-app-password"
3. Run the application:
   python gui.py

## How to Use
1. Go to the Add Task tab and fill in task details
2. Click Add Task to save
3. View all tasks in the View Tasks tab
4. Select a task and click Mark Complete to update its status
5. Click Check Deadlines to see approaching deadlines
6. Confirm to send email reminders to task owners
7. App automatically alerts you of flagged tasks on startup

## Notes
- Deadline format must be YYYY-MM-DD (e.g. 2026-03-25)
- Email reminders require an active internet connection
- App Password is required — your regular Gmail password will not work
- Completed tasks are still visible in View Tasks for record keeping

## Author
Built by Jesse | LearnDepth Academy Python Internship