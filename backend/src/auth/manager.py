from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas
from config import SECRET_KEY
from auth.models import Person
from auth.utils import get_user_db

from auth.generate_id import generate_tag_id

import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class UserManager(IntegerIDMixin, BaseUserManager[Person, int]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, person: Person, request: Optional[Request] = None):
        print(f"User {person.id} has registered.")
        await self.send_welcome_email(person)

    async def send_welcome_email(self, person: Person):
        sender_email = "notabane001@gmail.com"
        sender_password = "lbfbjwlgafkdvdef"  # приложение-пароль без пробелов
        subject = f"{person.person_name} добро пожаловать в Каленфи!"
        body = "Спасибо что зарегистрировались в нашем продукте!"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = person.email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            smtp = aiosmtplib.SMTP(hostname="smtp.gmail.com", port=465, use_tls=True)
            await smtp.connect()
            await smtp.login(sender_email, sender_password)
            await smtp.send_message(msg)
            await smtp.quit()
            print(f"Email sent to {person.email}")
        except Exception as e:
            print(f"Failed to send email to {person.email}: {e}")

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        user_dict["tag_id"] = generate_tag_id()
        user_dict["premium"] = False

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)