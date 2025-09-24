import os

from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

DATABASE_URL = os.getenv("DATABASE_URL")

mail_conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD"),
    MAIL_FROM = os.getenv("MAIL_FROM"),
    MAIL_PORT = os.getenv("MAIL_PORT"),
    MAIL_SERVER = os.getenv("MAIL_SERVER"),
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
)
