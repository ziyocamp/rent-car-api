from fastapi_mail import FastMail, MessageSchema
from app.core.config import mail_conf


async def send_verification_code_to_email(email: str, verification_code: int):

    message = MessageSchema(
        subject="Verification Code",
        recipients=[email],
        body=f"Tasdiqlash kod: {verification_code}",
        subtype="plain"
    )

    fm = FastMail(mail_conf)
    await fm.send_message(message)
