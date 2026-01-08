# Fungsi untuk mengecek email sesuai format  
def is_valid_email(email):
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._"

    if email == "@." or email == ".@":
        return False
    
    if "@" not in email or "." not in email:
        return False
    
    for char in email:
        if char not in valid_chars:
            return False
    return True

# Fungsi cek username apakah valid
def is_valid_username(username):
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._"
    for char in username:
        if char not in valid_chars:
            return False
    return True