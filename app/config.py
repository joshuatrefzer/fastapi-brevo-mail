from dotenv import load_dotenv
import os

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
MAIL_FROM = os.getenv("MAIL_FROM")
MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME")
ADMIN_MAIL = os.getenv("ADMIN_MAIL")
