import time

# Membaca List Resep #
def BacaNamaResepCSV(NamaFile):
    NamaResep = []
    with open(NamaFile, "r", encoding="utf-8") as f:
        Baris = f.readlines()

    for i in range(1, len(Baris)):
        Kolom = Baris[i].strip().split(",")
        NamaResep.append(Kolom[1].lower())

    return NamaResep

# Timer Resep (Manual) #
TimerResep = {
    "ayam kecap": 10,
    "ayam goreng marinasi": 12,
    "perkedel kentang": 15,
    "mashed potatto creamy garlic": 20,
    "telur balado": 8
}

# Percobaan Timer #
def JalankanTimer(NamaResep):
    if NamaResep not in TimerResep:
        print("Resep belum punya timer.")
        return

    Detik = TimerResep[NamaResep] * 60
    print(f"Timer {NamaResep} dimulai")

    while Detik > 0:
        print(f"{Detik//60:02d}:{Detik%60:02d}")
        time.sleep(1)
        Detik -= 1

    print("Masakan siap!")

# Utama #
ResepCSV = BacaNamaResepCSV("resep.csv")

print("Daftar Resep:")
for r in ResepCSV:
    print("-", r)

Pilihan = input("Pilih resep: ").lower()
JalankanTimer(Pilihan)