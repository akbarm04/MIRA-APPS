import function as fc

awal = True
while awal:
    with open("data_user.txt", "r") as file:
        lines = file.readlines()

    data_user = []
    for line in lines:
        new_line = line.strip( ).split( )
        data_user.append(new_line)

    print("Selamat Datang di Mira Apps")
    print("1. Login\n2. Sign Up\n3. Keluar")
    pilih = input("Pilihanmu: ")

    if (pilih == "1"): #Login
        while True:
            print("\nLakukan Login")
            email = input("Masukkan Email: ")
            password = input("Masukkan Password: ")
            index_email = fc.cari_index_email(data_user, email)
            if index_email != -1:
                if email == data_user[index_email][1] and password == data_user [index_email][2]:
                    print("Selamat anda berhasil Login")
                    lanjut = True
                    awal = False
                    break
                elif (index_email):
                    print("Password salah")
            else:
                print("Email tidak ditemukan\n")
                break

    elif(pilih == "2"): #Sign Up
        while True:
            print("\nLakukan Sign Up")
            new_email = input("Masukkan Email: ")
            cek_at = fc.cek_at(new_email)
            confirm = fc.cari_index_email(data_user, new_email)
            if confirm == -1 and cek_at == True:
                break
            if cek_at == False:
                print("Format email salah, silahkan masukkan email yang benar")
            else:
                print("Email sudah ada, silahkan gunakan email lain. ")
        new_username = input("Masukkan Username: ")
        new_password = input("Masukkan Password: ")
        new_data_user = f"{new_username} {new_email} {new_password}"
        with open ("data_user.txt", "a") as file:
            file.write(f"{new_data_user}\n")
        print("\nSign Up berhasil")
    elif (pilih == "3"):
        print("Selamat Tinggal")
        lanjut = False
        break
    else:
        print("Pilihan tidak ditemukan")

while lanjut:
    print(f"\nHalo {data_user[index_email][0]}, Selamat datang di Mira Apps\nMy Intelligence Recipe Assistant\n Apa yang ingin kamu lakukan sekarang?")
    print("1. Mencari resep\n2. Menulis resep\n3. Keluar")
    pilih_menu = input("Pilihanmu: ")

    if pilih_menu == 1:
        print("Silahkan pilih bahan dasar yang anda miliki:\n 1.")
