from utils.file_utils import baca_data, tambah_data, tulis_data, baca_csv

#fungsi mengambil data bookmark
def data_bookmark():
    with open("bookmark.txt", "r") as file:
            lines = file.readlines()
    data_bookmark = []
    for line in lines:
        data_bookmark.append(line.strip().split("|"))
    return data_bookmark

#cek isi bookmark apakah sudah ada
def cek_bookmark(resep, index, data):
    list_bookmark = data_bookmark()
    for i in range(len(list_bookmark)):
        if list_bookmark[i][0] == data[index][0] and list_bookmark[i][1] == resep["nama"]:
            return -1
        
#memasukkan resep ke bookmark
def bookmark(resep, index, data):
    valid = cek_bookmark(resep, index, data)
    if valid != -1:
        with open("bookmark.txt", "a") as file:
            file.write(f"{data[index][0]}|{resep['nama']}\n")
        print("Resep berhasil dimasukkan ke dalam bookmark")
    else:
        print("Resep sudah ada di bookmark")

#isi bookmark user
def bookmark_user(index, data):
    list_bookmark = data_bookmark()
    list_bookmark_user = []
    data[index][0]
    for i in range(len(list_bookmark)):
        if list_bookmark[i][0] == data[index][0]:
            list_bookmark_user.append(list_bookmark[i])
    return list_bookmark_user

#buka detail resep dari bookmark
def bookmark_detail (nama):
    with open("resep.csv", "r") as file:
        lines = file.readlines()

    for line in lines[1:]:
        hasil = line.strip().split(",")
        if hasil[1] == nama:
            resep = {
                "nama": hasil[1],
                "bahan": hasil[2].split(";"),
                "langkah": hasil[3].split(";")
            }
            detail_resep(resep)
            break
#buka bookmark di profile
def profile_bookmark(index, data):
    list_bookmark = bookmark_user(index, data)
    if not list_bookmark:
        print("\nBelum ada Bookmark!!")
        return -1
    else:
        print("\nBookmarkmu:")
        for i in range(len(list_bookmark)):
            print(f"{i+1}. {list_bookmark[i][1]}")

def pilih_bookmark_user(index, data):
    list_bookmark = bookmark_user(index, data)
    pilih_bookmark = input("Pilihanmu: ")
    valid_pilih = "1234567890"
    valid = True
    for i in pilih_bookmark:
        if i not in valid_pilih:
            valid = False
    if valid:
        pilih_bookmark = int(pilih_bookmark)-1
        if pilih_bookmark in range(len(list_bookmark)):
            bookmark_detail(list_bookmark[pilih_bookmark][1])
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")

#Menghapus bookmark
def hapus_bookmark (index, data):
    list_data_bookmark = data_bookmark()
    list_bookmark = bookmark_user(index, data)
    pilih_bookmark = input("Pilihanmu: ")
    valid_pilih = "1234567890"
    valid = True
    for i in pilih_bookmark:
        if i not in valid_pilih:
            valid = False
    if valid:
        pilih_bookmark = int(pilih_bookmark)-1
        if pilih_bookmark in range(len(list_bookmark)):
            for i in range(len(list_data_bookmark)):
                if data[index][0] == list_data_bookmark[i][0] and list_bookmark[pilih_bookmark][1] == list_data_bookmark[i][1]:
                    list_data_bookmark.pop(i)
                    with open("bookmark.txt", "w") as file:
                        for item in list_data_bookmark:
                            file.write(item[0] + "|" + item[1]+"\n")
                    print("Resep berhasil dihapus")
                    break
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")