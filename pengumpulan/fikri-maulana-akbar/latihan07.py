# nama = ["Andi", "Budi", "Citra"]

# print(nama[0],nama[1],nama[2])
# print(nama[0])
# print(nama[-1])


# nilai = [60, 75, 80, 55, 90]
# x = 0

# for n in nilai:
#     if n >= 75:
#         print(n)
#         x += 1

# print("Jumlah siswa yang lulus: ",x)


# barang = {
#     "pensil" : 2000,
#     "buku" : 5000,
#     "tas" : 20000
# }

# total = 0

# for k in barang:
#     print(k)

# for k in barang:
#     print(barang[k])
#     total += barang[k]

# print("Total harga barang: ",total)

data = [
    {"nama": "Andi", "nilai": 80, "kelas": "7A"},
    {"nama": "Budi", "nilai": 60, "kelas": "7A"},
    {"nama": "Citra", "nilai": 90, "kelas": "7B"}
]

for siswa in data:
    print(siswa["nama"]," - ",siswa["nilai"]," - ",siswa["kelas"])

for siswa in data:
    if siswa["nilai"] >= 75:
        print(siswa["nama"],": Lulus")

tertinggi = 0
nama_tertinggi = ""

for siswa in data:
    if siswa["nilai"] > tertinggi:
        tertinggi = siswa["nilai"]
        nama_tertinggi = siswa["nama"]

print("nilai tertinggi: ",nama_tertinggi,"-",tertinggi)