from utils.file_utils import baca_baris, baca_data, tambah_data

# Fungsi filter comment
def filter_comment(comment):
    text = comment
    comment_lower = text.lower()
    comment_pisah = comment_lower.split()
    
    kata_terlarang = baca_baris("data/id_badwords.txt")

    for i in range(len(comment_pisah)):
        if comment_pisah[i] in kata_terlarang:
            return -1
        
    if "|" in text:
        return -2
    else:
        return text

# Fungsi ambil data comment
def data_comment():
    return baca_data("data/comment.txt")

# Fungsi list comment sesuai pilihan 
def lihat_comment(data, resep):
    list_comment = []
    for item in data:
        if item[0] == resep:
            list_comment.append(item)
    return list_comment

# Melihat dan menulis comment
def comment(resep, index, data):
    while True:
        list_comment = data_comment()
        lihat_comment_resep = lihat_comment(list_comment, resep["nama"])
        
        # Menampilkan comment yang sudah ada
        if len(lihat_comment_resep) > 0:
            for i in range(len(lihat_comment_resep)):
                print("\n" + "=" * 50)
                print(f"Pengirim: {lihat_comment_resep[i][1]}")
                print(f"Username: @{lihat_comment_resep[i][2]}")
                print(f"Comment:\n{lihat_comment_resep[i][3]}")
                print("=" * 50)
        else:
            print("\n" + "=" * 50)
            print("Belum ada comment di resep ini")
            print("=" * 50 +"\n")
        
        print("1. Menulis comment")
        print("2. Back")
        pilih_tulis = input("Pilihanmu: ")
        
        if pilih_tulis == "1":
            comment_text = input("Silahkan tulis komentarmu:\n").strip()
            filtered_comment = filter_comment(comment_text)
            
            if comment_text == "":
                print("Komentar tidak boleh kosong")
            elif filtered_comment == -1:
                print("Dilarang menggunakan kata yang tidak pantas!")
                break
            elif filtered_comment == -2:
                print('Maaf tidak bisa menggunakan simbol "|"')
                break
            else:
                new_comment = f"{resep['nama']}|{data[index][3]}|{data[index][0]}|{comment_text}"
                tambah_data("data/comment.txt", new_comment)
                print("\nComment berhasil di tambahkan")
                
                # Tampilkan ulang
                list_comment = data_comment()
                lihat_comment_resep = lihat_comment(list_comment, resep["nama"])
                for i in range(len(lihat_comment_resep)):
                    print("\n" + "=" * 50)
                    print(f"Pengirim: {lihat_comment_resep[i][1]}")
                    print(f"Username: @{lihat_comment_resep[i][2]}")
                    print(f"Comment:\n{lihat_comment_resep[i][3]}")
                    print("=" * 50)
                break
                
        elif pilih_tulis == "2":
            break
        else:
            print("Pilihan tidak ditemukan\n")