from notification_service.settings.settings import *

__settings__ = Settings(_env_file=".env", _env_file_encoding="utf-8")

__smtp_setting__ = SMTPSettings(_env_file=".env", _env_file_encoding="utf-8")
