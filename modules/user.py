from . import recipe, comment, bookmark, profile
from utils.file_utils import baca_data

def menu_user(index, data):
    while True:
        print(f"\n=== Halo {data[index][3]}, Selamat datang di Mira Apps ===")
        print("My Intelligence Recipe Assistant\n\nApa yang ingin kamu lakukan sekarang?")
        print("1. Mencari resep\n2. Menulis resep\n3. Profile\n4. Log Out")
        
        pilihan = input("Pilihanmu: ").strip()
        
        if pilihan == "1":
            recipe.alur_cari_resep(index, data)
        elif pilihan == "2":
            recipe.tambah_resep_pribadi(index, data)
        elif pilihan == "3":
            profile.menu_profile(index, data)
        elif pilihan == "4":
            print("Terimakasih telah menggunakan Mira Apps\n")
            return
        else:
            print("Pilihan tidak ditemukan")