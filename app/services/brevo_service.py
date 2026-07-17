from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from app.config import *

BASE_DIR = Path(__file__).resolve().parent.parent

env = Environment(
    loader=FileSystemLoader(BASE_DIR / "templates")
)

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key["api-key"] = BREVO_API_KEY




api = sib_api_v3_sdk.TransactionalEmailsApi(
    sib_api_v3_sdk.ApiClient(configuration)
)

def send_admin_mail(name, email, message):

    template = env.get_template("admin_notification.html")

    html = template.render(
        name=name,
        email=email,
        message=message
    )

    mail = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": ADMIN_MAIL}],
        sender={
            "email": MAIL_FROM,
            "name": MAIL_FROM_NAME
        },
        subject="Neue Anfrage",
        html_content=html,
        text_content=f"""
Hallo,
du hast eine neue Anfrage von {name} ({email}) erhalten:

{message}
"""
    )

    api.send_transac_email(mail)
    
    
def send_customer_mail(name, email):

    template = env.get_template("customer_confirmation.html")

    html = template.render(
        name=name
    )

    mail = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": email}],
        sender={
            "email": MAIL_FROM,
            "name": MAIL_FROM_NAME
        },
        reply_to={
            "email": ADMIN_MAIL,
            "name": MAIL_FROM_NAME
        },
        subject="Vielen Dank für deine Anfrage",
        html_content=html,
        text_content=f"""
Hallo {name},

wir haben deine Anfrage erhalten.
Vielen Dank für dein Interesse!

Ich melde mich so schnell wie möglich persönlich bei dir.

Liebe Grüße
Josh
"""
        
    )

    api.send_transac_email(mail)