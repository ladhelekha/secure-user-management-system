import bcrypt
import base64


def verify_password(input_password, hashed_password_base64):
    hashed_password = base64.b64decode(hashed_password_base64.encode('utf-8'))
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

def get_password_hash(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    hashed_password = base64.b64encode(hashed_password).decode('utf-8')
    return hashed_password