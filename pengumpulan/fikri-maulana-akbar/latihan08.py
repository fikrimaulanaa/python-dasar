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
def rata_rata(nilai):
    total = sum(nilai_)
    return total / len(nilai)

nilai_ = []
while True:
    nilai = int(input("Masukkan nilai: "))
    if nilai != 0:
        nilai_.append(nilai)
    else:
        break

x = len(nilai_)
total = rata_rata(nilai_)
print(total)