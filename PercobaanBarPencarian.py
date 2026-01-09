def BacaResepDariFile(NamaFile):
    ListResep = []

    with open(NamaFile, "r", encoding="utf-8") as f:
        Blok = f.read().strip().split("\n\n")

    for b in Blok:
        Baris = b.split("\n")
        Nama = Baris[0]
        Langkah = Baris[1:]

        ListResep.append({
            "Nama": Nama,
            "Langkah": Langkah
        })

    return ListResep

def CariResep(Keyword, DaftarResep):
    Hasil = []
    Keyword = Keyword.lower()

    for Resep in DaftarResep:
        if Keyword in Resep["Nama"].lower():
            Hasil.append(Resep)

    return Hasil

def Pencarian():
    Resep = BacaResepDariFile("resep.txt")

    KataKunci = input("Cari resep yang Anda inginkan: ")
    Hasil = CariResep(KataKunci, Resep)

    if Hasil:
        for r in Hasil:
            print("\n" + r["Nama"])
            for Langkah in r["Langkah"]:
                print(Langkah)
    else:
        print("Resep tidak ditemukan.")

Pencarian()