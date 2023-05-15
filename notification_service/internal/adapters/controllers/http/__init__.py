from notification_service.middleware.jwt import JWTMiddleware, JWTConfig
from notification_service.settings import __jwt_settings__

config = JWTConfig(client_id="", client_secret="", issuer="", algorithm="")
jwt_middleware = JWTMiddleware(config=config)