from utils.file_utils import baca_data, tulis_data
from . import bookmark
from .recipe import tampil_detail_resep

# Ganti Profile Name
def ganti_nama_profile(user_data, user_index):
    print(f"Profile name sekarang: {user_data[user_index][3]}")
    
    while True:
        nama_baru = input("Silahkan masukkan Profile Name baru anda: ").strip()
        
        if nama_baru == "":
            print("Nama tidak boleh kosong")
        elif "|" in nama_baru:
            print('Nama tidak boleh mengandung "|"')
        elif user_data[user_index][3] == nama_baru:
            print("Nama sama. Silakan masukkan nama baru")
        else: 
            # Mengganti nama di data_user.txt
            user_data[user_index][3] = nama_baru
            tulis_data("data/data_user.txt", user_data)

            # Mengganti nama di comment.txt
            komentar = baca_data("data/comment.txt")
            for kom in komentar:
                if kom[2] == user_data[user_index][0]:
                    kom[1] = nama_baru
            tulis_data("data/comment.txt", komentar)
            
            print(f"Profile Name berhasil diganti")
            break

# Data resep pribadi user
def ambil_resep_pribadi_user(user_index, user_data):
    semua_resep = baca_data("data/resep_user.txt")
    resep_user = []
    
    for resep in semua_resep:
        if resep[0] == user_data[user_index][0]:
            resep_user.append(resep)
    
    return resep_user

# Detail resep pribadi user
def tampil_detail_resep_pribadi(nama_resep):
    resep_data = baca_data("data/resep_user.txt")
    
    for resep in resep_data:
        if resep[1] == nama_resep:
            resep_detail = {
                "nama": resep[1],
                "bahan": resep[2].split(";"),
                "langkah": resep[3].split(";")
            }
            tampil_detail_resep(resep_detail)
            break

# Hapus resep pribadi
def hapus_resep_pribadi(user_index, user_data, nama_resep):
    semua_resep = baca_data("data/resep_user.txt")
    
    for i in range(len(semua_resep)):
        if (user_data[user_index][0] == semua_resep[i][0] and 
            nama_resep == semua_resep[i][1]):
            semua_resep.pop(i)
            tulis_data("data/resep_user.txt", semua_resep)
            print("Resep pribadi berhasil dihapus!")
            break

# Resep pribadi di profile
def kelola_resep_pribadi(user_index, user_data):
    while True:
        resep_user = ambil_resep_pribadi_user(user_index, user_data)
        
        if len(resep_user) == 0:
            print("\nBelum ada Resep Pribadi!!")
            return
        
        print("\nResep Pribadimu:")
        for i in range(len(resep_user)):
            print(f"{i+1}. {resep_user[i][1]}")
        print(f"{len(resep_user)+1}. Back")
        
        pilihan = input("Pilihanmu: ").strip()
        if pilihan.isdigit():
            pilihan = int(pilihan) - 1
            
            if pilihan == len(resep_user):  # Back
                return
            elif pilihan >= 0 and pilihan < len(resep_user):
                tampil_detail_resep_pribadi(resep_user[pilihan][1])
                resep_terpilih = resep_user[pilihan][1]
                
                # Tanya apakah mau hapus
                pilihan_hapus = input("\nApakah ingin menghapus resep ini? (y/n): ").strip().lower()
                if pilihan_hapus == 'y':
                    hapus_resep_pribadi(user_index, user_data, resep_terpilih)
            else:
                print("Pilihan tidak ditemukan")
        else:
            print("Pilihan tidak ditemukan")

# Menu profile
def menu_profile(user_index, user_data):
    while True:
        print(f"\n========== PROFILE ==========")
        print(f"Profile Name: {user_data[user_index][3]}")
        print(f"Username: @{user_data[user_index][0]}")
        print(f"Email: {user_data[user_index][1]}")
        print("="*30)
        print("1. Bookmark")
        print("2. Resep Pribadi")
        print("3. Mengubah Profile Name")
        print("4. Back")
        
        pilihan = input("Pilihanmu: ").strip()
        
        if pilihan == "1":
            menu_bookmark(user_index, user_data)
        elif pilihan == "2":
            kelola_resep_pribadi(user_index, user_data)
        elif pilihan == "3":
            ganti_nama_profile(user_data, user_index)
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak ditemukan")

def menu_bookmark(user_index, user_data):
    while True:
        print("\n1. Melihat Bookmark")
        print("2. Menghapus Bookmark")
        print("3. Back")
        
        pilihan = input("Pilihanmu: ").strip()
        
        if pilihan == "1":
            if bookmark.tampil_bookmark_user(user_index, user_data):
                bookmark.pilih_bookmark_user(user_index, user_data)
        elif pilihan == "2":
            bookmark.hapus_bookmark(user_index, user_data)
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak ditemukan")