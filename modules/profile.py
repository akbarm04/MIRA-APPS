from utils.file_utils import *
from . import bookmark
from .recipe import show_recipe_detail

# Ganti Profile Name
def change_profile_name(user_data, user_index):
    print(f"Profile name sekarang: {user_data[user_index][3]}")
    
    while True:
        new_name = input("Silahkan masukkan Profile Name baru anda: ").strip()
        
        if new_name == "":
            print("Nama tidak boleh kosong")
        elif "|" in new_name:
            print('Nama tidak boleh mengandung "|"')
        elif user_data[user_index][3] == new_name:
            print("Nama sama. Silakan masukkan nama baru")
        else: 
            # Mengganti nama di data_user.txt
            user_data[user_index][3] = new_name
            write_data("data/data_user.txt", user_data)

            # Mengganti nama di comment.txt
            comments = read_data("data/comment.txt")
            for comment in comments:
                if comment[2] == user_data[user_index][0]:
                    comment[1] = new_name
            write_data("data/comment.txt", comments)
            
            print(f"Profile Name berhasil diganti")
            break

# Data resep pribadi user
def get_user_personal_recipes(user_index, user_data):
    all_recipes = read_data("data/resep_user.txt")
    user_recipes = []
    
    for recipe in all_recipes:
        if recipe[0] == user_data[user_index][0]:
            user_recipes.append(recipe)
    
    return user_recipes

# Detail resep pribadi user
def show_personal_recipe_detail(recipe_name):
    recipes = read_data("data/resep_user.txt")
    
    for recipe in recipes:
        if recipe[1] == recipe_name:
            recipe_data = {
                "nama": recipe[1],
                "bahan": recipe[2].split(";"),
                "langkah": recipe[3].split(";")
            }
            show_recipe_detail(recipe_data)
            break

# Hapus resep pribadi
def delete_personal_recipe(user_index, user_data, recipe_name):
    all_recipes = read_data("data/resep_user.txt")
    
    for i in range(len(all_recipes)):
        if (user_data[user_index][0] == all_recipes[i][0] and 
            recipe_name == all_recipes[i][1]):
            all_recipes.pop(i)
            write_data("data/resep_user.txt", all_recipes)
            print("Resep pribadi berhasil dihapus!")
            break

# Resep pribadi di profile
def manage_personal_recipes(user_index, user_data):
    while True:
        user_recipes = get_user_personal_recipes(user_index, user_data)
        
        if not user_recipes:
            print("\nBelum ada Resep Pribadi!!")
            return
        
        print("\nResep Pribadimu:")
        for i in range(len(user_recipes)):
            print(f"{i+1}. {user_recipes[i][1]}")
        print(f"{len(user_recipes)+1}. Back")
        
        last_selected = None
        
        choice = input("Pilihanmu: ").strip()
        if choice.isdigit():
            choice = int(choice) - 1
            
            if choice == len(user_recipes):  # Back
                return
            elif choice in range(len(user_recipes)):
                show_personal_recipe_detail(user_recipes[choice][1])
                last_selected = user_recipes[choice][1]
                
                # Tanya apakah mau hapus
                delete_choice = input("\nApakah ingin menghapus resep ini? (y/n): ").strip().lower()
                if delete_choice == 'y':
                    delete_personal_recipe(user_index, user_data, last_selected)
            else:
                print("Pilihan tidak ditemukan")
        else:
            print("Pilihan tidak ditemukan")

# Menu profile
def profile_menu(user_index, user_data):
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
        
        choice = input("Pilihanmu: ").strip()
        
        if choice == "1":
            bookmark_menu(user_index, user_data)
        elif choice == "2":
            manage_personal_recipes(user_index, user_data)
        elif choice == "3":
            change_profile_name(user_data, user_index)
        elif choice == "4":
            break
        else:
            print("Pilihan tidak ditemukan")

def bookmark_menu(user_index, user_data):
    while True:
        print("\n1. Melihat Bookmark")
        print("2. Menghapus Bookmark")
        print("3. Back")
        
        choice = input("Pilihanmu: ").strip()
        
        if choice == "1":
            if bookmark.show_user_bookmarks(user_index, user_data):
                bookmark.choose_bookmark(user_index, user_data)
        elif choice == "2":
            bookmark.delete_bookmark(user_index, user_data)
        elif choice == "3":
            break
        else:
            print("Pilihan tidak ditemukan")