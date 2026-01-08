from .validation import cek_email_valid, cek_username_valid
from utils.file_utils import baca_data, tambah_data

# Fungsi untuk mencari index email
def cari_index_email(list_user, cari_email):
    for i in range(len(list_user)):
        if list_user[i][1] == cari_email:
            return i
    return -1

# Fungsi untuk mencari index username
def cari_index_username(list_user, cari_username):
    for i in range(len(list_user)):
        if list_user[i][0] == cari_username:
            return i
    return -1

# Fungsi login user
def login_user():
    data_user = baca_data("data/data_user.txt")
    print("\n=== Lakukan Login ===")
    key_user = input("Masukkan Email atau Username: ").strip()
    #cek apakah email atau username
    if "@" in key_user:
        index_user = cari_index_email(data_user, key_user)
    else:
        key_user = key_user.lower()
        index_user = cari_index_username(data_user, key_user)

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
    data_user = baca_data("data/data_user.txt")
    # Memasukkan email baru
    while True:
        print("\n=== Lakukan Register ===")
        email_baru = input("Masukkan Email: ").strip()
        email_valid = cek_email_valid(email_baru)
        index_email = cari_index_email(data_user, email_baru)
        
        if index_email == -1 and email_valid:
            break
        elif email_baru == "":
            print("\nEmail tidak boleh kosong, silahkan isi")
        elif not email_valid:
            print("\nFormat email salah, silahkan masukkan email yang benar")
        else:
            print("\nEmail sudah ada, silahkan gunakan email lain.")

    # Memasukkan username baru
    while True:
        username_baru = input("Masukkan Username: ").lower().strip()
        username_valid = cek_username_valid(username_baru)
        index_username = cari_index_username(data_user, username_baru)
        
        if index_username == -1 and username_valid:
            break
        elif username_baru == "":
            print("\nUsername tidak boleh kosong, silahkan isi")
        elif not username_valid:
            print('\nUsername hanya bisa diisi huruf, angka, titik "." dan underscore "_"')
        elif username_baru == "." or username_baru == "_" or username_baru == "._" or username_baru == "_.":
            print("Format username salah")
        else:
            print("\nUsername sudah terpakai, silahkan gunakan yang lain")

    # Memasukkan password baru
    while True:
        password_baru = input("Masukkan Password: ").strip()
        if password_baru == "":
            print("\nPassword tidak boleh kosong, silahkan isi")
        else: 
            break
    
    # Memasukkan profile name
    while True:
        profile_name_baru = input("Masukkan Profile Name: ").strip()
        if profile_name_baru == "":
            print("\nProfile Name tidak boleh kosong, silahkan isi")
        elif "|" in profile_name_baru:
            print('Nama tidak boleh mengandung "|"')
        else: 
            break
    
    new_data_user = f"{username_baru}|{email_baru}|{password_baru}|{profile_name_baru}"
    with open ("data_user.txt", "a") as file:
        file.write(f"{new_data_user}\n")
    print("\nRegister berhasil")

#login untuk admin
def login_admin():
    data_admin = ambil_data_admin()
    while True:
        print("\n=== Lakukan Login ===")
        key_user = input("Masukkan Email atau Username: ")
        #cek apakah email atau username
        if "@" in key_user:
            key_user = key_user
            index_user = cari_index_email(data_admin, key_user)
        else:
            key_user = key_user.lower()
            index_user = cari_index_username(data_admin, key_user)

        password = input("Masukkan Password: ")
        if index_user != -1:
            if (key_user == data_admin[index_user][1] and password == data_admin [index_user][2]) or (key_user == data_admin[index_user][0] and password == data_admin [index_user][2]):
                print("Selamat anda berhasil Login")
                return True, index_user, data_admin
            else:
                print("\nPassword salah!")
                return False, -1, data_admin
        else:
            print("\nEmail atau Username tidak ditemukan!")
            return False, -1, data_admin