# modules/recipe.py

from utils.file_utils import baca_baris, baca_csv

# Fungsi menampilkan bahan
def tampil_bahan():
    bahan = baca_baris("data/bahan.txt")
    print("\n=== PILIH BAHAN YANG KAMU PUNYA ===")
    for i in range(len(bahan)):
        print(str(i+1) + ". " + bahan[i])
    return bahan

# Fungsi memilih bahan
def pilih_bahan(bahan):
    pilihan = input(f"Masukkan nomor bahan: ")
    pilihan = pilihan.split(",")
    bahan_user = []

    valid_pilih = "1234567890"
    for p in pilihan:
        valid = True
        if p not in valid_pilih:
            valid = False
        if valid:
            index = int(p.strip()) - 1 
            if index >= 0 and index < len(bahan):
                bahan_user.append(bahan[index])

    return bahan_user

# Fungsi cari resep
def cari_resep(bahan_user):
    hasil = []
    data = baca_csv("data/resep.csv")

    for i in range(1, len(data)):
        baris = data[i]
        bahan_utama = baris[0]
        nama = baris[1]
        bahan = baris[2].split(";")
        langkah = baris[3].split(";")

        if bahan_utama not in bahan_user:
            continue

        cocok = 0
        for b in bahan_user:
            if b in bahan:
                cocok += 1

        hasil.append({
            "nama": nama,
            "bahan": bahan,
            "langkah": langkah,
            "cocok": cocok
        })

    return hasil

# TAMPILKAN DAFTAR RESEP
def pilih_resep(hasil):
    print("\n=== REKOMENDASI RESEP ===")
    for i in range(len(hasil)):
        print(str(i+1) + ". " + hasil[i]["nama"])
    print(f"{len(hasil)+1}. Back" )
    
    pilih = input("Pilih nomor resep: ")
    valid_pilih = "1234567890"
    
    for p in pilih:
        valid = True
        if p not in valid_pilih:
            valid = False
    
    if valid:
        pilih = int(pilih) - 1
        if pilih == len(hasil):
            return -1
        else:
            return hasil[pilih]
    else:
        return -2

# DETAIL RESEP
def detail_resep(resep):
    print("\n=== DETAIL RESEP ===")
    print("Nama:", resep["nama"])
    print("\nBahan:")
    for b in resep["bahan"]:
        print("- " + b)
    print("\nLangkah Memasak:")
    for i in range(len(resep["langkah"])):
        print(str(i+1) + ". " + resep["langkah"][i])

# Alur cari resep (untuk compatibility dengan user.py)
def alur_cari_resep(index, data):
    """Alur lengkap pencarian resep"""
    # Import di dalam fungsi untuk hindari circular import
    from modules import comment, bookmark
    
    bahan = tampil_bahan()
    bahan_user = pilih_bahan(bahan)
    
    hasil = cari_resep(bahan_user)

    if len(hasil) == 0:
        print("Tidak ada resep yang cocok.")
    else:
        while True:
            resep = pilih_resep(hasil)
            if resep == -1:
                break
            elif resep == -2:
                print("Pilihan tidak ditemukan")
            else:
                detail_resep(resep)
                while True:
                    print("\n1. Melihat dan menulis comment")
                    print("2. Masukkan ke dalam Bookmark")
                    print("3. Back")
                    
                    pilih = input("Pilih: ").strip()
                    if pilih == "1":
                        comment.comment(resep, index, data)
                    elif pilih == "2":
                        bookmark.bookmark(resep, index, data)
                    elif pilih == "3":
                        break
                    else:
                        print("Pilihan tidak ditemukan")