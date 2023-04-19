from notification_service.server.routes.routes import *
from notification_service.internal.adapters.controllers.http import email_notification

__routes__ = Routes(routers=(email_notification.router,))
