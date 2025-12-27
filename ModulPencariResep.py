def CariResep(Keyword,DaftarResep):
    Hasil = []
    Keyword = Keyword.lower()

    for Resep in DaftarResep:
        if Keyword in Resep["Nama"].lower():
            Hasil.append(Resep)

    return Hasil