# Fungsi ambil data user dari file
def read_data(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        return data
    except FileNotFoundError:
        return []

# Fungsi membaca file sebagai list lines
def read_lines(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Fungsi menulis data ke file
def write_data(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write("|".join(item) + "\n")

# Fungsi menambahkan data ke file
def append_data(filename, line):
    with open(filename, "a") as file:
        file.write(line + "\n")

# Fungsi membaca file CSV
def read_csv(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split(","))
        return data
    except FileNotFoundError:
        return []

# Fungsi menulis data ke file CSV
def write_csv(filename, data, header=None):
    with open(filename, "w") as file:
        if header:
            file.write(",".join(header) + "\n")
        for item in data:
            file.write(",".join(item) + "\n")