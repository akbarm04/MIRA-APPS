import hashlib

# =========================
# HASH PASSWORD
# =========================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# =========================
# REGISTER
# =========================
def register():
    print("\n=== REGISTER ===")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")

    file = open("users.txt", "r")
    users = file.readlines()
    file.close()

    for u in users:
        if email == u.split(",")[1]:
            print("Email sudah terdaftar!")
            return

    password_hash = hash_password(password)

    file = open("users.txt", "a")
    file.write(username + "," + email + "," + password_hash + "\n")
    file.close()

    print("Register berhasil!")

# =========================
# LOGIN
# =========================
def login():
    print("\n=== LOGIN ===")
    email = input("Email: ")
    password = input("Password: ")

    password_hash = hash_password(password)

    file = open("users.txt", "r")
    users = file.readlines()
    file.close()

    for u in users:
        data = u.strip().split(",")
        if email == data[1] and password_hash == data[2]:
            print("Login berhasil!")
            return True

    print("Login gagal!")
    return False

# =========================
# TAMPILKAN BAHAN
# =========================
def tampilkan_bahan():
    file = open("bahan.txt", "r")
    bahan = file.read().splitlines()
    file.close()

    print("\n=== PILIH BAHAN YANG KAMU PUNYA ===")
    for i in range(len(bahan)):
        print(str(i+1) + ". " + bahan[i])

    return bahan

# =========================
# PILIH BAHAN
# =========================
def pilih_bahan(bahan):
    pilihan = input("\nMasukkan nomor bahan (pisahkan dengan koma): ")
    pilihan = pilihan.split(",")

    bahan_user = []

    for p in pilihan:
        index = int(p.strip()) - 1
        if index >= 0 and index < len(bahan):
            bahan_user.append(bahan[index])

    return bahan_user

# =========================
# CARI RESEP (PAKAI BAHAN UTAMA)
# =========================
def cari_resep(bahan_user):
    hasil = []

    file = open("resep.csv", "r")
    data = file.readlines()
    file.close()

    for i in range(1, len(data)):
        baris = data[i].strip().split(",")

        nama = baris[0]
        bahan_utama = baris[1]
        bahan = baris[2].split(";")
        langkah = baris[3].split(";")
        waktu = baris[4]
        tingkat = baris[5]

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
            "waktu": waktu,
            "tingkat": tingkat,
            "cocok": cocok
        })

    return hasil

# =========================
# TAMPILKAN DAFTAR RESEP
# =========================
def pilih_resep(hasil):
    print("\n=== REKOMENDASI RESEP ===")
    for i in range(len(hasil)):
        print(str(i+1) + ". " + hasil[i]["nama"])

    pilih = int(input("Pilih nomor resep: ")) - 1
    return hasil[pilih]

# =========================
# DETAIL RESEP
# =========================
def detail_resep(resep):
    print("\n=== DETAIL RESEP ===")
    print("Nama:", resep["nama"])
    print("Waktu Masak:", resep["waktu"], "menit")
    print("Tingkat Kesulitan:", resep["tingkat"])

    print("\nBahan:")
    for b in resep["bahan"]:
        print("- " + b)

    print("\nLangkah Memasak:")
    for i in range(len(resep["langkah"])):
        print(str(i+1) + ". " + resep["langkah"][i])

# =========================
# MENU SETELAH LOGIN
# =========================
def menu_mira():
    while True:
        print("\n=== MENU MIRA ===")
        print("1. Cari Resep")
        print("2. Logout")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            bahan = tampilkan_bahan()
            bahan_user = pilih_bahan(bahan)

            hasil = cari_resep(bahan_user)

            if len(hasil) == 0:
                print("Tidak ada resep yang cocok.")
            else:
                resep = pilih_resep(hasil)
                detail_resep(resep)

        elif pilih == "2":
            break
        else:
            print("Pilihan tidak valid!")

# =========================
# PROGRAM UTAMA
# =========================
while True:
    print("\n=== MIRA CLI ===")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    menu = input("Pilih menu: ")

    if menu == "1":
        if login():
            menu_mira()
    elif menu == "2":
        register()
    elif menu == "3":
        print("Terima kasih sudah menggunakan MIRA!")
        break
    else:
        print("Pilihan tidak valid!")
