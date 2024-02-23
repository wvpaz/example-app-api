import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from src.config.env_config import EnvSettings

settings = EnvSettings()

certificate = {
    "type": "service_account",
    "project_id": settings.env_project_id,
    "private_key_id": settings.env_private_key_id,
    "private_key": settings.env_private_key,
    "client_email": settings.env_client_email,
    "client_id": settings.env_client_id,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": settings.env_client_cert_url,
    "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(certificate)
firebase_admin.initialize_app(cred)

db = firestore.client()