from utils.file_utils import baca_baris, baca_csv, baca_data, tambah_data, tulis_data

# Fungsi menampilkan bahan
def tampil_bahan():
    bahan = baca_baris("data/bahan.txt")
    print("\n=== PILIH BAHAN YANG KAMU PUNYA ===")
    for i in range(len(bahan)):
        print(str(i+1) + ". " + bahan[i])
    return bahan

# Fungsi memilih bahan
def pilih_bahan(bahan):
    pilihan = input("Masukkan nomor bahan: ")
    pilihan = pilihan.split(",")
    bahan_user = []

    for p in pilihan:
        if p.strip().isdigit():
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
def pilih_resep_dari_hasil(hasil):
    print("\n=== REKOMENDASI RESEP ===")
    for i in range(len(hasil)):
        print(str(i+1) + ". " + hasil[i]["nama"])
    print(f"{len(hasil)+1}. Back" )
    
    pilih = input("Pilih nomor resep: ")
    if pilih.isdigit():
        pilih = int(pilih) - 1
        if pilih == len(hasil):
            return None
        elif pilih >= 0 and pilih < len(hasil):
            return hasil[pilih]
    
    return None

# DETAIL RESEP
def tampil_detail_resep(resep):
    print("\n=== DETAIL RESEP ===")
    print("Nama:", resep["nama"])

    print("\nBahan:")
    for b in resep["bahan"]:
        print("- " + b)

    print("\nLangkah Memasak:")
    for i in range(len(resep["langkah"])):
        print(str(i+1) + ". " + resep["langkah"][i])

# Alur pencarian resep
def alur_cari_resep(index, data):
    from modules import comment, bookmark
    
    bahan = tampil_bahan()
    bahan_user = pilih_bahan(bahan)
    
    hasil = cari_resep(bahan_user)

    if len(hasil) == 0:
        print("Tidak ada resep yang cocok.")
    else:
        while True:
            resep = pilih_resep_dari_hasil(hasil)
            if resep is None:
                break
            
            tampil_detail_resep(resep)
            while True:
                print("\n1. Melihat dan menulis comment")
                print("2. Masukkan ke dalam Bookmark")
                print("3. Back")
                
                pilih = input("Pilih: ").strip()
                if pilih == "1":
                    comment.manage_comments(resep, index, data)
                elif pilih == "2":
                    bookmark.tambah_bookmark(resep, index, data)
                elif pilih == "3":
                    break
                else:
                    print("Pilihan tidak ditemukan")

# Tambah resep pribadi
def tambah_resep_pribadi(index, data):
    print("=== Tambah Resep Pribadi ===")
    resep_pribadi = baca_data("data/resep_user.txt")
    
    while True:
        nama_resep = input("Masukkan nama resep: ").strip()
        sudah_ada = False
        for resep in resep_pribadi:
            if nama_resep == resep[1]:
                sudah_ada = True
                break
        
        if sudah_ada:
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
        "langkah": langkah_resep.split(";")
    }
    
    tampil_detail_resep(resep)
    print("="*50)
    print("1. Simpan resep")
    print("2. Hapus resep")
    konfirmasi = input("Pilihanmu: ").strip()
    
    if konfirmasi == "1":
        resep_baru = f"{data[index][0]}|{nama_resep}|{bahan_resep}|{langkah_resep}"
        tambah_data("data/resep_user.txt", resep_baru)
        print("\nResep berhasil di tambahkan")
    elif konfirmasi == "2":
        print("Resep batal disimpan")
    else:
        print("Pilihan tidak ditemukan")