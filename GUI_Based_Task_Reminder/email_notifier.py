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

 # Connecting to Gmail and send
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()  # encrypts the connection for security

        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())

        server.quit()

        return True, task_name
    except Exception as e:
        return False, str(e)

def send_all_reminders(flagged_tasks):
    "Loop through all flagged tasks and send emails."
    results = []
    
    for task in flagged_tasks:
        success, info = send_reminder(task)
        results.append((success, info))
    return results