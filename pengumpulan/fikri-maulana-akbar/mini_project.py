data = [
    {"nama": "Andi", "kelas": "7A", "nilai": 80}
]

def menu():
    print("\n=== SISTEM DATA SISWA ===")
    print("1. Lihat data: ")
    print("2. Tambah data: ")
    print("3. Hapus data: ")
    print("4. Keluar: ")

menu()

def tampil_data():
    for i in data:
        print(i["nama"],"-",i["kelas"],"-",i["nilai"])

def tambah_data(nama, kelas, nilai):
    data.append({"nama": nama, "kelas": kelas, "nilai": nilai})

def hapus_data(nama):
    # for x, y, z in enumerate(data):
    for x in data:
        if x["nama"]==nama:
            # print("a")
            index =
            data.pop(index)
            # data.remove(x["kelas"])
            # data.remove(x["nilai"])

while True:
    x = input("Masukkan pilihan: ")

    if x == "1":
        tampil_data()
        menu()
    elif x == "2":
        nama = input("Masukkan nama: ")
        kelas = input("Masukkan kelas: ")
        nilai = input("Masukkan nilai: ")
        tambah_data(nama, kelas, nilai)
        menu()
    elif x == "3":
        nama = input("Masukkan nama:")
        hapus_data(nama)
        menu()
    elif x =="4":
        break
    else:
        print("Menu tidak ada")
        menu()