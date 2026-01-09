def menu_user(index, data):

    while True:
        print(f"\n=== Halo {data[index][3]}, Selamat datang di Mira Apps ===")
        print("My Intelligence Recipe Assistant")
        print("\nApa yang ingin kamu lakukan sekarang?")
        print("1. Mencari resep")
        print("2. Menulis resep") 
        print("3. Profile")
        print("4. Log Out")
        
        pilih_menu = input("Pilihanmu: ").strip()
        
        if pilih_menu == "1":
            # Import di dalam fungsi untuk hindari circular import
            from .recipe import alur_cari_resep
            alur_cari_resep(index, data)
            
        elif pilih_menu == "2": 
            dari_profile = False
            tambah_resep_pribadi_flow(index, data, dari_profile)
            
        elif pilih_menu == "3":
            from .profile import menu_profile
            menu_profile(index, data)
            
        elif pilih_menu == "4":
            print("Terimakasih telah menggunakan Mira Apps\n")
            return
            
        else:
            print("Pilihan tidak ditemukan")

def tambah_resep_pribadi_flow(index, data, dari_profile=False):
    """Alur tambah resep pribadi"""
    from .profile import tambah_resep_pribadi
    tambah_resep_pribadi(index, data)
    
    if not dari_profile:
        input("\nTekan Enter untuk kembali ke menu utama...")

# Alias untuk compatibility
menu_mira = menu_user