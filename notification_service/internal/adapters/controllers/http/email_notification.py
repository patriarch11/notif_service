from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response

from notification_service.internal.adapters.controllers.http import jwt_middleware
from notification_service.internal.domain.interfaces.email_notification import EmailNotificationServiceInterface
from notification_service.internal.domain.models.email_notification import EmailNotification
from notification_service.internal.services.email_notification import get_email_notification_service

router = APIRouter()


@router.post("/send_email", status_code=200, response_class=Response, dependencies=[Depends(jwt_middleware)])
async def send_email_notification(notification: EmailNotification,
                                  email_notif_service: EmailNotificationServiceInterface = Depends(
                                      get_email_notification_service)):
    try:
        email_notif_service.send_email_notification(notification)
        return Response(status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
