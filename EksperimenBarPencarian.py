from ModulBacaResep import BacaResepDariFile
from ModulPencariResep import CariResep

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