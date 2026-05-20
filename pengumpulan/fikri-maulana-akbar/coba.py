# =========================================
# PROGRAM MANAJEMEN PERPUSTAKAAN SEDERHANA
# Menerapkan:
# List, Dictionary, Tuple, dan Set
# =========================================

# LIST -> Menyimpan semua data buku
daftar_buku = []

# TUPLE -> Data tetap / tidak bisa diubah
kategori = ("Novel", "Komik", "Teknologi", "Sejarah", "Fantasi")


# =========================================
# FUNCTION TAMBAH BUKU
# =========================================
def tambah_buku():
    print("\n===== TAMBAH BUKU =====")

    id_buku = int(input("Masukkan ID Buku: "))
    judul = input("Masukkan Judul Buku: ")
    penulis = input("Masukkan Nama Penulis: ")
    tahun = int(input("Masukkan Tahun Terbit: "))
    genre = input("Masukkan Genre: ")

    # DICTIONARY -> Menyimpan detail buku
    buku = {
        "id": id_buku,
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "genre": genre
    }

    # Menambahkan buku ke LIST
    daftar_buku.append(buku)

    print("Buku berhasil ditambahkan!")


# =========================================
# FUNCTION TAMPILKAN BUKU
# =========================================
def tampilkan_buku():
    print("\n===== DAFTAR BUKU =====")

    if len(daftar_buku) == 0:
        print("Belum ada data buku.")
    else:
        for buku in daftar_buku:
            print("-------------------------")
            print("ID      :", buku["id"])
            print("Judul   :", buku["judul"])
            print("Penulis :", buku["penulis"])
            print("Tahun   :", buku["tahun"])
            print("Genre   :", buku["genre"])


# =========================================
# FUNCTION CARI BUKU
# =========================================
def cari_buku():
    print("\n===== CARI BUKU =====")

    cari = input("Masukkan judul buku: ")

    ditemukan = False

    for buku in daftar_buku:
        if buku["judul"].lower() == cari.lower():
            print("\nBuku ditemukan!")
            print("ID      :", buku["id"])
            print("Judul   :", buku["judul"])
            print("Penulis :", buku["penulis"])
            print("Tahun   :", buku["tahun"])
            print("Genre   :", buku["genre"])

            ditemukan = True

    if ditemukan == False:
        print("Buku tidak ditemukan.")


# =========================================
# FUNCTION HAPUS BUKU
# =========================================
def hapus_buku():
    print("\n===== HAPUS BUKU =====")

    id_hapus = int(input("Masukkan ID Buku yang ingin dihapus: "))

    ditemukan = False

    for buku in daftar_buku:
        if buku["id"] == id_hapus:
            daftar_buku.remove(buku)
            print("Buku berhasil dihapus!")
            ditemukan = True
            break

    if ditemukan == False:
        print("ID buku tidak ditemukan.")


# =========================================
# FUNCTION TAMPILKAN GENRE UNIK
# =========================================
def tampilkan_genre():
    print("\n===== GENRE UNIK =====")

    # SET -> Menyimpan genre tanpa duplikasi
    genre_unik = set()

    for buku in daftar_buku:
        genre_unik.add(buku["genre"])

    if len(genre_unik) == 0:
        print("Belum ada genre.")
    else:
        for genre in genre_unik:
            print("-", genre)


# =========================================
# PROGRAM UTAMA
# =========================================
while True:

    print("\n===== MENU PERPUSTAKAAN =====")
    print("1. Tambah Buku")
    print("2. Tampilkan Buku")
    print("3. Cari Buku")
    print("4. Hapus Buku")
    print("5. Tampilkan Genre Unik")
    print("6. Tampilkan Kategori")
    print("7. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_buku()

    elif pilihan == "2":
        tampilkan_buku()

    elif pilihan == "3":
        cari_buku()

    elif pilihan == "4":
        hapus_buku()

    elif pilihan == "5":
        tampilkan_genre()

    elif pilihan == "6":
        print("\nKategori Buku:")
        for k in kategori:
            print("-", k)

    elif pilihan == "7":
        print("Program selesai.")
        break

    else:
        print("Menu tidak tersedia.")