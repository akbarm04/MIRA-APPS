def cari_index_email(list, cari):
    for i in range(len(list)):
        if list[i][1] == cari:
            return i
    return -1

def cek_at(email):
    if "@" in email:
        return True
    else:
        return False
    
#fungsi ambil data user dari file
def ambildata():
    with open("data_user.txt", "r") as file:
        lines = file.readlines()
    data_user = []
    for line in lines:
        data_user.append(line.strip( ).split( ))
    return data_user

#fungsi login
def login():
    data_user = ambildata()
    while True:
        print("\n=== Lakukan Login ===")
        email = input("Masukkan Email: ")
        password = input("Masukkan Password: ")
        index_email = cari_index_email(data_user, email)
            
        if index_email != -1:
            if email == data_user[index_email][1] and password == data_user [index_email][2]:
                print("Selamat anda berhasil Login")
                return True, index_email, data_user
            else:
                print("Password salah")
        else:
            print("Email tidak ditemukan\n")
            return False, -1, data_user
        
#fungsi signup        
def signup():
    data_user = ambildata()
    while True:
        print("\n=== Lakukan Sign Up ===")
        new_email = input("Masukkan Email: ")
        cek = cek_at(new_email)
        confirm = cari_index_email(data_user, new_email)

        if confirm == -1 and cek:
            break
        if not cek:
            print("Format email salah, silahkan masukkan email yang benar")
        else:
            print("Email sudah ada, silahkan gunakan email lain. ")

    new_username = input("Masukkan Username: ")
    new_password = input("Masukkan Password: ")

    new_data_user = f"{new_username} {new_email} {new_password}"
    with open ("data_user.txt", "a") as file:
        file.write(f"{new_data_user}\n")
    print("\nSign Up berhasil")

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

    for p in pilihan: 
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

    pilih = int(input("Pilih nomor resep: ")) - 1
    return hasil[pilih]

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

#menu setelah login
def menu_mira(username):
    while True:
        print(f"\n=== Halo {username}, Selamat datang di Mira Apps ===\nMy Intelligence Recipe Assistant\n\nApa yang ingin kamu lakukan sekarang? ===")
        print("1. Mencari resep\n2. Menulis resep\n3. Keluar")
        pilih_menu = input("Pilihanmu: ")

        if pilih_menu == "1":
            bahan = tampil_bahan()
            bahan_user = pilih_bahan(bahan)
            
            hasil = cari_resep(bahan_user)

            if len(hasil) == 0:
                print("Tidak ada resep yang cocok.")
            else:
                resep = pilih_resep(hasil)
                detail_resep(resep)
                
        elif pilih_menu == "2":
            print("Fitur menulis resep masih dalam pengembangan!")
            continue
        elif pilih_menu == "3":
            print("Terimakasih telah menggunakan Mira Apps\n")
            return
        else:
            print("Pilihan tidak ditemukan")

#program utama
while True:
    print("=== Selamat Datang di Mira Apps ===")
    print("1. Login\n2. Sign Up\n3. Keluar")
    pilih = input("Pilihanmu: ")

    if (pilih == "1"):
        berhasil, index, data = login()
        if berhasil:
            menu_mira(data[index][0])
    elif(pilih == "2"):
        signup()
    elif (pilih == "3"):
        print("Selamat Tinggal")
        break
    else:
        print("Pilihan tidak ditemukan")