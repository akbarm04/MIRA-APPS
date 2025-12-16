import function as fc

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
        print("\nLakukan Login")
        email = input("Masukkan Email: ")
        password = input("Masukkan Password: ")
        index_email = fc.cari_index_email(data_user, email)
            
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
        print("\nLakukan Sign Up")
        new_email = input("Masukkan Email: ")
        cek_at = fc.cek_at(new_email)
        confirm = fc.cari_index_email(data_user, new_email)

        if confirm == -1 and cek_at:
            break
        if not cek_at:
            print("Format email salah, silahkan masukkan email yang benar")
        else:
            print("Email sudah ada, silahkan gunakan email lain. ")

    new_username = input("Masukkan Username: ")
    new_password = input("Masukkan Password: ")

    new_data_user = f"{new_username} {new_email} {new_password}"
    with open ("data_user.txt", "a") as file:
        file.write(f"{new_data_user}\n")
    print("\nSign Up berhasil")

#menu setelah login
def menu_mira(username):
    while True:
        print(f"\nHalo {username}, Selamat datang di Mira Apps\nMy Intelligence Recipe Assistant\n\nApa yang ingin kamu lakukan sekarang?")
        print("1. Mencari resep\n2. Menulis resep\n3. Keluar")
        pilih_menu = input("Pilihanmu: ")

        if pilih_menu == "1":
            print("Silahkan pilih bahan dasar yang anda miliki:\n 1.")
        elif pilih_menu == "2":
            print("Fitur menulis resep masih dalam pengembangan")
        elif pilih_menu == "3":
            print("Terimakasih telah menggunakan Mira Apps")
            return
        else:
            print("Pilihan tidak ditemukan")

#program utama
while True:
    print("Selamat Datang di Mira Apps")
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