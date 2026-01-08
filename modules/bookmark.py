from utils.file_utils import baca_data, tambah_data, tulis_data
from .recipe import tampil_detail_resep

# Fungsi mengambil data bookmark
def ambil_bookmark():
    return baca_data("data/bookmark.txt")

# Cek isi bookmark apakah sudah ada
def cek_bookmark_ada(resep, user_index, user_data):
    bookmark = ambil_bookmark()
    
    for bm in bookmark:
        if bm[0] == user_data[user_index][0] and bm[1] == resep["nama"]:
            return True
    return False

# Memasukkan resep ke bookmark
def tambah_bookmark(resep, user_index, user_data):
    sudah_ada = cek_bookmark_ada(resep, user_index, user_data)
    
    if not sudah_ada:
        tambah_data("data/bookmark.txt", f"{user_data[user_index][0]}|{resep['nama']}")
        print("Resep berhasil dimasukkan ke dalam bookmark")
    else:
        print("Resep sudah ada di bookmark")

# Isi bookmark user
def ambil_bookmark_user(user_index, user_data):
    semua_bookmark = ambil_bookmark()
    bookmark_user = []
    
    for bookmark in semua_bookmark:
        if bookmark[0] == user_data[user_index][0]:
            bookmark_user.append(bookmark)
    
    return bookmark_user

# Buka detail resep dari bookmark
def tampil_detail_bookmark(nama_resep):
    resep_data = baca_csv("data/resep.csv")
    
    for resep in resep_data[1:]:
        if resep[1] == nama_resep:
            resep_detail = {
                "nama": resep[1],
                "bahan": resep[2].split(";"),
                "langkah": resep[3].split(";")
            }
            tampil_detail_resep(resep_detail)
            break

# Tampilkan bookmark di profile
def tampil_bookmark_user(user_index, user_data):
    bookmark_user = ambil_bookmark_user(user_index, user_data)
    
    if len(bookmark_user) == 0:
        print("\nBelum ada Bookmark!!")
        return False
    
    print("\nBookmarkmu:")
    for i in range(len(bookmark_user)):
        print(f"{i+1}. {bookmark_user[i][1]}")
    
    return True

# Pilih bookmark user
def pilih_bookmark_user(user_index, user_data):
    bookmark_user = ambil_bookmark_user(user_index, user_data)
    pilihan = input("Pilihanmu: ").strip()
    
    if pilihan.isdigit():
        pilihan = int(pilihan) - 1
        if pilihan >= 0 and pilihan < len(bookmark_user):
            tampil_detail_bookmark(bookmark_user[pilihan][1])
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")

# Hapus bookmark
def hapus_bookmark(user_index, user_data):
    semua_bookmark = ambil_bookmark()
    bookmark_user = ambil_bookmark_user(user_index, user_data)
    
    if len(bookmark_user) == 0:
        print("Belum ada bookmark")
        return
    
    if tampil_bookmark_user(user_index, user_data):
        pilihan = input("Pilihanmu: ").strip()
        
        if pilihan.isdigit():
            pilihan = int(pilihan) - 1
            if pilihan >= 0 and pilihan < len(bookmark_user):
                # Hapus dari list
                for i in range(len(semua_bookmark)):
                    if (user_data[user_index][0] == semua_bookmark[i][0] and 
                        bookmark_user[pilihan][1] == semua_bookmark[i][1]):
                        semua_bookmark.pop(i)
                        break
                
                # Tulis ulang file
                tulis_data("data/bookmark.txt", semua_bookmark)
                print("Resep berhasil dihapus")
            else:
                print("Pilihan tidak ditemukan")
        else:
            print("Pilihan tidak ditemukan")