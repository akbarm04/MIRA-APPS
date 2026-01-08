from utils.file_utils import *
from . import recipe

# Fungsi mengambil data bookmark
def get_bookmarks():
    return read_data("data/bookmark.txt")

# Cek isi bookmark apakah sudah ada
def check_bookmark_exists(recipe, user_index, user_data):
    bookmarks = get_bookmarks()
    
    for bookmark in bookmarks:
        if bookmark[0] == user_data[user_index][0] and bookmark[1] == recipe["nama"]:
            return True
    return False

# Memasukkan resep ke bookmark
def add_bookmark(recipe, user_index, user_data):
    exists = check_bookmark_exists(recipe, user_index, user_data)
    
    if not exists:
        append_data("data/bookmark.txt", f"{user_data[user_index][0]}|{recipe['nama']}")
        print("Resep berhasil dimasukkan ke dalam bookmark")
    else:
        print("Resep sudah ada di bookmark")

# Isi bookmark user
def get_user_bookmarks(user_index, user_data):
    all_bookmarks = get_bookmarks()
    user_bookmarks = []
    
    for bookmark in all_bookmarks:
        if bookmark[0] == user_data[user_index][0]:
            user_bookmarks.append(bookmark)
    
    return user_bookmarks

# Buka detail resep dari bookmark
def show_bookmark_detail(recipe_name):
    recipes = read_csv("data/resep.csv")
    
    for recipe in recipes[1:]:
        if recipe[1] == recipe_name:
            recipe_data = {
                "nama": recipe[1],
                "bahan": recipe[2].split(";"),
                "langkah": recipe[3].split(";")
            }
            recipe.show_recipe_detail(recipe_data)
            break

# Tampilkan bookmark di profile
def show_user_bookmarks(user_index, user_data):
    user_bookmarks = get_user_bookmarks(user_index, user_data)
    
    if not user_bookmarks:
        print("\nBelum ada Bookmark!!")
        return False
    
    print("\nBookmarkmu:")
    for i in range(len(user_bookmarks)):
        print(f"{i+1}. {user_bookmarks[i][1]}")
    
    return True

# Pilih bookmark user
def choose_bookmark(user_index, user_data):
    user_bookmarks = get_user_bookmarks(user_index, user_data)
    choice = input("Pilihanmu: ").strip()
    
    if choice.isdigit():
        choice = int(choice) - 1
        if 0 <= choice < len(user_bookmarks):
            show_bookmark_detail(user_bookmarks[choice][1])
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")

# Hapus bookmark
def delete_bookmark(user_index, user_data):
    all_bookmarks = get_bookmarks()
    user_bookmarks = get_user_bookmarks(user_index, user_data)
    
    if not user_bookmarks:
        print("Belum ada bookmark")
        return
    
    if show_user_bookmarks(user_index, user_data):
        choice = input("Pilihanmu: ").strip()
        
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(user_bookmarks):
                # Hapus dari list
                for i in range(len(all_bookmarks)):
                    if (user_data[user_index][0] == all_bookmarks[i][0] and 
                        user_bookmarks[choice][1] == all_bookmarks[i][1]):
                        all_bookmarks.pop(i)
                        break
                
                # Tulis ulang file
                write_data("data/bookmark.txt", all_bookmarks)
                print("Resep berhasil dihapus")
            else:
                print("Pilihan tidak ditemukan")
        else:
            print("Pilihan tidak ditemukan")