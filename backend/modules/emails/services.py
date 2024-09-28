import smtplib
from email.message import EmailMessage
from typing import Sequence


def create_message(
    from_: str, to: str | Sequence[str], subject: str, body: str
) -> EmailMessage:
    message = EmailMessage()
    message["From"] = from_
    message["To"] = to
    message["Subject"] = subject
    message.set_content(body)
    return message


def send_email(
    message: EmailMessage, login: str, password: str, receiver: str | Sequence[str]
) -> bool:
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(login, password)
            smtp.sendmail(login, receiver, message.as_string())
    except Exception as e:
        return False
    return True


# class EmailService:
#     DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
#
#     def __init__(self):
#         self.login = config.EMAIL_USER
#         self.password = config.EMAIL_APP_CLIENT_ACCESS_CODE
#
#     def send_email_to_yourself(self, subject: str, body: str) -> bool:
#         message = create_message(self.login, self.login, subject, body)
#         return send_email(message, self.login, self.password, self.login)
