# modules/admin.py

from utils.file_utils import baca_baris, baca_csv, tulis_csv, tambah_data
from .recipe import detail_resep

border = "─" * 45
border2 = "=" * 45
spasi = 45

# List resep.csv
def list_resep():
    return baca_csv("data/resep.csv")

# Tambah resep admin
def tambah_resep_admin():
    print(f"\n\n\n{border2}")
    print("Tambah Resep".center(spasi))
    print(border2)
    list_bahan = baca_baris("data/bahan.txt")

    # Bahan dasar
    while True:
        print("Pilih Bahan Dasar")
        for i in range(len(list_bahan)):
            print(str(i+1) + ". " + list_bahan[i])
        
        pilih_bahan = input("Pilihanmu: ").strip()
        
        if pilih_bahan.isdigit():
            pilih_bahan = int(pilih_bahan)-1
            if pilih_bahan in range(len(list_bahan)):
                bahan = list_bahan[pilih_bahan]
                break
            else:
                print("Pilihan tidak ditemukan")
        else:
            print("Pilihan tidak ditemukan")

    # Nama resep
    list_reseps = list_resep()[1:]  
    
    while True:
        nama_resep = input("Masukkan nama resep: ").strip()
        nama_ada = False
        
        for i in range(len(list_reseps)):
            if nama_resep == list_reseps[i][1]:
                print("Resep sudah ada. Silakan masukkan nama resep kembali")
                nama_ada = True
                break
        
        if not nama_ada:
            if nama_resep == "":
                print("Nama resep tidak boleh kosong. Silakan masukkan nama resep kembali")
            else:
                break

    # Bahan-bahan 
    while True:
        bahan_resep = input("Masukkan bahan-bahan (pisahkan dengan titik koma ';'): ").strip()
        if bahan_resep == "":
            print("Bahan-bahan tidak boleh kosong. Silakan masukkan bahan kembali")
        else:
            break
    
    # Langkah-langkah
    while True:
        langkah_resep = input("Masukkan langkah-langkah (pisahkan dengan titik koma ';'): ").strip()
        if langkah_resep == "":
            print("Langkah-langkah tidak boleh kosong. Silakan masukkan langkah kembali")
        else:
            break

    resep = {
        "nama": nama_resep,
        "bahan": bahan_resep.split(";"),
        "langkah": langkah_resep.split(";")
    }
    
    detail_resep(resep)
    
    confirm = input("="*50 + "\n1. Simpan resep\n2. Hapus resep\nPilihanmu: ").strip()
    
    if confirm == "1":
        new_resep = f"{bahan},{nama_resep},{bahan_resep},{langkah_resep}"
        tambah_data("data/resep.csv", new_resep)
        print("\nResep berhasil di tambahkan")
    elif confirm == "2":
        print("Resep batal disimpan")
    else:
        print("Pilihan tidak ditemukan")

# Hapus resep admin
def hapus_resep_admin():
    list_reseps = list_resep()[1:] 
    
    if len(list_reseps) == 0:
        print("Tidak ada resep untuk dihapus")
        return
    
    print("Pilih resep yang ingin dihapus: ")
    for i in range(len(list_reseps)):
        print(f"{i+1}. {list_reseps[i][1]}")
    
    pilih_reseps = input("Pilihanmu: ").strip()
    
    if pilih_reseps.isdigit():
        pilih_reseps = int(pilih_reseps)-1
        if pilih_reseps in range(len(list_reseps)):
            list_reseps.pop(pilih_reseps)
            
            header = ["bahan_dasar", "nama_resep", "bahan_tambahan", "langkah-langkah"]
            tulis_csv("data/resep.csv", list_reseps, header)
            print("Resep berhasil dihapus!")
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")

# Mengubah resep admin
def ubah_resep_admin():
    list_reseps = list_resep()[1:]  
    
    if len(list_reseps) == 0:
        print("Tidak ada resep untuk diubah")
        return
    
    print("Pilih resep yang ingin diubah: ")
    for i in range(len(list_reseps)):
        print(f"{i+1}. {list_reseps[i][1]}")
    
    pilih_reseps = input("Pilihanmu: ").strip()
    
    if pilih_reseps.isdigit():
        pilih_reseps = int(pilih_reseps)-1
        if pilih_reseps in range(len(list_reseps)):
            while True:
                resep = {
                    "nama": list_reseps[pilih_reseps][1],
                    "bahan": list_reseps[pilih_reseps][2].split(";"),
                    "langkah": list_reseps[pilih_reseps][3].split(";")
                }
                
                detail_resep(resep)
                
                print("\nYang ingin diubah:")
                print("1. Nama resep")
                print("2. Bahan-bahan")
                print("3. Langkah-langkah")
                print("4. Selesai")
                
                pilih_ubah = input("Pilihanmu: ").strip()
                
                if pilih_ubah == "1":
                    while True:
                        nama_resep = input("Masukkan nama resep: ").strip()
                        sama = False
                        
                        for i, resep_item in enumerate(list_reseps):
                            if i != pilih_reseps and nama_resep == resep_item[1]:
                                print("Nama resep sama. Silakan masukkan nama resep kembali")
                                sama = True
                                break
                        
                        if not sama:
                            if nama_resep == "":
                                print("Nama resep tidak boleh kosong. Silakan masukkan nama resep kembali")
                            else:
                                list_reseps[pilih_reseps][1] = nama_resep
                                break
                                
                elif pilih_ubah == "2":
                    while True:
                        bahan_resep = input("Masukkan bahan-bahan (pisahkan dengan titik koma ';'): ").strip()
                        if bahan_resep == "":
                            print("Bahan-bahan tidak boleh kosong. Silakan masukkan bahan kembali")
                        else:
                            list_reseps[pilih_reseps][2] = bahan_resep
                            break
                            
                elif pilih_ubah == "3":
                    while True:
                        langkah_resep = input("Masukkan langkah-langkah (pisahkan dengan titik koma ';'): ").strip()
                        if langkah_resep == "":
                            print("Langkah-langkah tidak boleh kosong. Silakan masukkan langkah kembali")
                        else:
                            list_reseps[pilih_reseps][3] = langkah_resep
                            break
                            
                elif pilih_ubah == "4":
                    break
                else:
                    print("Pilihan tidak ditemukan")
            
            # Tampilkan hasil
            resep = {
                "nama": list_reseps[pilih_reseps][1],
                "bahan": list_reseps[pilih_reseps][2].split(";"),
                "langkah": list_reseps[pilih_reseps][3].split(";")
            }
            
            detail_resep(resep)
            
            # Simpan perubahan
            header = ["bahan_dasar", "nama_resep", "bahan_tambahan", "langkah-langkah"]
            tulis_csv("data/resep.csv", list_reseps, header)
            print("Resep berhasil diubah!")
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")

# Menu admin
def menu_admin(index, data):
    while True:
        print(f"\n\n\n{border}")
        print(f"Halo Admin {data[index][3]}, Selamat datang di Mira Apps".center(spasi))
        print(border)
        print("My Intelligence Recipe Assistant\n\nApa yang ingin kamu lakukan sekarang?")
        print("1. Menambah resep\n2. Menghapus resep\n3. Mengubah resep\n4. Log Out")
        
        pilih_menu_admin = input("Pilihanmu: ").strip()
        
        if pilih_menu_admin == "1":
            tambah_resep_admin()
        elif pilih_menu_admin == "2":
            hapus_resep_admin()
        elif pilih_menu_admin == "3":
            ubah_resep_admin()
        elif pilih_menu_admin == "4":
            print("Terimakasih telah menggunakan Mira Apps\n")
            break
        else:
            print("Pilihan tidak ditemukan")
