
from cryptography.fernet import Fernet

fernet = Fernet(SECRET_KEY)

def generate_encrypted_url(file_id: int):
    return fernet.encrypt(str(file_id).encode()).decode()

def decrypt_url(token: str):
    return int(fernet.decrypt(token.encode()).decode())
