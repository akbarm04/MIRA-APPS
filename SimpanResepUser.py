from ModulResepUser import InputResepUser

def SimpanResep(Nama, Langkah, NamaFile="resep.txt"):
    with open(NamaFile, "a", encoding="utf-8") as f:
        f.write(Nama + "\n")
        for LangkahResep in Langkah:
            f.write(LangkahResep + "\n")
        f.write("\n")

Nama, Langkah = InputResepUser()
SimpanResep(Nama, Langkah)

print("Resep Anda berhasil disimpan!")