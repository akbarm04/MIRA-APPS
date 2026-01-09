from .validation import valid_email, valid_username
from utils.file_utils import baca_data, tambah_data

border = "─" * 45
spasi = 45

# Fungsi mencari index email
def cari_index_email(list, cari):
    for i in range(len(list)):
        if list[i][1] == cari:
            return i
    return -1

# Fungsi mencari index username
def cari_index_username(list, cari):
    for i in range(len(list)):
        if list[i][0] == cari:
            return i
    return -1

# Fungsi ambil data user dari file
def ambildata():
    return baca_data("data/data_user.txt")

# Fungsi login
def login():
    data_user = ambildata()
    print(f"\n\n\n{border}")
    print("Lakukan Login".center(spasi))
    print(border)
    key_user = input("Masukkan Email atau Username: ").strip()
    
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

# Fungsi register
def register():
    data_user = ambildata()
    
    # Memasukkan email baru
    while True:
        print(f"\n\n\n{border}")
        print("Lakukan Register".center(spasi))
        print(border)
        new_email = input("Masukkan Email: ").strip()
        cek_email = valid_email(new_email)
        confirm_email = cari_index_email(data_user, new_email)
        
        if confirm_email == -1 and cek_email:
            break
        elif new_email == "":
            print("\nEmail tidak boleh kosong, silahkan isi")
        elif not cek_email:
            print("\nFormat email salah, silahkan masukkan email yang benar")
        else:
            print("\nEmail sudah ada, silahkan gunakan email lain.")

    # Memasukkan username baru
    while True:
        new_username = input("Masukkan Username: ").lower().strip()
        cek_username = valid_username(new_username)
        confirm_username = cari_index_username(data_user, new_username)
        
        if confirm_username == -1 and cek_username:
            break
        elif new_username == "":
            print("\nUsername tidak boleh kosong, silahkan isi")
        elif not cek_username:
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
    
    new_data_user = f"{new_username}|{new_email}|{new_password}|{new_profile_name}"
    tambah_data("data/data_user.txt", new_data_user)
    print("\nRegister berhasil")

# Ambil data Admin
def ambil_data_admin():
    return baca_data("data/data_admin.txt")

# Login untuk admin
def login_admin():
    data_admin = ambil_data_admin()
    print(f"\n\n\n{border}")
    print("Lakukan Login".center(spasi))
    print(border)
    key_user = input("Masukkan Email atau Username: ").strip()
    
    if "@" in key_user:
        index_user = cari_index_email(data_admin, key_user)
    else:
        key_user = key_user.lower()
        index_user = cari_index_username(data_admin, key_user)

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

# Alias untuk compatibility
login_user = login
register_user = register