def baca_data(nama_file):
#Baca data dari file
    with open(nama_file, "r") as file:
        lines = file.readlines()
    data = []
    for line in lines:
        data.append(line.strip().split("|"))
    return data

def baca_baris(nama_file):
#Baca file sebagai list of lines
    with open(nama_file, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def tulis_data(nama_file, data):
#Tulis data ke file
    with open(nama_file, "w") as file:
        for item in data:
            file.write("|".join(item) + "\n")

def tambah_data(nama_file, baris):
#Tambah baris ke file
    with open(nama_file, "a") as file:
        file.write(baris + "\n")

def baca_csv(nama_file):
#Baca file CSV
    with open(nama_file, "r") as file:
        lines = file.readlines()
    data = []
    for line in lines:
        data.append(line.strip().split(","))
    return data

def tulis_csv(nama_file, data, header=None):
#Tulis data ke CSV
    with open(nama_file, "w") as file:
        if header:
            file.write(",".join(header) + "\n")
        for item in data:
            file.write(",".join(item) + "\n")