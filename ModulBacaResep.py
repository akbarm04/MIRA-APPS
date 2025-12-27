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
