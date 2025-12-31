#fungsi mencari index email
def cari_index_email(list, cari):
    for i in range(len(list)):
        if list[i][1] == cari:
            return i
    return -1

#fungsi mencari index username
def cari_index_username(list, cari):
    for i in range(len(list)):
        if list[i][0] == cari:
            return i
    return -1

#fungsi untuk mengecek email sesuai format  
def valid_email(email):
    valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._"

    #cek apakah email hanya @. atau .@ saja
    if email == "@." or email == ".@":
        return False
    
    #cek apakah ada @
    if "@" and "." not in email:
        return False
    
    #cek apakah email sesuai
    for char in email:
        if char not in valid:
            return False
    return True

#fungsi cek username apakah valid
def valid_username (username):
    valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._"
    for char in username:
        if char not in valid:
            return False
    return True
        
#fungsi ambil data user dari file
def ambildata():
    with open("data_user.txt", "r") as file:
        lines = file.readlines()
    data_user = []
    for line in lines:
        data_user.append(line.strip().split("|"))
    return data_user



#fungsi login
def login():
    data_user = ambildata()
    while True:
        print("\n=== Lakukan Login ===")
        key_user = input("Masukkan Email atau Username: ")
        #cek apakah email atau username
        if "@" in key_user:
            key_user = key_user
            index_user = cari_index_email(data_user, key_user)
        else:
            key_user = key_user.lower()
            index_user = cari_index_username(data_user, key_user)

        password = input("Masukkan Password: ")
        if index_user != -1:
            if (key_user == data_user[index_user][1] and password == data_user [index_user][2]) or (key_user == data_user[index_user][0] and password == data_user [index_user][2]):
                print("Selamat anda berhasil Login")
                return True, index_user, data_user
            else:
                print("\nPassword salah!")
                return False, -1, data_user
        else:
            print("\nEmail atau Username tidak ditemukan!")
            return False, -1, data_user
        
#fungsi register       
def register():
    data_user = ambildata()
    #Memasukkan email baru
    while True:
        print("\n=== Lakukan Register ===")
        new_email = input("Masukkan Email: ").strip()
        cek_email = valid_email(new_email)
        confirm_email = cari_index_email(data_user, new_email)
        if confirm_email == -1 and cek_email:
            break
        elif new_email == "":
            print("\nEmail tidak boleh kosong, silahkan isi")
        elif not cek_email:
            print("\nFormat email salah, silahkan masukkan email yang benar")
        else:
            print("\nEmail sudah ada, silahkan gunakan email lain.")

    #memasukkan username baru
    while True:
        new_username = input("Masukkan Username: ").lower().strip()
        cek_username = valid_username(new_username)
        confirm_username =  cari_index_username(data_user, new_username)
        if confirm_username == -1 and cek_username:
            break
        elif new_username == "":
            print("\nUsername tidak boleh kosong, silahkan isi")
        elif not cek_username:
            print('\nUsername hanya bisa diisi huruf, angka, titik "." dan underscore "_"')
        elif new_username == "." or new_username == "_" or new_username == "._" or new_username == "_.":
            print("Format username salah")
        else:
            print("\nUsername sudah terpakai, silahkan gunakan yang lain")

    #memasukkan password baru
    while True:
        new_password = input("Masukkan Password: ")
        if new_password == "":
            print("\nPassword tidak boleh kosong, silahkan isi")
        else: 
            break
    #memasukkan profile name
    while True:
        new_profile_name = input("Masukkan Profile Name: ").strip()
        if new_profile_name == "":
            print("\nProfile Name tidak boleh kosong, silahkan isi")
        elif "|" in new_profile_name:
            print('Nama tidak boleh mengandung "|"')
        else: 
            break
    new_data_user = f"{new_username}|{new_email}|{new_password}|{new_profile_name}"
    with open ("data_user.txt", "a") as file:
        file.write(f"{new_data_user}\n")
    print("\nRegister berhasil")

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
    print(f"{len(hasil)+1}. Back" )
    pilih = int(input("Pilih nomor resep: ")) - 1
    print(len(hasil))
    if pilih == len(hasil):
        return -1
    else:
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

#Fungsi filter comment
def filter_comment(comment):
    text = comment
    comment_lower = text.lower()
    comment_pisah = comment_lower.split()
    with open("id_badwords.txt", "r") as file:
        lines = file.readlines()
    kata_terlarang = []
    for line in lines:
        kata_terlarang.append(line.strip())

    for i in range(len(comment_pisah)):
        if comment_pisah[i] in kata_terlarang:
            return -1
        
    if "|" in text:
        return -2
    else:
        return text

#fungsi ambil data comment
def data_comment():
    with open("comment.txt", "r") as file:
        lines = file.readlines()
    data_comment = []
    for line in lines:
        data_comment.append(line.strip().split("|"))
    return data_comment

#fungsi list comment sesuai pilihan 
def lihat_comment(data, resep):
    list_comment = []
    for item in data:
        if item[0] == resep:
            list_comment.append(item)
    return list_comment

#melihat dan menulis comment
def comment(resep, index, data):
    while True:
        resep = resep
        list_comment = data_comment()
        lihat_comment_resep = lihat_comment(list_comment, resep["nama"])
        #menampilkan comment yang sudah ada
        if len(lihat_comment_resep) > 0:
            for i in range(len(lihat_comment_resep)):
                print("\n" + "=" * 50 + f"\nPengirim: {lihat_comment_resep[i][1]}\nUsername: @{lihat_comment_resep[i][2]}\nComment:\n{lihat_comment_resep[i][3]}\n"+ "=" * 50)
        else:
            print("\n" + "=" * 50 + "\nBelum ada comment di resep ini\n"+ "=" * 50 +"\n")
        print("1. Menulis comment\n2. Back")
        pilih_tulis = input("Pilihanmu: ")
        if pilih_tulis == "1":
            comment = input("Silahkan tulis komentarmu:\n").strip()
            comment = filter_comment(comment)
            if comment == "":
                print("Komentar tidak boleh kosong")
            elif comment == -1:
                print("Dilarang menggunakan kata yang tidak pantas!")
                break
            elif comment == -2:
                print('Maaf tidak bisa menggunakan simbol "|"')
                break
            else:
                new_comment = f"{resep["nama"]}|{data[index][3]}|{data[index][0]}|{comment}"
                with open ("comment.txt", "a") as file:
                    file.write(f"{new_comment}\n")
                print("\nComment berhasil di tambahkan")
                lihat_comment_resep = lihat_comment(list_comment, resep["nama"])
                for i in range(len(lihat_comment_resep)):
                    print("\n" + "=" * 50 + f"\nPengirim: {lihat_comment_resep[i][1]}\nUsername: @{lihat_comment_resep[i][2]}\nComment:\n{lihat_comment_resep[i][3]}\n"+ "=" * 50)
                    break
        elif pilih_tulis == "2":
            break
        else:
            print("Pilihan tidak ditemukan\n")

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
            file.write(f"{data[index][0]}|{resep["nama"]}\n")
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

#menabah resep pribadi
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
            print("Langkah tidak boleh kosong")
        else:
            break

    new_resep = f"{data[index][0]}|{nama_resep}|{bahan_resep}|{langkah_resep}"
    with open ("resep_user.txt", "a") as file:
        file.write(f"{new_resep}\n")
        print("\nResep berhasil di tambahkan")

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
#resep pribadi di profile
def profile_resep_pribadi(index, data):
    list_resep_pribadi = resep_pribadi_user(index, data)
    if not list_resep_pribadi:
        print("\nBelum ada Resep Pribadi!!")
        return -1
    else:
        print("\nResep Pribadimu:")
        for i in range(len(list_resep_pribadi)):
            print(f"{i+1}. {list_resep_pribadi[i][1]}")

def pilih_resep_pribadi(index, data):
    list_resep_pribadi = resep_pribadi_user(index, data)
    pilih_resep_pribadi = input("Pilihanmu: ")
    valid_pilih = "1234567890"
    valid = True
    for i in pilih_resep_pribadi:
        if i not in valid_pilih:
            valid = False
    if valid:
        pilih_resep_pribadi = int(pilih_resep_pribadi)-1
        if pilih_resep_pribadi in range(len(list_resep_pribadi)):
            resep_pribadi_detail(list_resep_pribadi[pilih_resep_pribadi][1])
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")

def hapus_resep_prbadi (index, data):
    list_data_resep_pribadi = data_resep_pribadi()
    list_resep_pribadi = resep_pribadi_user(index, data)
    pilih_bookmark = input("Pilihanmu: ")
    valid_pilih = "1234567890"
    valid = True
    for i in pilih_bookmark:
        if i not in valid_pilih:
            valid = False
    if valid:
        pilih_bookmark = int(pilih_bookmark)-1
        if pilih_bookmark in range(len(list_resep_pribadi)):
            for i in range(len(list_data_resep_pribadi)):
                if data[index][0] == list_data_resep_pribadi[i][0] and list_resep_pribadi[pilih_bookmark][1] == list_data_resep_pribadi[i][1]:
                    list_data_resep_pribadi.pop(i)
                    with open("resep_user.txt", "w") as file:
                        for item in list_data_resep_pribadi:
                            file.write(item[0] + "|" + item[1]+ "|" + item[2]+ "|" + item[3]+"\n")
                    print("Resep pribadi berhasil dihapus!")
                    break
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")

#ambil data Admin
def ambil_data_admin():
    with open("data_admin.txt", "r") as file:
        lines = file.readlines()
    data_user = []
    for line in lines:
        data_user.append(line.strip().split("|"))
    return data_user

#login untuk admin
def login_admin():
    data_admin = ambil_data_admin()
    while True:
        print("\n=== Lakukan Login ===")
        key_user = input("Masukkan Email atau Username: ")
        #cek apakah email atau username
        if "@" in key_user:
            key_user = key_user
            index_user = cari_index_email(data_admin, key_user)
        else:
            key_user = key_user.lower()
            index_user = cari_index_username(data_admin, key_user)

        password = input("Masukkan Password: ")
        if index_user != -1:
            if key_user == data_admin[index_user][1] or key_user == data_admin[index_user][0] and password == data_admin [index_user][2]:
                print("Selamat anda berhasil Login")
                return True, index_user, data_admin
            else:
                print("\nPassword salah!")
                return False, -1, data_admin
        else:
            print("\nEmail atau Username tidak ditemukan!")
            return False, -1, data_admin
#list resep.csv
def list_resep():
    with open("resep.csv", "r") as file:
        lines = file.readlines()
    list_resep = []
    for line in lines[1:]:
        list_resep.append(line.strip().split(","))
    return list_resep

#tambah resep admin
def tambah_resep_admin():
    print("=== Tambah Resep===")
    with open("bahan.txt", "r") as file:
        lines = file.readlines()
    list_bahan =[]
    for line in lines:
        list_bahan.append(line.strip())

    #bahan dasar
    while True:
        print("Pilih Bahan Dasar")
        for i in range(len(list_bahan)):
            print(str(i+1) + ". " + list_bahan[i])
        pilih_bahan = input("Pilihanmu: ")
        valid_pilih = "1234567890"
        valid = True
        for i in pilih_bahan:
            if i not in valid_pilih:
                valid = False
        if valid:
            pilih_bahan = int(pilih_bahan)-1
            if pilih_bahan in range(len(list_bahan)):
                bahan = list_bahan[pilih_bahan]
                break
            else:
                print("Pilihan tidak ditemukan")
        else:
            print("Pilihan tidak ditemukan")

    #nama resep
    list_reseps = list_resep()

    nama_resep = input("Masukkan nama resep: ")
    for i in range(len(list_reseps)):
        if nama_resep == list_reseps[i][1]:
            print("Resep sudah ada")
            return

    bahan_resep = input("Masukkan bahan-bahan (pisahkan dengan titik koma ';'): ") #bahan
    langkah_resep = input("Masukkan langkah-langkah (pisahkan dengan titik koma ';'): ") #langkah-langkah

    new_resep = f"{bahan},{nama_resep},{bahan_resep},{langkah_resep}"
    with open ("resep.csv", "a") as file:
        file.write(f"{new_resep}\n")
        print("\nResep berhasil di tambahkan")

#hapus resep admin
def hapus_resep_admin():
    list_reseps = list_resep()
    list_nama_resep = []
    for i in range(len(list_reseps)):
        list_nama_resep.append(list_reseps[i][1])

    print("Pilih resep yang ingin di hapus: ")
    for i in range(len(list_reseps)):
        print(f"{i+1}. {list_reseps[i][1]}")

    pilih_reseps = input("Pilihanmu: ")
    valid_pilih = "1234567890"
    valid = True
    for i in pilih_reseps:
        if i not in valid_pilih:
            valid = False
    if valid:
        pilih_reseps = int(pilih_reseps)-1
        if pilih_reseps in range(len(list_reseps)):
            list_reseps.pop(pilih_reseps)
            with open("resep.csv", "w") as file:
                file.write("bahan_dasar,nama_resep,bahan_tambahan,langkah-langkah\n")
            with open("resep.csv", "a") as file:
                for item in list_reseps:
                    file.write(item[0] + "," + item[1]+ "," + item[2]+ "," + item[3]+"\n")
            print("Resep berhasil dihapus!")
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")
    
#mengubah resep admin
def ubah_resep_admin():
    list_reseps = list_resep()
    list_nama_resep = []
    for i in range(len(list_reseps)):
        list_nama_resep.append(list_reseps[i][1])

    print("Pilih resep yang ingin di ubah: ")
    for i in range(len(list_reseps)):
        print(f"{i+1}. {list_reseps[i][1]}")

    pilih_reseps = input("Pilihanmu: ")
    valid_pilih = "1234567890"
    valid = True
    for i in pilih_reseps:
        if i not in valid_pilih:
            valid = False
    if valid:
        pilih_reseps = int(pilih_reseps)-1
        if pilih_reseps in range(len(list_reseps)):
            bahan_resep = input("Masukkan bahan-bahan (pisahkan dengan titik koma ';'): ") #bahan
            langkah_resep = input("Masukkan langkah-langkah (pisahkan dengan titik koma ';'): ") #langkah-langkah
            list_reseps[pilih_reseps][2], list_reseps[pilih_reseps][3] = bahan_resep, langkah_resep
            with open("resep.csv", "w") as file:
                file.write("bahan_dasar,nama_resep,bahan_tambahan,langkah-langkah\n")
            with open("resep.csv", "a") as file:
                for item in list_reseps:
                    file.write(item[0] + "," + item[1]+ "," + item[2]+ "," + item[3]+"\n")
            print("Resep berhasil diubah!")
        else:
            print("Pilihan tidak ditemukan")
    else:
        print("Pilihan tidak ditemukan")
    
#menu admin
def menu_admin(index, data):
    while True:
        print(f"\n=== Halo Admin {data[index][3]}, Selamat datang di Mira Apps ===\nMy Intelligence Recipe Assistant\n\nApa yang ingin kamu lakukan sekarang?")
        print("1. Menambah resep\n2. Menghapus resep\n3. Mengubah resep\n4. Log Out")
        pilih_menu_admin = input("Pilihanmu: ")
        if pilih_menu_admin == "1":
            tambah_resep_admin()
        elif pilih_menu_admin == "2":
            hapus_resep_admin()
        elif pilih_menu_admin == "3":
            ubah_resep_admin()
        elif pilih_menu_admin == "4":
            print("Terimakasih telah menggunakan Mira Apps\n")
            break


        
#menu user
def menu_mira(index, data):
    while True:
        print(f"\n=== Halo {data[index][3]}, Selamat datang di Mira Apps ===\nMy Intelligence Recipe Assistant\n\nApa yang ingin kamu lakukan sekarang?")
        print("1. Mencari resep\n2. Menulis resep\n3. Profile\n4. Log Out")
        pilih_menu = input("Pilihanmu: ")

        if pilih_menu == "1":
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
                    else:
                        detail_resep(resep)
                    while True:
                        print("\n1. Melihat dan menulis comment\n2. Masukkan ke dalam Bookmark\n3. Back")
                        pilih = input("Pilih: ")
                        if pilih == "1":
                            comment(resep, index, data)
                        elif pilih == "2":
                            bookmark(resep, index, data)
                        elif pilih == "3":
                            break
                        else:
                            print("Pilihan tidak ditemukan")
        elif pilih_menu == "2":
            tambah_resep_pribadi(index, data)
        elif pilih_menu == "3":
            print(f"\n=== PROFILE ===\nProfile Name: {data[index][3]}\nUsername: @{data[index][0]}\nEmail: {data[index][1]}\n")
            while True:
                print("="*30 +"\n1. Bookmark\n2. Resep Pribadi\n3. Mengubah Profile Name\n4. Back")
                pilih_profile = input("Pilihanmu: ")
                if pilih_profile == "1":
                    while True:
                        print("\n1. Melihat Bookmark\n2. Menghapus Bookmark\n3. Back")
                        pilih_bookmark_profile = input("Pilihanmu: ")
                        if pilih_bookmark_profile == "1":
                            if profile_bookmark(index,data) != -1:
                                pilih_bookmark_user(index, data)
                        elif pilih_bookmark_profile == "2":
                            if profile_bookmark(index, data) != -1:
                                hapus_bookmark(index,data)
                        elif pilih_bookmark_profile == "3":
                            break
                        else:
                            print("Pilihan tidak ditemukan")
                elif pilih_profile == "2":
                    while True:
                        print("\n1. Melihat Resep Pribadi\n2. Menghapus Resep Pribadi\n3. Back")
                        pilih_resep_profile = input("Pilihanmu: ")
                        if pilih_resep_profile == "1":
                            if profile_resep_pribadi(index, data) != -1:
                                pilih_resep_pribadi(index,data)
                        elif pilih_resep_profile == "2":
                            if profile_resep_pribadi(index, data) != -1:
                                hapus_resep_prbadi(index,data)
                        elif pilih_resep_profile == "3":
                            break
                        else:
                            print("Pilihan tidak ditemukan")
                elif pilih_profile == "3":
                    change_name(data, index)
                elif pilih_profile == "4":
                    break
                else:
                    print("Pilihan tidak ditemukan")
        elif pilih_menu == "4":
            print("Terimakasih telah menggunakan Mira Apps\n")
            return
        else:
            print("Pilihan tidak ditemukan")

#program utama
while True:
    print("=== Selamat Datang di Mira Apps ===")
    print("1. Kamu seorang Pengguna\n2. Kamu seorang Admin\n3. Keluar")
    pilih = input("Pilihanmu: ")
    if pilih == "1":
        while True:
            print("1. Login\n2. Register\n3. Back")
            pilih_user = input("Pilihanmu: ")
            if (pilih_user == "1"):
                berhasil, index, data = login()
                if berhasil:
                    menu_mira(index, data)
            elif(pilih_user == "2"):
                register()
            elif (pilih_user == "3"):
                print("Selamat Tinggal")
                break
            else:
                print("Pilihan tidak ditemukan")
    elif pilih == "2":
        print("Ini Perintah Admin")
        berhasil, index, data = login_admin()
        if berhasil:
            menu_admin(index, data)
    elif pilih == "3":
        print("Selamat Tinggal")
        break
    else:
        print("Pilihan tidak ditemukan")
