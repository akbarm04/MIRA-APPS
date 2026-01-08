from utils.file_utils import baca_data, tulis_data
from . import bookmark
from .recipe import tampil_detail_resep

#ganti Profile Name
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
            #mengganti nama di data_user.txt
            data[index][3] = change_name
            with open("data_user.txt", "w") as file:
                for i in data:
                    file.write(i[0] + "|" + i[1] + "|" + i[2] + "|" + i[3] + "\n")

            #mengganti nama di comment,txt
            list_comment = data_comment()
            for j in range(len(list_comment)):
                if list_comment[j][2] == data[index][0]:
                    list_comment[j][1] = change_name
            with open("comment.txt", "w") as file_comment:
                for k in list_comment:
                    file_comment.write(k[0] + "|" + k[1] + "|" + k[2] + "|" + k[3] +"\n")
            print(f"Profile Name berhasil diganti")
            break

#data resep pribadi
def data_resep_pribadi():
    with open("resep_user.txt", "r") as file:
            lines = file.readlines()
    data_resep_pribadi = []
    for line in lines:
        data_resep_pribadi.append(line.strip().split("|"))
    return data_resep_pribadi

#data resep pribadi user
def resep_pribadi_user(index, data):
    list_resep_pribadi = data_resep_pribadi()
    list_resep_user = []
    for i in range(len(list_resep_pribadi)):
        if list_resep_pribadi[i][0] == data[index][0]:
            list_resep_user.append(list_resep_pribadi[i])
    return list_resep_user

#detai resep pribadi user
def resep_pribadi_detail (nama):
    with open("resep_user.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        hasil = line.strip().split("|")
        if hasil[1] == nama:
            resep = {
                "nama": hasil[1],
                "bahan": hasil[2].split(";"),
                "langkah": hasil[3].split(";")
            }
            detail_resep(resep)
            break

#menambah resep pribadi
def tambah_resep_pribadi(index, data):
    print("=== Tambah Resep Pribadi ===")
    list_resep_pribadi = data_resep_pribadi()
    
    while True:
        nama_resep = input("Masukkan nama resep: ").strip()
        for i in range(len(list_resep_pribadi)):
            if nama_resep == list_resep_pribadi[i][1]:
                print("Resep sudah ada")
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
    resep = {
            "nama": nama_resep,
            "bahan": bahan_resep.split(";"),
            "langkah": langkah_resep.split(";")}
    detail_resep(resep)

    confirm = input("="*50 + "\n1. Simpan resep\n2. Hapus resep\nPilihanmu: ").strip()
    if confirm == "1":
        new_resep = f"{data[index][0]}|{nama_resep}|{bahan_resep}|{langkah_resep}"

        with open ("resep_user.txt", "a") as file:
            file.write(f"{new_resep}\n")
            print("\nResep berhasil di tambahkan")
    elif confirm == "2":
        print("Resep batal disimpan")
    else:
        print("Pilihan tidak ditemukan")

#hapus resep pribadi
def hapus_resep_pribadi (index, data, nama):
    list_data_resep_pribadi = data_resep_pribadi()
    for i in range(len(list_data_resep_pribadi)):
        if data[index][0] == list_data_resep_pribadi[i][0] and nama == list_data_resep_pribadi[i][1]:
            list_data_resep_pribadi.pop(i)
            with open("resep_user.txt", "w") as file:
                for item in list_data_resep_pribadi:
                    file.write(item[0] + "|" + item[1]+ "|" + item[2]+ "|" + item[3]+"\n")
            print("Resep pribadi berhasil dihapus!")
            break

#resep pribadi di profile
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
            valid_pilih = "1234567890"
            valid = True
            for i in pilih_resep_pribadi:
                if i not in valid_pilih:
                    valid = False
            if valid:
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
        
        pilihan = input("Pilihanmu: ").strip()
        
        if pilihan == "1":
            menu_bookmark(user_index, user_data)
        elif pilihan == "2":
            kelola_resep_pribadi(user_index, user_data)
        elif pilihan == "3":
            ganti_nama_profile(user_data, user_index)
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak ditemukan")

def menu_bookmark(user_index, user_data):
    while True:
        print("\n1. Melihat Bookmark")
        print("2. Menghapus Bookmark")
        print("3. Back")
        
        pilihan = input("Pilihanmu: ").strip()
        
        if pilihan == "1":
            if bookmark.tampil_bookmark_user(user_index, user_data):
                bookmark.pilih_bookmark_user(user_index, user_data)
        elif pilihan == "2":
            bookmark.hapus_bookmark(user_index, user_data)
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak ditemukan")