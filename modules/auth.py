from .validation import *
from utils.file_utils import *

# Fungsi untuk mencari index email
def find_email_index(user_list, email):
    for i in range(len(user_list)):
        if user_list[i][1] == email:
            return i
    return -1

# Fungsi untuk mencari index username
def find_username_index(user_list, username):
    for i in range(len(user_list)):
        if user_list[i][0] == username:
            return i
    return -1

# Fungsi login user
def login_user():
    data_user = read_data("data/data_user.txt")
    while True:
        print("\n=== Lakukan Login ===")
        key_user = input("Masukkan Email atau Username: ").strip()
        
        if "@" in key_user:
            index_user = find_email_index(data_user, key_user)
        else:
            key_user = key_user.lower()
            index_user = find_username_index(data_user, key_user)

        password = input("Masukkan Password: ").strip()
        
        if index_user != -1:
            if (key_user == data_user[index_user][1] and password == data_user[index_user][2]) or \
               (key_user == data_user[index_user][0] and password == data_user[index_user][2]):
                print("Selamat anda berhasil Login")
                return True, index_user, data_user
            else:
                print("\nPassword salah!")
                return False, -1, data_user
        else:
            print("\nEmail atau Username tidak ditemukan!")
            return False, -1, data_user

# Fungsi register user
def register_user():
    data_user = read_data("data/data_user.txt")
    
    # Memasukkan email baru
    while True:
        print("\n=== Lakukan Register ===")
        new_email = input("Masukkan Email: ").strip()
        is_email_valid = is_valid_email(new_email)
        email_index = find_email_index(data_user, new_email)
        
        if email_index == -1 and is_email_valid:
            break
        elif new_email == "":
            print("\nEmail tidak boleh kosong, silahkan isi")
        elif not is_email_valid:
            print("\nFormat email salah, silahkan masukkan email yang benar")
        else:
            print("\nEmail sudah ada, silahkan gunakan email lain.")

    # Memasukkan username baru
    while True:
        new_username = input("Masukkan Username: ").lower().strip()
        is_username_valid = is_valid_username(new_username)
        username_index = find_username_index(data_user, new_username)
        
        if username_index == -1 and is_username_valid:
            break
        elif new_username == "":
            print("\nUsername tidak boleh kosong, silahkan isi")
        elif not is_username_valid:
            print('\nUsername hanya bisa diisi huruf, angka, titik "." dan underscore "_"')
        elif new_username in [".", "_", "._", "_."]:
            print("Format username salah")
        else:
            print("\nUsername sudah terpakai, silahkan gunakan yang lain")

    # Memasukkan password baru
    while True:
        new_password = input("Masukkan Password: ").strip()
        if new_password == "":
            print("\nPassword tidak boleh kosong, silahkan isi")
        else: 
            break
    
    # Memasukkan profile name
    while True:
        new_profile_name = input("Masukkan Profile Name: ").strip()
        if new_profile_name == "":
            print("\nProfile Name tidak boleh kosong, silahkan isi")
        elif "|" in new_profile_name:
            print('Nama tidak boleh mengandung "|"')
        else: 
            break
    
    new_user_data = f"{new_username}|{new_email}|{new_password}|{new_profile_name}"
    append_data("data/data_user.txt", new_user_data)
    print("\nRegister berhasil")

# Fungsi login admin
def login_admin():
    data_admin = read_data("data/data_admin.txt")
    while True:
        print("\n=== Lakukan Login ===")
        key_user = input("Masukkan Email atau Username: ").strip()
        
        if "@" in key_user:
            index_user = find_email_index(data_admin, key_user)
        else:
            key_user = key_user.lower()
            index_user = find_username_index(data_admin, key_user)

        password = input("Masukkan Password: ").strip()
        
        if index_user != -1:
            if (key_user == data_admin[index_user][1] and password == data_admin[index_user][2]) or \
               (key_user == data_admin[index_user][0] and password == data_admin[index_user][2]):
                print("Selamat anda berhasil Login")
                return True, index_user, data_admin
            else:
                print("\nPassword salah!")
                return False, -1, data_admin
        else:
            print("\nEmail atau Username tidak ditemukan!")
            return False, -1, data_admin