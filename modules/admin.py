from utils.file_utils import baca_baris, baca_csv, tulis_csv, tambah_data
from .recipe import detail_resep 

#ambil data Admin
def ambil_data_admin():
    with open("data_admin.txt", "r") as file:
        lines = file.readlines()
    data_user = []
    for line in lines:
        data_user.append(line.strip().split("|"))
    return data_user

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
        
#menu admin
def menu_admin(index, data):
    while True:
        print(f"\n=== Halo Admin {data[index][3]}, Selamat datang di Mira Apps ===\nMy Intelligence Recipe Assistant\n\nApa yang ingin kamu lakukan sekarang?")
        print("1. Menambah resep\n2. Menghapus resep\n3. Mengubah resep\n4. Log Out")
        pilih_menu_admin = input("Pilihanmu: ").strip()

        if pilih_menu_admin == "1":
            tambah_resep_admin()
        elif pilih_menu_admin == "2":
            hapus_resep_admin()
        elif pilih_menu_admin == "3":
            ubah_resep_admin()
        elif pilih_menu_admin == "4":
            print("Terimakasih telah menggunakan Mira Apps\n")
            break
        else:
            print("Pilihan tidak ditemukan")
