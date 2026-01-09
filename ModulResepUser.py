def InputResepUser():
    Nama = input("Nama resep Anda: ")

    print("Masukkan langkah (ketik 'selesai' untuk berhenti): ")
    Langkah = []
    Nomor = 1

    while True:
        Baris = input(f"Langkah {Nomor}: ")
        if Baris.strip().lower() == "selesai":
            break
        Langkah.append(f"{Nomor}. {Baris}")
        Nomor += 1

    return Nama, Langkah