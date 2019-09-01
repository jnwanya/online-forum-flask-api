from app.main import bcrypt


def hash_value(value: str):
    return bcrypt.generate_password_hash(value, 12).decode('utf-8')


def match_hashed_value(plain_value: str, hashed_value: str):
    return bcrypt.check_password_hash(hashed_value, plain_value)
