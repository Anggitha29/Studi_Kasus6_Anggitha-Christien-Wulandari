import json

with open ("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)


# Membaca data dari file JSON
while True:
    print("=== SISTEM MANAJEMEN INVENTARIS BARANG ===")
    print("1. Tampilkan Data Barang")
    print("2. Tambah Data Barang")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("=== DATA INVENTARIS BARANG ===")

        if len(data) == 0:
            print("Belum ada data barang.")
        else:
            for barang in data:
                print("Kode Barang :", barang["kode_barang"])
                print("Nama Barang :", barang["nama"])
                print("Kategori    :", barang["kategori"])
                print("Harga       :", barang["harga"])
                print("Stok        :", barang["stok"])
                print("Satuan      :", barang["satuan"])
                print("-" * 30)

    elif pilihan == "2":
        print("=== TAMBAH DATA BARANG ===")
        print("1. Makanan")
        print("2. Minuman")
        print("3. Alat Tulis")

        kategori = input("Pilih kategori: ")

        if kategori == "1":
            nama_kategori = "Makanan"
            kode_awal = "M"

        elif kategori == "2":
            nama_kategori = "Minuman"
            kode_awal = "MN"

        elif kategori == "3":
            nama_kategori = "Alat Tulis"
            kode_awal = "AT"

        else:
            print("Kategori tidak tersedia.")
            continue

        nama = input("Nama barang : ")
        harga = int(input("Harga       : "))
        stok = int(input("Stok        : "))
        satuan = input("Satuan      : ")

        nomor = 1

        for barang in data:
            if barang["kategori"] == nama_kategori:
                nomor = nomor + 1

        kode_barang = kode_awal + str(nomor).zfill(3)

        barang_baru = {
            "kode_barang": kode_barang,
            "nama": nama,
            "kategori": nama_kategori,
            "harga": harga,
            "stok": stok,
            "satuan": satuan
        }

        data.append(barang_baru)

        # Menyimpan data ke file JSON
        with open("Data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print("Data barang berhasil ditambahkan.")
        print("Kode Barang :", kode_barang)

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")


