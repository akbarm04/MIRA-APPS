# modules/validation.py

def valid_email(email):
    valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._"

    if email == "@." or email == ".@":
        return False
    
    if "@" and "." not in email:
        return False
    
    for char in email:
        if char not in valid:
            return False
    return True

def valid_username(username):
    valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._"
    for char in username:
        if char not in valid:
            return False
    return True