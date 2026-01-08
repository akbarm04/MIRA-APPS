# Fungsi membaca semua data dari file (general)
def baca_semua(nama_file):
    file = open(nama_file, "r")
    lines = file.readlines()
    file.close()
    
    data = []
    for line in lines:
        data.append(line.strip())
    return data

# Fungsi untuk membaca CSV khusus resep.csv
def baca_resep_csv():
    file = open("data/resep.csv", "r")
    lines = file.readlines()
    file.close()
    
    data = []
    for line in lines:
        data.append(line.strip().split(","))
    return data