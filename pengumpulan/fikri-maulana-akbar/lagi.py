daftar_buah = []

while True:

    print("\n===== MENU BUAH =====")
    print("1. Tambah Buah")
    print("2. Tampilkan Data")
    print("3. Tampilkan Warna")
    print("4. Keluar")

    pilihan = input("Pilih menu: " )

    if pilihan == "1":
        nama = input("Input nama buah: ")
        warna = input("Input warna buah: ")

        buah = {
            "Nama" : nama,
            "Warna" : warna
        }

        daftar_buah.append[buah]

        print("Buah berhasil ditambahkan")

    elif pilihan == "2":
        print("\n==== DAFTAR BUAH ====")
        
        if len(daftar_buah) == 0:
            print("Belum ada buah ditambahkan")

        else:
            for buah in daftar_buah:
                print("Nama buah: ",buah["Nama"])
                print("Warna buah: ",buah["Warna"])
                print("-------------------")

    elif pilihan == "3":
        print("\n===== WARNA UNIK =====")

        warna_unik = set()

        for buah in daftar_buah:
            warna_unik.add(buah["Warna"])

        for warna in warna_unik:
            print("-",warna)