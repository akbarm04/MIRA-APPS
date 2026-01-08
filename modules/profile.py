# modules/profile.py

from utils.file_utils import baca_data, tulis_data

# Ganti Profile Name
def change_name(data, index):
    print(f"Profile name sekarang: {data[index][3]}")
    while True:
        change_name = input("Silahkan masukkan Profile Name baru anda: ").strip()
        if change_name == "":
            print("Nama tidak boleh kosong")
        elif "|" in change_name:
            print('Nama tidak boleh mengandung "|"')
        elif data[index][3] == change_name:
            print("Nama sama. Silakan masukkan nama baru")
        else: 
            # Mengganti nama di data_user.txt
            data[index][3] = change_name
            tulis_data("data/data_user.txt", data)

            # Mengganti nama di comment.txt
            from .comment import data_comment
            list_comment = data_comment()
            for j in range(len(list_comment)):
                if list_comment[j][2] == data[index][0]:
                    list_comment[j][1] = change_name
            tulis_data("data/comment.txt", list_comment)
            print(f"Profile Name berhasil diganti")
            break

# Data resep pribadi
def data_resep_pribadi():
    return baca_data("data/resep_user.txt")

# Data resep pribadi user
def resep_pribadi_user(index, data):
    list_resep_pribadi = data_resep_pribadi()
    list_resep_user = []
    for i in range(len(list_resep_pribadi)):
        if list_resep_pribadi[i][0] == data[index][0]:
            list_resep_user.append(list_resep_pribadi[i])
    return list_resep_user

# Detail resep pribadi user
def resep_pribadi_detail(nama):
    data = data_resep_pribadi()
    for line in data:
        if line[1] == nama:
            resep = {
                "nama": line[1],
                "bahan": line[2].split(";"),
                "langkah": line[3].split(";")
            }
            # Gunakan fungsi detail dari recipe
            from .recipe import detail_resep
            detail_resep(resep)
            break

# Menambah resep pribadi
def tambah_resep_pribadi(index, data, dari_profile=True):
    """Menambah resep pribadi"""
    print("=== Tambah Resep Pribadi ===")
    list_resep_pribadi = data_resep_pribadi()
    
    while True:
        nama_resep = input("Masukkan nama resep: ").strip()
        nama_ada = False
        for i in range(len(list_resep_pribadi)):
            if nama_resep == list_resep_pribadi[i][1]:
                print("Resep sudah ada")
                nama_ada = True
                break
        
        if nama_ada:
            return
        
        if nama_resep == "":
            print("Nama resep tidak boleh kosong. Silakan masukkan nama resep kembali")
        else:
            break
    
    while True:
        bahan_resep = input("Masukkan bahan-bahan (pisahkan dengan titik koma ';'): ").strip()
        if bahan_resep == "":
            print("Bahan-bahan tidak boleh kosong. Silakan masukkan bahan kembali")
        else:
            break
    
    while True:
        langkah_resep = input("Masukkan langkah-langkah (pisahkan dengan titik koma ';'): ").strip()
        if langkah_resep == "":
            print("Langkah-langkah tidak boleh kosong. Silakan masukkan langkah kembali")
        else:
            break
    
    from .recipe import detail_resep
    resep = {
        "nama": nama_resep,
        "bahan": bahan_resep.split(";"),
        "langkah": langkah_resep.split(";")
    }
    detail_resep(resep)

    confirm = input("="*50 + "\n1. Simpan resep\n2. Hapus resep\nPilihanmu: ").strip()
    if confirm == "1":
        new_resep = f"{data[index][0]}|{nama_resep}|{bahan_resep}|{langkah_resep}"
        from utils.file_utils import tambah_data
        tambah_data("data/resep_user.txt", new_resep)
        print("\nResep berhasil di tambahkan")
        
        if not dari_profile:
            print("Resep telah disimpan ke koleksi pribadimu!")
            
    elif confirm == "2":
        print("Resep batal disimpan")
    else:
        print("Pilihan tidak ditemukan")
    
    from .recipe import detail_resep
    resep = {
        "nama": nama_resep,
        "bahan": bahan_resep.split(";"),
        "langkah": langkah_resep.split(";")
    }
    detail_resep(resep)


# Hapus resep pribadi
def hapus_resep_pribadi(index, data, nama):
    list_data_resep_pribadi = data_resep_pribadi()
    for i in range(len(list_data_resep_pribadi)):
        if data[index][0] == list_data_resep_pribadi[i][0] and nama == list_data_resep_pribadi[i][1]:
            list_data_resep_pribadi.pop(i)
            tulis_data("data/resep_user.txt", list_data_resep_pribadi)
            print("Resep pribadi berhasil dihapus!")
            break

# Resep pribadi di profile
def profile_resep_pribadi(index, data):
    list_resep_pribadi = resep_pribadi_user(index, data)
    if not list_resep_pribadi:
        print("\nBelum ada Resep Pribadi!!")
        return -1
    else:
        last_pilih = None
        while True:
            list_resep_pribadi = resep_pribadi_user(index, data)
            print("\nResep Pribadimu:")
            for i in range(len(list_resep_pribadi)):
                print(f"{i+1}. {list_resep_pribadi[i][1]}")
            print(f"{len(list_resep_pribadi)+1}. Back")
            if last_pilih is not None:
                print(f"{len(list_resep_pribadi)+2}. Hapus resep")
            
            pilih_resep_pribadi = input("Pilihanmu: ")
            
            if pilih_resep_pribadi.isdigit():
                pilih_resep_pribadi = int(pilih_resep_pribadi)-1
                if pilih_resep_pribadi == len(list_resep_pribadi):
                    return
                elif pilih_resep_pribadi == len(list_resep_pribadi)+1 and last_pilih != None:
                    hapus_resep_pribadi(index, data, last_pilih)
                    last_pilih = None
                elif pilih_resep_pribadi in range(len(list_resep_pribadi)):
                    resep_pribadi_detail(list_resep_pribadi[pilih_resep_pribadi][1])
                    last_pilih = list_resep_pribadi[pilih_resep_pribadi][1]
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
        
        choice = input("Pilihanmu: ").strip()
        
        if choice == "1":
            bookmark_menu(user_index, user_data)
        elif choice == "2":
            profile_resep_pribadi(user_index, user_data)
        elif choice == "3":
            change_name(user_data, user_index)
        elif choice == "4":
            break
        else:
            print("Pilihan tidak ditemukan")

def bookmark_menu(user_index, user_data):
    from .bookmark import profile_bookmark, pilih_bookmark_user, hapus_bookmark
    
    while True:
        print("\n1. Melihat Bookmark")
        print("2. Menghapus Bookmark")
        print("3. Back")
        
        choice = input("Pilihanmu: ").strip()
        
        if choice == "1":
            if profile_bookmark(user_index, user_data) != -1:
                pilih_bookmark_user(user_index, user_data)
        elif choice == "2":
            if profile_bookmark(user_index, user_data) != -1:
                hapus_bookmark(user_index, user_data)
        elif choice == "3":
            break
        else:
            print("Pilihan tidak ditemukan")