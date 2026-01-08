from utils.file_utils import baca_baris

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
                new_comment = f"{resep['nama']}|{data[index][3]}|{data[index][0]}|{comment}"
                with open ("comment.txt", "a") as file:
                    file.write(f"{new_comment}\n")
                print("\nComment berhasil di tambahkan")
                lihat_comment_resep = lihat_comment(list_comment, resep["nama"])
                for i in range(len(lihat_comment_resep)):
                    print("\n" + "=" * 50 + f"\nPengirim: {lihat_comment_resep[i][1]}\nUsername: @{lihat_comment_resep[i][2]}\nComment:\n{lihat_comment_resep[i][3]}\n"+ "=" * 50)
                    break
        elif pilih_tulis == "2":
            detail_resep(resep)
            break
        else:
            print("Pilihan tidak ditemukan\n")