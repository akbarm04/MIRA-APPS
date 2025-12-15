def baca_resep_dari_file(nama_file):
    resep_list = []

    with open(nama_file, "r", encoding="utf-8") as f:
        blok = f.read().strip().split("\n\n")

    for b in blok:
        baris = b.split("\n")
        nama = baris[0]
        langkah = baris[1:]

        resep_list.append({
            "nama": nama,
            "langkah": langkah
        })

    return resep_list

def cari_resep(keyword, daftar_resep):
    hasil = []
    keyword = keyword.lower()

    for resep in daftar_resep:
        if keyword in resep["nama"].lower():
            hasil.append(resep)

    return hasil

resep = baca_resep_dari_file("resep.txt")

kata_kunci = input("Cari resep: ")
hasil = cari_resep(kata_kunci, resep)

if hasil:
    for r in hasil:
        print("\n", r["nama"])
        for langkah in r["langkah"]:
            print(langkah)
else:
    print("Resep tidak ditemukan.")
