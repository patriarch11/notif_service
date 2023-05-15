from dataclasses import dataclass
from typing import Any

import jwt
from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


@dataclass(frozen=True, slots=True)
class JWTData:
    token: str
    user_id: str


@dataclass(frozen=True, slots=True)
class JWTConfig:
    client_id: str
    client_secret: str
    issuer: str
    algorithm: str


class JWTMiddleware(HTTPBearer):
    config: JWTConfig

    def __init__(self, config: JWTConfig):
        super().__init__()
        self.config = config

    async def __call__(self, request: Request) -> JWTData:
        credentials: HTTPAuthorizationCredentials = await super(JWTMiddleware, self).__call__(request)
        try:
            token = credentials.credentials
            decoded_token = self.verify_token(token)
            user_id = decoded_token.get("sub")
            return JWTData(token=credentials.credentials, user_id=user_id)
        except Exception:
            raise HTTPException(status_code=401, detail="invalid token")

    def verify_token(self, token: str) -> dict[str, Any]:
        try:
            decoded_token = jwt.decode(token,
                                       audience=[self.config.client_id],
                                       issuer=self.config.issuer,
                                       key=self.config.client_secret,
                                       algorithms=[self.config.algorithm],
                                       verify=True,
                                       options={
                                           "verify_iat": True,
                                           "verify_nbf": True,
                                           "verify_exp": True,
                                           "verify_iss": True,
                                           "verify_aud": True,
                                       }
                                       )
        except Exception:
            raise HTTPException(status_code=401, detail="invalid token")
        if decoded_token.get("client") != self.config.client_id:
            raise HTTPException(status_code=401, detail="invalid token")
        return decoded_token
