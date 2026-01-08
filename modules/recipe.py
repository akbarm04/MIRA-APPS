from utils.file_utils import *
from . import comment, bookmark

# Fungsi menampilkan bahan
def show_ingredients():
    ingredients = read_lines("data/bahan.txt")
    print("\n=== PILIH BAHAN YANG KAMU PUNYA ===")
    for i in range(len(ingredients)):
        print(str(i+1) + ". " + ingredients[i])
    return ingredients

# Fungsi memilih bahan
def choose_ingredients(ingredients):
    choices = input("Masukkan nomor bahan: ").split(",")
    user_ingredients = []

    for choice in choices:
        if choice.strip().isdigit():
            index = int(choice.strip()) - 1 
            if 0 <= index < len(ingredients):
                user_ingredients.append(ingredients[index])

    return user_ingredients

# Fungsi cari resep
def find_recipes(user_ingredients):
    results = []
    data = read_csv("data/resep.csv")

    for i in range(1, len(data)):
        row = data[i]
        main_ingredient = row[0]
        name = row[1]
        ingredients = row[2].split(";")
        steps = row[3].split(";")

        if main_ingredient not in user_ingredients:
            continue

        match_count = 0
        for ing in user_ingredients:
            if ing in ingredients:
                match_count += 1

        results.append({
            "nama": name,
            "bahan": ingredients,
            "langkah": steps,
            "cocok": match_count
        })

    return results

# TAMPILKAN DAFTAR RESEP
def choose_recipe(results):
    print("\n=== REKOMENDASI RESEP ===")
    for i in range(len(results)):
        print(str(i+1) + ". " + results[i]["nama"])
    print(f"{len(results)+1}. Back" )
    
    choice = input("Pilih nomor resep: ")
    if choice.isdigit():
        choice = int(choice) - 1
        if choice == len(results):
            return None
        elif 0 <= choice < len(results):
            return results[choice]
    
    return None

# DETAIL RESEP
def show_recipe_detail(recipe):
    print("\n=== DETAIL RESEP ===")
    print("Nama:", recipe["nama"])

    print("\nBahan:")
    for ingredient in recipe["bahan"]:
        print("- " + ingredient)

    print("\nLangkah Memasak:")
    for i in range(len(recipe["langkah"])):
        print(str(i+1) + ". " + recipe["langkah"][i])

# Alur pencarian resep
def search_recipe_flow(index, data):
    ingredients = show_ingredients()
    user_ingredients = choose_ingredients(ingredients)
    
    results = find_recipes(user_ingredients)

    if len(results) == 0:
        print("Tidak ada resep yang cocok.")
    else:
        while True:
            recipe = choose_recipe(results)
            if recipe is None:
                break
            
            show_recipe_detail(recipe)
            while True:
                print("\n1. Melihat dan menulis comment")
                print("2. Masukkan ke dalam Bookmark")
                print("3. Back")
                
                choice = input("Pilih: ").strip()
                if choice == "1":
                    comment.manage_comments(recipe, index, data)
                elif choice == "2":
                    bookmark.add_bookmark(recipe, index, data)
                elif choice == "3":
                    break
                else:
                    print("Pilihan tidak ditemukan")

# Tambah resep pribadi
def add_personal_recipe(index, data):
    print("=== Tambah Resep Pribadi ===")
    personal_recipes = read_data("data/resep_user.txt")
    
    while True:
        recipe_name = input("Masukkan nama resep: ").strip()
        exists = False
        for recipe in personal_recipes:
            if recipe_name == recipe[1]:
                print("Resep sudah ada")
                return
        
        if recipe_name == "":
            print("Nama resep tidak boleh kosong. Silakan masukkan nama resep kembali")
        else:
            break
    
    while True:
        ingredients = input("Masukkan bahan-bahan (pisahkan dengan titik koma ';'): ").strip()
        if ingredients == "":
            print("Bahan-bahan tidak boleh kosong. Silakan masukkan bahan kembali")
        else:
            break
    
    while True:
        steps = input("Masukkan langkah-langkah (pisahkan dengan titik koma ';'): ").strip()
        if steps == "":
            print("Langkah-langkah tidak boleh kosong. Silakan masukkan langkah kembali")
        else:
            break
    
    recipe = {
        "nama": recipe_name,
        "bahan": ingredients.split(";"),
        "langkah": steps.split(";")
    }
    
    show_recipe_detail(recipe)
    print("="*50)
    print("1. Simpan resep")
    print("2. Hapus resep")
    confirm = input("Pilihanmu: ").strip()
    
    if confirm == "1":
        new_recipe = f"{data[index][0]}|{recipe_name}|{ingredients}|{steps}"
        append_data("data/resep_user.txt", new_recipe)
        print("\nResep berhasil di tambahkan")
    elif confirm == "2":
        print("Resep batal disimpan")
    else:
        print("Pilihan tidak ditemukan")