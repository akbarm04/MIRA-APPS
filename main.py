from modules import auth, user, admin

def main():
    while True:
        print("=== Selamat Datang di Mira Apps ===")
        print("1. Kamu seorang Pengguna\n2. Kamu seorang Admin\n3. Keluar")
        pilih = input("Pilihanmu: ").strip()
        
        if pilih == "1":
            user_flow()
        elif pilih == "2":
            admin_flow()
        elif pilih == "3":
            print("Selamat Tinggal")
            break
        else:
            print("Pilihan tidak ditemukan")

def user_flow():
    while True:
        print("1. Login\n2. Register\n3. Back")
        pilih_user = input("Pilihanmu: ").strip()
        
        if pilih_user == "1":
            success, user_index, user_data = auth.login_user()
            if success:
                user.user_menu(user_index, user_data)
        elif pilih_user == "2":
            auth.register_user()
        elif pilih_user == "3":
            break
        else:
            print("Pilihan tidak ditemukan")

def admin_flow():
    success, admin_index, admin_data = auth.login_admin()
    if success:
        admin.admin_menu(admin_index, admin_data)

if __name__ == "__main__":
    main()