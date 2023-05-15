import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from notification_service.internal.domain.interfaces.email_notification import EmailNotificationServiceInterface
from notification_service.internal.domain.models.email_notification import EmailNotification, EmailBodyType
from notification_service.settings import __smtp_setting__


def get_email_notification_service() -> EmailNotificationServiceInterface:
    if not hasattr(get_email_notification_service, "service"):
        get_email_notification_service.service = EmailNotificationService(
            smtp_server=__smtp_setting__.server,
            smtp_port=__smtp_setting__.port,
            smtp_username=__smtp_setting__.username,
            smtp_password=__smtp_setting__.password,
        )
    return get_email_notification_service.service


class EmailNotificationService(EmailNotificationServiceInterface):
    smtp_server: str
    smtp_port: int
    smtp_username: str
    smtp_password: str

    def __init__(self, smtp_server: str, smtp_port: int, smtp_username: str, smtp_password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def send_email_notification(self, email_notification: EmailNotification):
        message = MIMEMultipart()
        message["From"] = email_notification.from_
        message["To"] = ", ".join(email_notification.to)
        if email_notification.cc:
            message["Cc"] = ", ".join(email_notification.cc)
        message["Subject"] = email_notification.subject

        if email_notification.body_type == EmailBodyType.html:
            body = MIMEText(email_notification.body, 'html')
        else:
            body = MIMEText(email_notification.body, 'plain')
        message.attach(body)

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp:
            smtp.starttls()
            smtp.login(self.smtp_username, self.smtp_password)
            smtp.sendmail(email_notification.from_,
                          email_notification.to + email_notification.cc + email_notification.bcc, message.as_string())
