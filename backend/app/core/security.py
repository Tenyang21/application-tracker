from datetime import datetime, timedelta, timezone
import jwt
from pwdlib import PasswordHash
from app.core.config import settings

# PasswordHash is a class that provides a method to hash and verify passwords.
password_hash = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

# create_access_token is a function that creates a JWT token for a given user.
# copy the data, work out when it expires, add the expiry, sign it with the secret key, and return the token string.
def create_access_token(data: dict, time_delta: timedelta = None) -> str:
    to_encode = data.copy()
    if time_delta:
        expire = datetime.now(timezone.utc) + time_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    # encode_jwt retursn header, payload, and signature together as a single string.
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

# When a request comes in, the server takes the header + payload, 
# recalculates the signature using the secret key from its config, 
# and compares it with the signature in the token. If they match and the token hasn’t expired, 
# the server trusts it and reads the user ID from the payload.