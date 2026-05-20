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


barang = {
    "pensil" : 2000,
    "buku" : 5000,
    "tas" : 20000
}

total = 0

for k in barang:
    print(k)

for k in barang:
    print(barang[k])
    total += barang[k]

print("Total harga barang: ",total)