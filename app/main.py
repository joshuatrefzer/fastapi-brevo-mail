from fastapi import FastAPI

from pydantic import BaseModel

from app.services.brevo_service import (
    send_customer_mail,
    send_admin_mail,
)
app = FastAPI()

class Contact(BaseModel):
    name: str
    email: str
    message: str

@app.post("/contact")
def contact(contact: Contact):

    send_customer_mail(
        contact.name,
        contact.email
    )

    send_admin_mail(
        contact.name,
        contact.email,
        contact.message
    )

    return {
        "success": True
    }