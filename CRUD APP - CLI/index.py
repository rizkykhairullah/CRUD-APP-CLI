# Memakai file crud.py sebagai fungsi perintah
import crud

# Membuat perintah untuk tampilan index/interface awal
def index():
    print('-----------------------------------------------------')
    print('     Selamat datang diaplikasi CRUD berbasis CLI     ')
    print('-----------------------------------------------------')
    print('1. Tampilkan data mahasiswa')
    print('2. Buat data mahasiswa')
    print('3. Perbarui data mahasiswa')
    print('4. Hapus data mahasiswa')
    print('5. Berhentikan program')

    # Membuat percabangan untuk program yang dipilih
    choice = input('Masukan pilihan dengan angka : ')
    if choice == '1':
        # Mamanggil fungsi show pada file crud.py
        crud.show()
        # Memberikan waktu untuk user melihat datanya, sampai enter ditekan
        blank = input('\nTekan enter untuk lanjut...')
        # Mengembalikan interface ke fungsi index awal
        index()

    elif choice == '2':
        crud.create()
        blank = input('\nTekan enter untuk lanjut...')
        index()

    elif choice == '3':
        id = input('Masukan id mahasiswa : ')
        crud.update(id)
        blank = input('\nTekan enter untuk lanjut...')
        index()

    elif choice == '4':
        id = input('Masukan id mahasiswa : ')
        crud.delete(id)
        blank = input('\nTekan enter untuk lanjut...')
        index()

    else:
        print('Program dihentikan...')

# Memanggil fungsi index
index()