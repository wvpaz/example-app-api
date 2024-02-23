from pydantic_settings import BaseSettings, SettingsConfigDict

class EnvSettings(BaseSettings):
    env_private_key_id: str = ''
    env_private_key: str = ''
    env_project_id: str = ''
    env_client_email: str = ''
    env_client_id: str = ''
    env_client_cert_url: str = ''
    
    model_config = SettingsConfigDict(env_file=".env")