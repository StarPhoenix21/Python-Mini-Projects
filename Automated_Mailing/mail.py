import smtplib
import os
import pandas as pd
from email.message import EmailMessage

def send_email(to_email, subject, body, attachment_path=None):
    try:
        # Email Credentials (Replace with actual credentials or environment variables)
        EMAIL_ADDRESS = os.getenv('EMAIL_USER', 'your_email@example.com')
        EMAIL_PASSWORD = os.getenv('EMAIL_PASS', 'yourpassword')
        
        # Setup Email
        msg = EmailMessage()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.set_content(body)
        
        # Attach file if provided
        if attachment_path:
            try:
                with open(attachment_path, 'rb') as f:
                    file_data = f.read()
                    file_name = os.path.basename(attachment_path)
                    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
                print(f"Attachment {file_name} added successfully.")
            except FileNotFoundError:
                print("Error: Attachment file not found.")
                return
        
        # Send Email
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {to_email}")
            
            # Log email details
            log_email(to_email, subject, attachment_path)
        
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")

def log_email(to_email, subject, attachment):
    log_file = 'email_log.csv'
    log_data = {'Recipient': [to_email], 'Subject': [subject], 'Attachment': [attachment]}
    df = pd.DataFrame(log_data)
    
    if os.path.exists(log_file):
        df.to_csv(log_file, mode='a', header=False, index=False)
    else:
        df.to_csv(log_file, mode='w', header=True, index=False)
    print("Email logged successfully.")

# Example Usage
send_email("recipient@example.com", "Test Subject", "This is a test email.", "test.pdf")
