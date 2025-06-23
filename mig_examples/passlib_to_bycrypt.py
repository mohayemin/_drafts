
import bcrypt

def password_valid(actual_pw, check):
    pwd_hash = actual_pw.decode('utf8').encode('utf8')
    return bcrypt.hashpw(check, pwd_hash) == pwd_hash

def set_password(new_pw):
    new_pw = new_pw.encode('utf8')
    hashed_pw = bcrypt.hashpw(new_pw, bcrypt.gensalt())
    return hashed_pw
