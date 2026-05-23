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


def cek_lulus(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"

def tampil_data():
    if len(data) != 0:
        for i, item in enumerate(data):
            print(i+1,".",item["nama"],"-",item["kelas"],"-",item["nilai"],cek_lulus(item["nilai"]))
    else:
        print("Data tidak ditemukan")        

def tambah_data(nama, kelas, nilai):
    data.append({"nama": nama, "kelas": kelas, "nilai": nilai})

def hapus_data():
    for x in data:
        tampil_data()
        index = int(input("Masukkan nomor data yang ingin dihapus: "))-1
        if 0 <= index < len(data):
            del data[index]
            print("Data berhasil dihapus")
        else:
            print("Data tidak ditemukan")

            

while True:
    x = input("Masukkan pilihan: ")

    if x == "1":
        tampil_data()
        menu()
    elif x == "2":
        nama = input("Masukkan nama: ")
        kelas = input("Masukkan kelas: ")
        nilai = int(input("Masukkan nilai: "))
        tambah_data(nama, kelas, nilai)
        menu()
    elif x == "3":
        hapus_data()
        menu()
    elif x =="4":
        break
    else:
        print("Menu tidak ada")
        menu()