import jwt
from datetime import timedelta, datetime

from app.models.user import User
from app.core.config import SECRET_KEY, JWT_ALGORITHM


def generate_token(user: User) -> str:
    payload = {
        'sub': str(user.id),
        'role': str(user.role),
        'exp': datetime.utcnow() + timedelta(minutes=15)
    }
    token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=JWT_ALGORITHM)

    return token
