from utils.file_utils import baca_data, baca_baris, tambah_data, tulis_data

# Fungsi filter comment
def filter_komentar(text):
    comment_lower = text.lower()
    kata_pisah = comment_lower.split()
    
    kata_terlarang = baca_baris("data/id_badwords.txt")
    
    for i in range(len(kata_pisah)):
        if kata_pisah[i] in kata_terlarang:
            return -1
        
    if "|" in text:
        return -2
    else:
        return text

# Fungsi lihat comment sesuai resep 
def ambil_komentar_untuk_resep(nama_resep):
    semua_komentar = baca_data("data/comment.txt")
    komentar_resep = []
    
    for komentar in semua_komentar:
        if komentar[0] == nama_resep:
            komentar_resep.append(komentar)
    
    return komentar_resep

# Melihat dan menulis comment
def manage_comments(resep, user_index, user_data):
    while True:
        komentar_resep = ambil_komentar_untuk_resep(resep["nama"])
        
        if len(komentar_resep) > 0:
            for komentar in komentar_resep:
                print("\n" + "=" * 50)
                print(f"Pengirim: {komentar[1]}")
                print(f"Username: @{komentar[2]}")
                print(f"Comment:\n{komentar[3]}")
                print("=" * 50)
        else:
            print("\n" + "=" * 50)
            print("Belum ada comment di resep ini")
            print("=" * 50 + "\n")
        
        print("1. Menulis comment")
        print("2. Back")
        pilihan = input("Pilihanmu: ").strip()
        
        if pilihan == "1":
            komentar_text = input("Silahkan tulis komentarmu:\n").strip()
            komentar_filter = filter_komentar(komentar_text)
            
            if komentar_text == "":
                print("Komentar tidak boleh kosong")
            elif komentar_filter == -1:
                print("Dilarang menggunakan kata yang tidak pantas!")
                break
            elif komentar_filter == -2:
                print('Maaf tidak bisa menggunakan simbol "|"')
                break
            else:
                komentar_baru = f"{resep['nama']}|{user_data[user_index][3]}|{user_data[user_index][0]}|{komentar_text}"
                tambah_data("data/comment.txt", komentar_baru)
                print("\nComment berhasil di tambahkan")
                
                komentar_resep = ambil_komentar_untuk_resep(resep["nama"])
                for komentar in komentar_resep:
                    print("\n" + "=" * 50)
                    print(f"Pengirim: {komentar[1]}")
                    print(f"Username: @{komentar[2]}")
                    print(f"Comment:\n{komentar[3]}")
                    print("=" * 50)
                break
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak ditemukan\n")