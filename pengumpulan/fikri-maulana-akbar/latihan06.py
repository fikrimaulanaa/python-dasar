# for i in range(1,20,2):
#     print(i)


# angka = int(input("Masukkan angka: "))

# for i in range(11):
#     print(angka*i)


jumlah_siswa = int(input("Masukkan jumlah siswa: "))
i = 0
total = 0

while i <= jumlah_siswa-1:
    i += 1
    nilai_siswa = int(input("Masukkan nilai siswa: "))
    total += nilai_siswa

print("Total: ",total)


# angka = None
# total = 0

# while angka != 0:
#     angka = int(input("Masukkan angka: "))
#     total += angka

# print("total: ", total)


# for i in range(6):
#     print("*" * i)

# for i in range(5,0,-1):
#     print("*" * i)

# for i in range(5,0,-1):
#     print(" " * (i-1),"*" * (5-i+1))

# for i in range(1,6,1):
#     print(" " * (i-1),"*" * (5-((i-1))))