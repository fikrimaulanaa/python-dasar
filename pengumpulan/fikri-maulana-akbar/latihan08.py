# def sapa(nama):
#     print("Halo: ",nama)

# sapa("fikri")
# sapa("andi")
# sapa("fakhri")
# sapa("rifqi")
# sapa("aji")

# while True:
#     nilai_ = []
#     nilai = int(input("Masukkan nilai: "))

#     def rata_rata(nilai):
#         jumlah = 0
#         while nilai != 0:
#             jumlah += nilai
#             return nilai_.append(nilai)

#     rata_rata(nilai)


#     if nilai == 0:
#         break


# def rata_rata(nilai):
#     total = sum(nilai_)
#     return total / len(nilai)

# nilai_ = []
# while True:
#     nilai = int(input("Masukkan nilai: "))
#     if nilai != 0:
#         nilai_.append(nilai)
#     else:
#         break

# x = len(nilai_)
# total = rata_rata(nilai_)
# print(total)


# data = [
#     {"nama": "Andi", "nilai": 80},
#     {"nama": "Budi", "nilai": 60},
#     {"nama": "Citra", "nilai": 90}
# ]

# def menu():
#     print("\n==== data nilai siswa ====")
#     print("1. Cek kelulusan siswa")
#     print("2. Rata-rata nilai seluruh siswa")
#     print("3. Tampilkan semua data siswa")
#     print("4. Rata-rata nilai seluruh siswa")

# menu()

# def cek_lulus(nama):
#     for i in data:
#         if i["nama"]==nama:
#             if i["nilai"] >= 75:
#                 print("Status: Lulus")
#             else:
#                 print("Status: Belum Lulus")
#             return
#     print("Nama tidak tersedia")

# def rata_rata():
#     y = sum(i["nilai"] for i in data)
#     print(y/len(data))

# def semua_data():
#     for i in data:
#         print("Nama: ",i["nama"], "-","Nilai: ", i["nilai"])

# while True:
#     x = input("Masukkan pilihan: ")

#     if x == "1":
#         nama = input("Masukkan nama siswa: ")
#         cek_lulus(nama)
#         menu()
#     elif x == "2":
#         rata_rata()
#         menu()
#     elif x == "3":
#         semua_data()
#         menu()
#     elif x == "4":
#         rata_rata()
#         menu()
#     elif x == "0":
#         break
#     else:
#         print("Menu tidak tersedia")
#         menu()
