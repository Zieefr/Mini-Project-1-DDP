# Sistem Pendataan Daftar Warisan Budaya

# Tampilkan Menu
print("=== Sistem Pendataan Daftar Warisan Budaya ===")
print("1. Tambah Daftar Budaya")
print("2. Lihat Daftar Budaya")
print("3. Ubah Daftar Budaya")
print("4. Hapus Daftar Budaya")

# Input Menu
pilihan = input("Pilih menu (1-4): ")

# List Daftar Budaya
daftar_budaya = [
    ("Batik", "Yogyakarta", "Tak Benda", "2009"),
    ("Wayang", "Jawa Tengah",  "Benda", "2008"),
    ("Angklung", "Jawa Barat", "Benda", "2010"),
    ("Tari Saman", "Aceh", "Tak Benda", "2011"),
]

# Menambahkan Daftar Warisan Budaya
if pilihan == "1":
    print("Tambahkan Daftar Warisan Budaya")
    nama = input("Masukkan nama budaya: ")
    asal = input("Masukkan asal budaya: ")
    jenis = input("Masukkan jenis (Benda/Tak Benda): ")
    tahun = input("Masukkan tahun: ")
    
    budaya_baru = (nama, asal, jenis, tahun)
    daftar_budaya.append(budaya_baru)
    
    print("\nData berhasil ditambahkan.")
    print("Daftar terbaru:", daftar_budaya)

# Menampilkan Daftar Warisan Budaya
elif pilihan == "2":
    print("\nDaftar Warisan Budaya:")
    for budaya in daftar_budaya:
        print(budaya)

# Mengubah Data Daftar Warisan Budaya
elif pilihan == "3":
    print("\nDaftar Budaya:", daftar_budaya)
    indeks = int(input("Masukkan nomor indeks data yang ingin diubah (0,1,...): "))
    
    nama = input("Masukkan nama baru: ")
    asal = input("Masukkan asal baru: ")
    jenis = input("Masukkan jenis baru: ")
    tahun = input("Masukkan tahun baru: ")
    
    budaya_baru = (nama, asal, jenis, tahun)
    daftar_budaya[indeks] = budaya_baru
    
    print("\nData berhasil diubah.")
    print("Daftar terbaru:", daftar_budaya)

# Menghapus Data Daftar Warisan Budaya
elif pilihan == "4":
    print("\nDaftar Budaya:", daftar_budaya)
    indeks = int(input("Masukkan nomor indeks data yang ingin dihapus (0,1,...): "))
    
    del daftar_budaya[indeks]
    
    print("\nData berhasil dihapus.")
    print("Daftar terbaru:", daftar_budaya)

else:
    print("\nPilihan tidak valid.")