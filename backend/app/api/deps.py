import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.db import get_db
from app.core.config import settings
from app.models.user import User

bearer_scheme = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
) -> User:

    unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"}
    )

    token = credentials.credentials
    try:
        #decode recalculates the sig from header and payload with secret key
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except InvalidTokenError:
        raise unauthorized
    
    #sub reads the user id from the payload
    user_id = payload.get("sub")
    if user_id is None:
        raise unauthorized

    #Tries to get the user object using the key
    user = db.get(User, int(user_id))
    if user is None:
        raise unauthorized
    return user
