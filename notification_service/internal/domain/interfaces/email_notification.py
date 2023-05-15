from abc import ABC, abstractmethod

from notification_service.internal.domain.models.email_notification import EmailNotification


class EmailNotificationServiceInterface(ABC):

    @abstractmethod
    def send_email_notification(self, email_notification: EmailNotification):
        ...
