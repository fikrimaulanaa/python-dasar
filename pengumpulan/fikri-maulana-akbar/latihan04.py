# umur = int(input("Masukkan umur: "))

# if umur >= 17:
#     print("Dewasa")
# else:
#     print("Belum dewasa")

# nilai = int(input("Masukkan nilai: "))

# if nilai >= 90:
#     print("A")
# elif nilai >= 80:
#     print("B")
# elif nilai >= 75:
#     print("C")
# else:
#     print("D")

# nama = input("Masukkan nama siswa: ")
# nilai = int(input("Masukkan nilai siswa: "))

# print("===== HASIL =====")
# print("Nama: ",nama)
# print("Nilai: ",nilai)

# if nilai >= 90:
#     print("Grade: A")
# elif nilai >= 80:
#     print("Grade: B")
# elif nilai >= 70:
#     print("Grade: C")
# else:
#     print("Grade: D")

# if nilai >= 80:
#     print("Status: Lulus")
# else:
#     print("Status: Gagal")

# print("================")

nama = input("Masukkan nama: ")
nilai_teori = int(input("Masukkan nilai ujian teori: "))
nilai_praktek = int(input("Masukkan nilai ujian praktek: "))

print("===== HASIL UJIAN SIM =====")
print("Nama: ",nama)
print("Nilai teori: ",nilai_teori)
print("Nilai praktek: ",nilai_praktek)

if nilai_teori > 90:
    if nilai_praktek > 90:
        print("Status: Lulus")
    else:
        print("Status: Lulus Bersyarat")

else:
    if nilai_praktek > 90:
        print("Status: Lulus Bersyarat")
    else:
        print("Status: Tidak Lulus")

print("==========================")