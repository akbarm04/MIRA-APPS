# program utama
from modules.auth import login, register, login_admin
from modules.user import menu_user
from modules.admin import menu_admin

border = "─" * 45
spasi = 45

while True:
    print(f"\n\n\n{border}")
    print("Selamat Datang di Mira Apps".center(spasi))
    print(border)
    print("1. Kamu seorang Pengguna\n2. Kamu seorang Admin\n3. Keluar")

    pilih = input("\nPilihanmu: ").strip()
    
    if pilih == "1":
        while True:
            print("\n1. Login\n2. Register\n3. Back")
            pilih_user = input("\nPilihanmu: ").strip()
            
            if pilih_user == "1":
                berhasil, index, data = login()
                if berhasil:
                    menu_user(index, data)
                    
            elif pilih_user == "2":
                register()
                
            elif pilih_user == "3":
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
