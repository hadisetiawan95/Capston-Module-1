
# Data Mobil
list_data_mobil = [
    {'nama mobil': 'toyota avanza',
     'tahun': 2016,
     'jumlah penumpang': 7,
     'harga sewa': 300000,
     'status': 'tersedia'},

    {'nama mobil': 'toyota innova',
     'tahun': 2018,
     'jumlah penumpang': 7,
     'harga sewa': 350000,
     'status': 'kosong'},

    {'nama mobil': 'honda c-rv',
     'tahun': 2018,
     'jumlah penumpang': 5,
     'harga sewa': 400000,
     'status': 'tersedia'}
]

# Fungsi untuk Menampilkan Data Mobil
def tampilkan_data():
    for i, mobil in enumerate(list_data_mobil, 1):
        print(f"\nData Mobil {i}:")
        for key, value in mobil.items():
            print(f"{key}: {value}")
        print("-" * 20)

# Fungsi untuk Menambahkan Data Mobil
def tambahkan_data():
    nama_mobil = input("Masukkan nama mobil: ")
    tahun = int(input("Masukkan tahun mobil: "))
    jumlah_penumpang = int(input("Masukkan jumlah penumpang: "))
    harga_sewa = int(input("Masukkan harga sewa: "))
    status = input("Masukkan status mobil (tersedia/kosong): ")

    mobil_baru = {'nama mobil': nama_mobil,
                  'tahun': tahun,
                  'jumlah penumpang': jumlah_penumpang,
                  'harga sewa': harga_sewa,
                  'status': status}

    list_data_mobil.append(mobil_baru)
    print("Data mobil berhasil ditambahkan.")

# Fungsi untuk Mengedit Data Mobil
def edit_data():
    tampilkan_data()
    nomor_mobil = int(input("Masukkan nomor mobil yang ingin diubah: ")) - 1

    if 0 <= nomor_mobil < len(list_data_mobil):
        mobil = list_data_mobil[nomor_mobil]
        print("\nData mobil sebelum diubah:")
        for key, value in mobil.items():
            print(f"{key}: {value}")

        mobil['nama mobil'] = input("masukan nama mobil baru: ")
        mobil['tahun'] = int(input("Masukkan tahun mobil yang baru: "))
        mobil['jumlah penumpang'] = int(input("Masukkan jumlah penumpang yang baru: "))
        mobil['harga sewa'] = int(input("Masukkan harga sewa yang baru: "))
        mobil['status'] = input("Masukkan status mobil yang baru (tersedia/kosong): ")

        print("\nData mobil setelah diubah:")
        for key, value in mobil.items():
            print(f"{key}: {value}")

        print("Data mobil berhasil diubah.")
    else:
        print("Nomor mobil tidak valid.")

# Fungsi untuk Menghapus Data Mobil
def hapus_data():
    tampilkan_data()
    nomor_mobil = int(input("Masukkan nomor mobil yang ingin dihapus: ")) - 1

    if 0 <= nomor_mobil < len(list_data_mobil):
        mobil = list_data_mobil[nomor_mobil]
        print("\nData mobil sebelum dihapus:")
        for key, value in mobil.items():
            print(f"{key}: {value}")

        konfirmasi = input("Apakah Anda yakin ingin menghapus data mobil ini? (ya/tidak): ").lower()
        if konfirmasi == "ya":
            list_data_mobil.pop(nomor_mobil)
            print("Data mobil berhasil dihapus.")
        else:
            print("Penghapusan data mobil dibatalkan.")
    else:
        print("Nomor mobil tidak valid.")

# Fungsi untuk Menyewa Mobil
def sewa_mobil():
    tampilkan_data()
    nomor_mobil = int(input("Masukkan nomor mobil yang ingin disewa: ")) - 1

    if 0 <= nomor_mobil < len(list_data_mobil):
        mobil = list_data_mobil[nomor_mobil]

        if mobil['status'].lower() == 'tersedia':
            mobil['status'] = 'disewa'
            print("Mobil berhasil disewa.")
        else:
            print("Maaf, mobil ini tidak tersedia untuk disewa saat ini.")
    else:
        print("Nomor mobil tidak valid.")

# Program Utama
while True:
    print('''
    Menu Rental Mobil:
    1. Tampilkan data mobil
    2. Tambahkan data mobil
    3. Edit data mobil
    4. Hapus data mobil
    5. Sewa Mobil
    6. Keluar
    ''')

    pilihan = input("Pilih menu (1/2/3/4/5/6): ")

    if pilihan == '1':
        tampilkan_data()
    elif pilihan == '2':
        tambahkan_data()
    elif pilihan == '3':
        edit_data()
    elif pilihan == '4':
        hapus_data()
    elif pilihan == '5':
        sewa_mobil()
    elif pilihan == '6':
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")