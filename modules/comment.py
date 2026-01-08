from utils.file_utils import *

# Fungsi filter comment
def filter_comment(text):
    comment_lower = text.lower()
    words = comment_lower.split()
    
    forbidden_words = read_lines("data/id_badwords.txt")
    
    for word in words:
        if word in forbidden_words:
            return -1
    
    if "|" in text:
        return -2
    
    return text

# Fungsi lihat comment sesuai resep 
def get_comments_for_recipe(recipe_name):
    all_comments = read_data("data/comment.txt")
    recipe_comments = []
    
    for comment in all_comments:
        if comment[0] == recipe_name:
            recipe_comments.append(comment)
    
    return recipe_comments

# Melihat dan menulis comment
def manage_comments(recipe, user_index, user_data):
    while True:
        recipe_comments = get_comments_for_recipe(recipe["nama"])
        
        if len(recipe_comments) > 0:
            for comment in recipe_comments:
                print("\n" + "=" * 50)
                print(f"Pengirim: {comment[1]}")
                print(f"Username: @{comment[2]}")
                print(f"Comment:\n{comment[3]}")
                print("=" * 50)
        else:
            print("\n" + "=" * 50)
            print("Belum ada comment di resep ini")
            print("=" * 50 + "\n")
        
        print("1. Menulis comment")
        print("2. Back")
        choice = input("Pilihanmu: ").strip()
        
        if choice == "1":
            comment_text = input("Silahkan tulis komentarmu:\n").strip()
            filtered_comment = filter_comment(comment_text)
            
            if comment_text == "":
                print("Komentar tidak boleh kosong")
            elif filtered_comment == -1:
                print("Dilarang menggunakan kata yang tidak pantas!")
                break
            elif filtered_comment == -2:
                print('Maaf tidak bisa menggunakan simbol "|"')
                break
            else:
                new_comment = f"{recipe['nama']}|{user_data[user_index][3]}|{user_data[user_index][0]}|{comment_text}"
                append_data("data/comment.txt", new_comment)
                print("\nComment berhasil di tambahkan")
                recipe_comments = get_comments_for_recipe(recipe["nama"])
                for comment in recipe_comments:
                    print("\n" + "=" * 50)
                    print(f"Pengirim: {comment[1]}")
                    print(f"Username: @{comment[2]}")
                    print(f"Comment:\n{comment[3]}")
                    print("=" * 50)
                break
        elif choice == "2":
            break
        else:
            print("Pilihan tidak ditemukan\n")