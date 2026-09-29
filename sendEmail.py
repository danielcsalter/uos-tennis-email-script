import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

#Jonny's code from his old script

def send_email_booked(email, name, park, date, time, court, code):
    load_dotenv()
    gmail_pass = os.getenv('gmail_pass')
    from_email = os.getenv('gmail_email')
    from_name = os.getenv('gmail_name')

    msg = EmailMessage()
    msg["From"] = f"{from_email}"
    msg["To"] = email
    msg["Subject"] = "UoS Tennis Court Booking"
    msg.set_content(f"Hi {name}, \n\nFor your upcoming court booking, the code is as follows:\n{park}, {date}, {time}, Court {court} - {code}\n\nIf you have any questions or issues on the day, please don't hesitate to contact me. I hope you enjoy your session!\n\nKind regards,\nDaniel")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(from_email, gmail_pass)
            smtp.send_message(msg)
        
        return True 
    except Exception as e:
        import traceback
        traceback.print_exc()
        return False
    
def send_email_unavailable(email, name):
    load_dotenv()
    gmail_pass = os.getenv('gmail_pass')
    from_email = os.getenv('gmail_email')
    from_name = os.getenv('gmail_name')

    msg = EmailMessage()
    msg["From"] = f"{from_email}"
    msg["To"] = email
    msg["Subject"] = "UoS Tennis Court Booking"
    msg.set_content(f"Hi {name},\n\nUnfortunately, your court booking for the slot you requested is unavailable.\nPlease re-submit a booking request for a different time slot.\n\nKind regards,\nDaniel")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(from_email, gmail_pass)
            smtp.send_message(msg)
        
        return True 
    except Exception as e:
        import traceback
        traceback.print_exc()
        return False
    
def send_email_denied(email, name, reason):
    load_dotenv()
    gmail_pass = os.getenv('gmail_pass')
    from_email = os.getenv('gmail_email')
    from_name = os.getenv('gmail_name')

    msg = EmailMessage()
    msg["From"] = f"{from_email}"
    msg["To"] = email
    msg["Subject"] = "UoS Tennis Court Booking"

    if reason == "you have already booked your 1 hour for this week":
        msg.set_content(f"Hi {name},\n\nUnfortunately, your court booking for the slot you requested is denied.\nReason: {reason}\n\nKind regards,\nDaniel")
    else:
        msg.set_content(f"Hi {name},\n\nUnfortunately, your court booking for the slot you requested is denied.\nReason: {reason}\n\nPlease re-submit a booking request for a different time slot.\n\nKind regards,\nDaniel")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(from_email, gmail_pass)
            smtp.send_message(msg)
        
        return True 
    except Exception as e:
        import traceback
        traceback.print_exc()
        return False
    