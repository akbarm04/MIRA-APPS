#fungsi menampilkan bahan
def tampil_bahan():
    with open("bahan.txt", "r") as file:
        bahan = file.read().splitlines()

    print("\n=== PILIH BAHAN YANG KAMU PUNYA ===")
    for i in range(len(bahan)):
        print(str(i+1) + ". " + bahan[i])

    return bahan

#fungsi memilih bahan
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
    
def cari_resep(bahan_user):
    hasil = []

    file = open("resep.csv", "r")
    data = file.readlines()
    file.close()

    for i in range(1, len(data)):
        baris = data[i].strip().split(",")
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