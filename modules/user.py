from . import recipe, comment, bookmark, profile
from utils.file_utils import *

def user_menu(index, data):
    while True:
        print(f"\n=== Halo {data[index][3]}, Selamat datang di Mira Apps ===")
        print("My Intelligence Recipe Assistant\n\nApa yang ingin kamu lakukan sekarang?")
        print("1. Mencari resep\n2. Menulis resep\n3. Profile\n4. Log Out")
        
        choice = input("Pilihanmu: ").strip()
        
        if choice == "1":
            recipe.search_recipe_flow(index, data)
        elif choice == "2":
            recipe.add_personal_recipe(index, data)
        elif choice == "3":
            profile.profile_menu(index, data)
        elif choice == "4":
            print("Terimakasih telah menggunakan Mira Apps\n")
            return
        else:
            print("Pilihan tidak ditemukan")