from utils.file_utils import baca_baris, baca_csv, tulis_csv, tambah_data
from .recipe import tampil_detail_resep

# List resep.csv
def ambil_daftar_resep():
    return baca_csv("data/resep.csv")

# Tambah resep admin
def tambah_resep_admin():
    print("=== Tambah Resep ===")
    bahan = baca_baris("data/bahan.txt")
    
    # Bahan dasar
    while True:
        print("Pilih Bahan Dasar")
        for i in range(len(bahan)):
            print(str(i+1) + ". " + bahan[i])
        
        pilihan = input("Pilihanmu: ").strip()
        
        if pilihan.isdigit():
            pilihan = int(pilihan) - 1
            if pilihan >= 0 and pilihan < len(bahan):
                bahan_dasar = bahan[pilihan]
                break
        print("Pilihan tidak ditemukan")
    
    # Nama resep
    resep_list = ambil_daftar_resep()
    resep_list = resep_list[1:]  # Skip header
    
    while True:
        nama_resep = input("Masukkan nama resep: ").strip()
        nama_sama = False
        
        for resep in resep_list:
            if nama_resep == resep[1]:
                print("Resep sudah ada. Silakan masukkan nama resep kembali")
                nama_sama = True
                break
        
        if not nama_sama:
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
    
    resep_data = {
        "nama": nama_resep,
        "bahan": bahan_resep.split(";"),
        "langkah": langkah_resep.split(";")
    }
    
    tampil_detail_resep(resep_data)
    print("="*50)
    print("1. Simpan resep")
    print("2. Hapus resep")
    konfirmasi = input("Pilihanmu: ").strip()
    
    if konfirmasi == "1":
        resep_baru = f"{bahan_dasar},{nama_resep},{bahan_resep},{langkah_resep}"
        tambah_data("data/resep.csv", resep_baru)
        print("\nResep berhasil di tambahkan")
    elif konfirmasi == "2":
        print("Resep batal disimpan")
    else:
        print("Pilihan tidak ditemukan")

# Hapus resep admin
def hapus_resep_admin():
    resep_list = ambil_daftar_resep()
    resep_list = resep_list[1:]  # Skip header
    
    if len(resep_list) == 0:
        print("Tidak ada resep untuk dihapus")
        return
    
    print("Pilih resep yang ingin dihapus: ")
    for i in range(len(resep_list)):
        print(f"{i+1}. {resep_list[i][1]}")
    
    pilihan = input("Pilihanmu: ").strip()
    
    if pilihan.isdigit():
        pilihan = int(pilihan) - 1
        if pilihan >= 0 and pilihan < len(resep_list):
            resep_list.pop(pilihan)
            
            # Write back with header
            header = ["bahan_dasar", "nama_resep", "bahan_tambahan", "langkah-langkah"]
            tulis_csv("data/resep.csv", resep_list, header)
            print("Resep berhasil dihapus!")
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")

# Mengubah resep admin
def ubah_resep_admin():
    resep_list = ambil_daftar_resep()
    resep_list = resep_list[1:]  # Skip header
    
    if len(resep_list) == 0:
        print("Tidak ada resep untuk diubah")
        return
    
    print("Pilih resep yang ingin diubah: ")
    for i in range(len(resep_list)):
        print(f"{i+1}. {resep_list[i][1]}")
    
    pilihan = input("Pilihanmu: ").strip()
    
    if pilihan.isdigit():
        pilihan = int(pilihan) - 1
        if pilihan >= 0 and pilihan < len(resep_list):
            while True:
                resep_data = {
                    "nama": resep_list[pilihan][1],
                    "bahan": resep_list[pilihan][2].split(";"),
                    "langkah": resep_list[pilihan][3].split(";")
                }
                
                tampil_detail_resep(resep_data)
                print("\nYang ingin diubah:")
                print("1. Nama resep")
                print("2. Bahan-bahan")
                print("3. Langkah-langkah")
                print("4. Selesai")
                
                pilihan_ubah = input("Pilihanmu: ").strip()
                
                if pilihan_ubah == "1":
                    while True:
                        nama_baru = input("Masukkan nama resep: ").strip()
                        nama_sama = False
                        
                        for i, resep in enumerate(resep_list):
                            if i != pilihan and nama_baru == resep[1]:
                                print("Nama resep sama. Silakan masukkan nama resep kembali")
                                nama_sama = True
                                break
                        
                        if not nama_sama:
                            if nama_baru == "":
                                print("Nama resep tidak boleh kosong. Silakan masukkan nama resep kembali")
                            else:
                                resep_list[pilihan][1] = nama_baru
                                break
                elif pilihan_ubah == "2":
                    while True:
                        bahan_baru = input("Masukkan bahan-bahan (pisahkan dengan titik koma ';'): ").strip()
                        if bahan_baru == "":
                            print("Bahan-bahan tidak boleh kosong. Silakan masukkan bahan kembali")
                        else:
                            resep_list[pilihan][2] = bahan_baru
                            break
                elif pilihan_ubah == "3":
                    while True:
                        langkah_baru = input("Masukkan langkah-langkah (pisahkan dengan titik koma ';'): ").strip()
                        if langkah_baru == "":
                            print("Langkah-langkah tidak boleh kosong. Silakan masukkan langkah kembali")
                        else:
                            resep