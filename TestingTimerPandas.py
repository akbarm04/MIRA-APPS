import pandas as pd
import time

# Membaca Resep #
Resep = pd.read_csv("resep.csv")

TimerResep = {}

for i in range(len(Resep)):
    Nama = Resep["nama_resep"][i].lower()
    Waktu = Resep["waktu"][i]
    TimerResep[Nama] = Waktu

print(TimerResep)

# Fungsi Timer #
def Timer(Menit):
    Detik = Menit * 60

    while Detik > 0:
        print(f"Sisa Waktu >> {Detik//60:02}:{Detik%60:02}")
        time.sleep(1)
        Detik -= 1

    print("Waktu habis!")

# Utama #
print("Daftar Resep:")
for Nama in TimerResep:
    print("-", Nama)

Pilihan = input("Pilih resep (atau q untuk keluar): ").lower()

if Pilihan == "q":
    print("Program dihentikan.")
elif Pilihan in TimerResep:
    Timer(TimerResep[Pilihan])
else:
    print("Resep tidak ditemukan.")