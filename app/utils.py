from passlib.hash import argon2
pwd_context = argon2.using(rounds=4)
def hash_password(password: str):
    return pwd_context.hash(password)
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)