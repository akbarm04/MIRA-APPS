def cari_index_email(list, cari):
    for i in range(len(list)):
        if list[i][1] == cari:
            return i
    return -1

def cek_at(email):
    if "@" in email:
        return True
    else:
        return False
