from utils.file_utils import *
from .recipe import show_recipe_detail

# List resep.csv
def get_recipe_list():
    return read_csv("data/resep.csv")

# Tambah resep admin
def add_admin_recipe():
    print("=== Tambah Resep ===")
    ingredients = read_lines("data/bahan.txt")
    
    # Bahan dasar
    while True:
        print("Pilih Bahan Dasar")
        for i in range(len(ingredients)):
            print(str(i+1) + ". " + ingredients[i])
        
        choice = input("Pilihanmu: ").strip()
        
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(ingredients):
                main_ingredient = ingredients[choice]
                break
        print("Pilihan tidak ditemukan")
    
    # Nama resep
    recipes = get_recipe_list()[1:]  # Skip header
    while True:
        recipe_name = input("Masukkan nama resep: ").strip()
        exists = False
        
        for recipe in recipes:
            if recipe_name == recipe[1]:
                print("Resep sudah ada. Silakan masukkan nama resep kembali")
                exists = True
                break
        
        if not exists:
            if recipe_name == "":
                print("Nama resep tidak boleh kosong. Silakan masukkan nama resep kembali")
            else:
                break
    
    # Bahan-bahan 
    while True:
        recipe_ingredients = input("Masukkan bahan-bahan (pisahkan dengan titik koma ';'): ").strip()
        if recipe_ingredients == "":
            print("Bahan-bahan tidak boleh kosong. Silakan masukkan bahan kembali")
        else:
            break
    
    # Langkah-langkah
    while True:
        steps = input("Masukkan langkah-langkah (pisahkan dengan titik koma ';'): ").strip()
        if steps == "":
            print("Langkah-langkah tidak boleh kosong. Silakan masukkan langkah kembali")
        else:
            break
    
    recipe_data = {
        "nama": recipe_name,
        "bahan": recipe_ingredients.split(";"),
        "langkah": steps.split(";")
    }
    
    show_recipe_detail(recipe_data)
    print("="*50)
    print("1. Simpan resep")
    print("2. Hapus resep")
    confirm = input("Pilihanmu: ").strip()
    
    if confirm == "1":
        new_recipe = f"{main_ingredient},{recipe_name},{recipe_ingredients},{steps}"
        append_data("data/resep.csv", new_recipe)
        print("\nResep berhasil di tambahkan")
    elif confirm == "2":
        print("Resep batal disimpan")
    else:
        print("Pilihan tidak ditemukan")

# Hapus resep admin
def delete_admin_recipe():
    recipes = get_recipe_list()[1:]  # Skip header
    
    if not recipes:
        print("Tidak ada resep untuk dihapus")
        return
    
    print("Pilih resep yang ingin dihapus: ")
    for i in range(len(recipes)):
        print(f"{i+1}. {recipes[i][1]}")
    
    choice = input("Pilihanmu: ").strip()
    
    if choice.isdigit():
        choice = int(choice) - 1
        if 0 <= choice < len(recipes):
            recipes.pop(choice)
            
            # Write back with header
            header = ["bahan_dasar", "nama_resep", "bahan_tambahan", "langkah-langkah"]
            write_csv("data/resep.csv", recipes, header)
            print("Resep berhasil dihapus!")
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")

# Mengubah resep admin
def edit_admin_recipe():
    recipes = get_recipe_list()[1:]  # Skip header
    
    if not recipes:
        print("Tidak ada resep untuk diubah")
        return
    
    print("Pilih resep yang ingin diubah: ")
    for i in range(len(recipes)):
        print(f"{i+1}. {recipes[i][1]}")
    
    choice = input("Pilihanmu: ").strip()
    
    if choice.isdigit():
        choice = int(choice) - 1
        if 0 <= choice < len(recipes):
            while True:
                recipe_data = {
                    "nama": recipes[choice][1],
                    "bahan": recipes[choice][2].split(";"),
                    "langkah": recipes[choice][3].split(";")
                }
                
                show_recipe_detail(recipe_data)
                print("\nYang ingin diubah:")
                print("1. Nama resep")
                print("2. Bahan-bahan")
                print("3. Langkah-langkah")
                print("4. Selesai")
                
                edit_choice = input("Pilihanmu: ").strip()
                
                if edit_choice == "1":
                    while True:
                        new_name = input("Masukkan nama resep: ").strip()
                        exists = False
                        
                        for i, recipe in enumerate(recipes):
                            if i != choice and new_name == recipe[1]:
                                print("Nama resep sama. Silakan masukkan nama resep kembali")
                                exists = True
                                break
                        
                        if not exists:
                            if new_name == "":
                                print("Nama resep tidak boleh kosong. Silakan masukkan nama resep kembali")
                            else:
                                recipes[choice][1] = new_name
                                break
                elif edit_choice == "2":
                    while True:
                        new_ingredients = input("Masukkan bahan-bahan (pisahkan dengan titik koma ';'): ").strip()
                        if new_ingredients == "":
                            print("Bahan-bahan tidak boleh kosong. Silakan masukkan bahan kembali")
                        else:
                            recipes[choice][2] = new_ingredients
                            break
                elif edit_choice == "3":
                    while True:
                        new_steps = input("Masukkan langkah-langkah (pisahkan dengan titik koma ';'): ").strip()
                        if new_steps == "":
                            print("Langkah-langkah tidak boleh kosong. Silakan masukkan langkah kembali")
                        else:
                            recipes[choice][3] = new_steps
                            break
                elif edit_choice == "4":
                    break
                else:
                    print("Pilihan tidak ditemukan")
            
            # Tampilkan hasil
            recipe_data = {
                "nama": recipes[choice][1],
                "bahan": recipes[choice][2].split(";"),
                "langkah": recipes[choice][3].split(";")
            }
            show_recipe_detail(recipe_data)
            
            # Simpan perubahan
            header = ["bahan_dasar", "nama_resep", "bahan_tambahan", "langkah-langkah"]
            write_csv("data/resep.csv", recipes, header)
            print("Resep berhasil diubah!")
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")

# Menu admin
def admin_menu(index, data):
    while True:
        print(f"\n=== Halo Admin {data[index][3]}, Selamat datang di Mira Apps ===")
        print("My Intelligence Recipe Assistant")
        print("\nApa yang ingin kamu lakukan sekarang?")
        print("1. Menambah resep")
        print("2. Menghapus resep")
        print("3. Mengubah resep")
        print("4. Log Out")
        
        choice = input("Pilihanmu: ").strip()
        
        if choice == "1":
            add_admin_recipe()
        elif choice == "2":
            delete_admin_recipe()
        elif choice == "3":
            edit_admin_recipe()
        elif choice == "4":
            print("Terimakasih telah menggunakan Mira Apps\n")
            break
        else:
            print("Pilihan tidak ditemukan")