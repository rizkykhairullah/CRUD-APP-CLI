# Memakai file database.py sebagai jalan akses ke database
import database

# Variabel untuk mengendalikan database
cursor = database.db.cursor()

# Fungsi untuk melakukan sesuatu pada data di database
def create():
    print('Silahkan membuat data baru, perhatikan data yang ingin dimasukan...')
    # Membuat input data untuk dimasukan ke database
    nama = input('Masukan Nama Mahasiswa   : ')
    gmail = input('Masukan Gmail Mahasiswa  : ')
    nim = input('Masukan NIM Mahasiswa    : ')
    # Pembuatan kerangka perintah sql ke database
    sql = 'INSERT INTO mahasiswa (nama, gmail, nim) VALUES (%s, %s, %s)'
    val = (nama, gmail, nim)
    cursor.execute(sql, val)
    # Melakukan komit/simpan data ke database
    database.db.commit()
    print('\n')

def update(id):
    # Pembuatan kerangka perintah sql ke database
    sql = "SELECT * FROM mahasiswa"
    cursor.execute(sql)
    # Menampilkan semua data di database
    results = cursor.fetchall()
    for data in results:
        if str(data[0]) == str(id):
            print(f'\nData mahasiswa yang lama : {data[0]}. {data[1]} - {data[2]} - {data[3]}')
        else:
            pass
    print('Silahkan memperbarui data, perhatikan pilihan dan data yang ingin dimasukan...')
    print('1. Perbarui Nama')
    print('2. Perbarui Gmail')
    print('3. Perbarui NIM')
    print('4. Perbarui Nama & Gmail')
    print('5. Perbarui Nama & NIM')
    print('6. Perbarui Gmail & NIM')
    print('7. Perbarui semua data')
    choice = input('Masukan pilihan berupa angka : ')
    if choice == '1':
        nama = input('Masukan data nama yang baru : ')
        sql = 'UPDATE mahasiswa SET nama=%s WHERE id=%s'
        val = (nama, id)
        # Pembuatan kerangka perintah sql ke database
        cursor.execute(sql, val)
        # Melakukan komit/simpan data ke database
        database.db.commit()
        print('\n')

    elif choice == '2':
        gmail = input('Masukan data gmail yang baru : ')
        sql = 'UPDATE mahasiswa SET gmail=%s WHERE id=%s'
        val = (gmail, id)
        # Pembuatan kerangka perintah sql ke database
        cursor.execute(sql, val)
        # Melakukan komit/simpan data ke database
        database.db.commit()
        print('\n')

    elif choice == '3':
        nim = input('Masukan data NIM yang baru : ')
        sql = 'UPDATE mahasiswa SET nim=%s WHERE id=%s'
        val = (nim, id)
        # Pembuatan kerangka perintah sql ke database
        cursor.execute(sql, val)
        # Melakukan komit/simpan data ke database
        database.db.commit()
        print('\n')

    elif choice == '4':
        nama = input('Masukan data nama yang baru : ')
        gmail = input('Masukan data gmail yang baru : ')
        sql = 'UPDATE mahasiswa SET nama=%s, gmail=%s WHERE id=%s'
        val = (nama, gmail, id)
        # Pembuatan kerangka perintah sql ke database
        cursor.execute(sql, val)
        # Melakukan komit/simpan data ke database
        database.db.commit()
        print('\n')

    elif choice == '5':
        nama = input('Masukan data nama yang baru : ')
        nim = input('Masukan data NIM yang baru : ')
        sql = 'UPDATE mahasiswa SET nama=%s, nim=%s WHERE id=%s'
        val = (nama, nim, id)
        # Pembuatan kerangka perintah sql ke database
        cursor.execute(sql, val)
        # Melakukan komit/simpan data ke database
        database.db.commit()
        print('\n')

    elif choice == '6':
        gmail = input('Masukan data gmail yang baru : ')
        nim = input('Masukan data NIM yang baru : ')
        sql = 'UPDATE mahasiswa SET gmail=%s, nim=%s WHERE id=%s'
        val = (gmail, nim, id)
        # Pembuatan kerangka perintah sql ke database
        cursor.execute(sql, val)
        # Melakukan komit/simpan data ke database
        database.db.commit()
        print('\n')

    elif choice == '7':
        nama = input('Masukan data nama yang baru : ')
        gmail = input('Masukan data gmail yang baru : ')
        nim = input('Masukan data NIM yang baru : ')
        sql = 'UPDATE mahasiswa SET nama=%s, gmail=%s, nim=%s WHERE id=%s'
        val = (nama, gmail, nim, id)
        # Pembuatan kerangka perintah sql ke database
        cursor.execute(sql, val)
        # Melakukan komit/simpan data ke database
        database.db.commit()
        print('\n')

    else:
        print('Data tidak ditemukan atau pilihan yang anda masukan salah...')

def delete(id):
    # Pembuatan kerangka perintah sql ke database
    sql = "DELETE FROM mahasiswa WHERE id=%s"
    val = (id, )
    cursor.execute(sql, val)
    # Melakukan komit/simpan data ke database
    database.db.commit()
    print('\n')

def show():
    print('-----------------------------------------------------')
    print('id. Nama Mahasiswa - Gmail - NIM')
    print('-----------------------------------------------------')
    # Pembuatan kerangka perintah sql ke database
    sql = "SELECT * FROM mahasiswa"
    cursor.execute(sql)
    # Menampilkan semua data di database
    results = cursor.fetchall()
    for data in results:
        print(f'{data[0]}. {data[1]} - {data[2]} - {data[3]}')
    print('\n')