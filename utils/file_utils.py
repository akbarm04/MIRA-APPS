# Fungsi ambil data dari file
def baca_data(nama_file):
    file = open(nama_file, "r")
    lines = file.readlines()
    file.close()
    
    data = []
    for line in lines:
        data.append(line.strip().split("|"))
    return data

# Fungsi membaca file sebagai list lines
def baca_baris(nama_file):
    file = open(nama_file, "r")
    lines = file.readlines()
    file.close()
    
    data_baris = []
    for line in lines:
        data_baris.append(line.strip())
    return data_baris

# Fungsi menulis data ke file
def tulis_data(nama_file, data):
    file = open(nama_file, "w")
    for item in data:
        file.write("|".join(item) + "\n")
    file.close()

# Fungsi menambahkan data ke file
def tambah_data(nama_file, baris):
    file = open(nama_file, "a")
    file.write(baris + "\n")
    file.close()

# Fungsi membaca file CSV
def baca_csv(nama_file):
    file = open(nama_file, "r")
    lines = file.readlines()
    file.close()
    
    data = []
    for line in lines:
        data.append(line.strip().split(","))
    return data

# Fungsi menulis data ke file CSV
def tulis_csv(nama_file, data, header=None):
    file = open(nama_file, "w")
    if header:
        file.write(",".join(header) + "\n")
    for item in data:
        file.write(",".join(item) + "\n")
    file.close()