from utils.file_utils import baca_data, tambah_data, tulis_data, baca_csv

# Fungsi mengambil data bookmark
def data_bookmark():
    return baca_data("data/bookmark.txt")

# Cek isi bookmark apakah sudah ada
def cek_bookmark(resep, index, data):
    list_bookmark = data_bookmark()
    for i in range(len(list_bookmark)):
        if list_bookmark[i][0] == data[index][0] and list_bookmark[i][1] == resep["nama"]:
            return -1

# Memasukkan resep ke bookmark
def bookmark(resep, index, data):
    valid = cek_bookmark(resep, index, data)
    if valid != -1:
        tambah_data("data/bookmark.txt", f"{data[index][0]}|{resep['nama']}")
        print("Resep berhasil dimasukkan ke dalam bookmark")
    else:
        print("Resep sudah ada di bookmark")

# Isi bookmark user
def bookmark_user(index, data):
    list_bookmark = data_bookmark()
    list_bookmark_user = []
    for i in range(len(list_bookmark)):
        if list_bookmark[i][0] == data[index][0]:
            list_bookmark_user.append(list_bookmark[i])
    return list_bookmark_user

# Fungsi detail resep lokal (untuk hindari circular import)
def detail_resep_lokal(resep):
    print("\n=== DETAIL RESEP ===")
    print("Nama:", resep["nama"])
    print("\nBahan:")
    for b in resep["bahan"]:
        print("- " + b)
    print("\nLangkah Memasak:")
    for i in range(len(resep["langkah"])):
        print(str(i+1) + ". " + resep["langkah"][i])

# Buka detail resep dari bookmark
def bookmark_detail(nama):
    data = baca_csv("data/resep.csv")
    for line in data[1:]:
        if line[1] == nama:
            resep = {
                "nama": line[1],
                "bahan": line[2].split(";"),
                "langkah": line[3].split(";")
            }
            detail_resep_lokal(resep)
            break

# Buka bookmark di profile
def profile_bookmark(index, data):
    list_bookmark = bookmark_user(index, data)
    if not list_bookmark:
        print("\nBelum ada Bookmark!!")
        return -1
    else:
        print("\nBookmarkmu:")
        for i in range(len(list_bookmark)):
            print(f"{i+1}. {list_bookmark[i][1]}")
        return list_bookmark

# Pilih bookmark user
def pilih_bookmark_user(index, data):
    list_bookmark = bookmark_user(index, data)
    pilih_bookmark = input("Pilihanmu: ")
    
    if pilih_bookmark.isdigit():
        pilih_bookmark = int(pilih_bookmark)-1
        if pilih_bookmark in range(len(list_bookmark)):
            bookmark_detail(list_bookmark[pilih_bookmark][1])
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")

# Hapus bookmark
def hapus_bookmark(index, data):
    list_data_bookmark = data_bookmark()
    list_bookmark = bookmark_user(index, data)
    
    pilih_bookmark = input("Pilihanmu: ")
    
    if pilih_bookmark.isdigit():
        pilih_bookmark = int(pilih_bookmark)-1
        if pilih_bookmark in range(len(list_bookmark)):
            for i in range(len(list_data_bookmark)):
                if data[index][0] == list_data_bookmark[i][0] and list_bookmark[pilih_bookmark][1] == list_data_bookmark[i][1]:
                    list_data_bookmark.pop(i)
                    tulis_data("data/bookmark.txt", list_data_bookmark)
                    print("Resep berhasil dihapus")
                    break
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")