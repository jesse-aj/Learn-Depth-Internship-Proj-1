import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Gmail Cred.
SENDER_EMAIL = "appiahjesse123@gmail.com"
SENDER_PASSWORD = "ntll wbil wkpw rpvi"

#Function to send email
def send_reminder(task):
    "Send a reminder email for a single task."

    receiver_email = task["email"]
    task_name      = task["name"]
    deadline       = task["deadline"]
    urgency        = task["urgency"]


  # The actual email build
    msg = MIMEMultipart()
    msg["From"]    = SENDER_EMAIL
    msg["To"]      = receiver_email
    msg["Subject"] = f"Task Reminder: {task_name}"

    body = f"""
Hello,

This is a reminder for your task:

  Task Name   : {task_name}
  Description : {task["description"]}
  Deadline    : {deadline}
  Status      : {urgency.upper()}

Please ensure the task is completed before the deadline.

Regards,
Task Reminder System
    """

    msg.attach(MIMEText(body, "plain"))


