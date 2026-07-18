from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.services.brevo_service import (
    send_customer_mail,
    send_admin_mail,
)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://joshuatrefzer.de"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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