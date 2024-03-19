#CAPSTONE WICAKSONO HOSPITAL ROOM MANAGER v.1
from tabulate import tabulate

listPasien = [
{   'Nomor Rekam Medis' : '000001',
    'Nama' : "Bayu Wicaksono",
    'Ruangan' : 'Mawar',
    'Kota' : 'Jakarta',
    'Umur' : 20,
    'Status' : 'Kritis'
},

{   'Nomor Rekam Medis' : '000002',
    'Nama' : "Shaq O'Neal",
    'Ruangan' : 'Angrek',
    'Kota' : 'Bekasi',
    'Umur' : 30,
    'Status' : 'Koma'
},

{   'Nomor Rekam Medis' : '000003',
    'Nama' : "Della Az-Zahra",
    'Ruangan' : 'Melati',
    'Kota' : 'Depok',
    'Umur' : 40,
    'Status' : 'Siuman'
}
]

pasienPulang = []

def menu_utama():   
    while True: #berguna untuk melooping menu_utama dengan menggunakan input angka untuk menjalankan fungsi conditional statement
        pilihanmenu = input('''
            Selamat Datang WICAKSONO HOSPITAL ROOM MANAGER

            List Menu :
            1. Melihat Daftar Pasien
            2. Tambah Pasien Rawat Inap
            3. Edit Data Pasien
            4. Hapus Pasien Rawat Inap (Pasien Pulang)
            5. Arsip Pasien
            6. Exit

            Masukkan angka Menu yang ingin dijalankan : ''')
        if(pilihanmenu == '1'):
            ReadDaftarPasien()
        elif(pilihanmenu == '2'):
            CreateNewPasien()
        elif(pilihanmenu == '3'):
            UpdatePasien()
        elif(pilihanmenu == '4'):
            DeletePasien()
        elif(pilihanmenu == '5'):
            cekHistoryPasien()
        elif(pilihanmenu == '6'):
            print('\n *** EXIT WICAKSONO HOSPITAL ROOM MANAGER *** \n')
            break
        else:
            print('\n *** Input Invalid. Pilih 1 - 6 ***')
            print('__________________________________')

def ReadDaftarPasien(): 
    while True: 
        print('''
                1. Melihat Daftar Seluruh Pasien
                2. Cari Pasien berdasarkan Nomor Rekam Medis
                3. Kembali ke Menu Utama
                ''')
        a = input("Masukkan 1 - 3: ")
        if(a == '1'):
            print_PasienTabulate(listPasien)
        elif(a == '2'):
            printPasien_byID(listPasien)
        elif(a == '3'):
            break
        else:
            print('\n*** Input Invalid. Pilih 1 - 3 ***')
            print('__________________________________')


def print_PasienTabulate(listPasien):
    if not listPasien:
        print("\n *** Data Pasien Kosong ***")
    else:
        headers = listPasien[0].keys()
        data = [[pasien[field] for field in headers] for pasien in listPasien]
        print(tabulate(data, headers=headers, tablefmt='grid'))


def printPasien_byID(listPasien):
    nomor_rekam_medis = input("Masukkan Nomor Rekam Medis pasien yang ingin ditampilkan: ")
    for pasien in listPasien:
        if pasien['Nomor Rekam Medis'] == nomor_rekam_medis:
            print("Detail Pasien dengan Nomor Rekam Medis", nomor_rekam_medis)
            print_PasienTabulate([pasien])
            return
    print("\n ***Nomor Rekam Medis tidak Ditemukan ***")


def CreateNewPasien():
    print_PasienTabulate(listPasien)
    while True:#berguna untuk menjalankan looping dari CreateNewPasien dengan menggunakan input angka untuk menjalankan fungsi conditional statement
        print('''
                1. Tambah Pasien Rawat Inap
                2. Kembali ke Menu Utama
                ''')
        a = input("Masukan angka 1 atau 2: ")
        if(a == '1'):
            tambah_NoRekMed = InputNoRekMed ()
            index = CariPasien(tambah_NoRekMed)
            if index != -1:
                print('\n*** Pasien Sudah Terdaftar ***')
                print('______________________________')
                continue
            tambah_Nama = InputNama()
            tambah_Ruangan = InputRuangan() 
            tambah_Kota = InputKota() 
            tambah_Umur = InputUmur()
            tambah_Status = InputStatus()
            temporary_table = {
                    'Nomor Rekam Medis' : tambah_NoRekMed,
                    'Nama' : tambah_Nama,
                    'Ruangan' :tambah_Ruangan,
                    'Kota' : tambah_Kota,
                    'Umur' : tambah_Umur,
                    'Status' : tambah_Status}
            res = konfirmasi(temporary_table,'input','tambah')
            if  res :
                break
        elif(a == '2'):
            break
        else:
            print('\n*** Input Invalid. Pilih 1 - 2 ***')
            print('__________________________________')


def CariPasien(pasienLama): #bertujuan untuk mencari indeks(key) dari tiap pasien dalam listpasien berdasarkan Nomor Rekam Medis. 
    for i in range(len(listPasien)):
        if listPasien[i]['Nomor Rekam Medis'] == pasienLama:
            return i
    return -1


def InputNoRekMed():
    while True:
        try:
            NoRekMed = input("Masukkan 6 Digit Angka Nomor Rekam Medis Baru: ")
            if not NoRekMed.isdigit():
                raise ValueError("Input harus berupa 6 digit angka ***")
            number = int(NoRekMed)
            if len(NoRekMed) != 6:
                raise ValueError("Input harus berupa 6 digit angka ***")
            if number == 0:
                raise ValueError("Input tidak bisa 000000 ***")
            return NoRekMed 
        except ValueError as error:
            print(" *** Input Invalid:", error)
     

def InputNama():
    NamaPasien = input("Masukkan Nama Pasien: ").strip().capitalize()
    if not NamaPasien or any(char.isdigit() for char in NamaPasien) or not any(char.isalnum() for char in NamaPasien) or len(NamaPasien) > 25:
        print(" *** Input Invalid. Masukkan Nama Pasien (maksimal 25 karakter) tanpa angka *** ")
        return InputNama() 
    else:
        return NamaPasien

def InputUmur():
    while True:
        try:
            UmurPasien = input("Masukkan Umur: ")
            if not UmurPasien.isdigit():
                raise ValueError("Umur harus berupa angka ***")
            UmurPasien = int(UmurPasien)
            if UmurPasien < 1 or UmurPasien > 120:
                raise ValueError("Umur Pasien harus diantara 1 dan 120 tahun ***")
            return UmurPasien
        except ValueError as error2:
            print(" *** Input Invalid:", error2)

def InputRuangan():
    NamaRuangan = input("Masukkan Nama Ruangan: ").capitalize()
    if not NamaRuangan or NamaRuangan.isdigit() or len(NamaRuangan) > 10: 
        print(" *** Input Invalid. Masukkan Nama Ruangan (maksimal 10 karakter) ***")
        return InputRuangan() 
    else:
        return NamaRuangan

def InputKota():
    NamaKota = input("Masukkan Kota Pasien: ").capitalize()
    if not NamaKota or NamaKota.isdigit() or len(NamaKota) > 10: 
        print(" *** Input Invalid. Masukkan Kota Pasien (maksimal 10 karakter) ***")
        return InputKota() 
    else:
        return NamaKota

def InputStatus():
    NamaStatus = input("Masukkan Status Pasien: ").capitalize()
    if not NamaStatus or NamaStatus.isdigit() or len(NamaStatus) > 10: 
        print(" *** Input Invalid. Masukkan Status Pasien ***")
        return InputStatus() 
    else:
        return NamaStatus
 

def UpdatePasien():
    while True: 
        print('''
                1. Edit data Pasien Rawat Inap
                2. Kembali ke Menu Utama
                ''')
        a = input("Masukkan 1 - 2: ")
        if(a == '1'):
            editDataPasien()
        elif(a == '2'):
            break
        else:
            print('\n*** Input Invalid. Pilih 1 - 2 ***')
            print('__________________________________')

 
def editDataPasien():
    while True:
        PasienLama = str(input('Masukkan Nomor Rekam Medis Pasien: '))
        index = CariPasien(PasienLama)
        if index == -1:
            print("\n *** Nomor Rekam Medis Tidak Ditemukan ***")
            print(" ___________________________________")
            break
        print_PasienTabulate([listPasien[index]])
        print('''
                1. Edit Nama
                2. Edit Ruangan
                3. Edit Kota
                4. Edit Umur
                5. Edit Status
                6. Batal
                ''')
        a = input("Pilih 1 - 6: ")
        pilihan = {
            '1': 'Nama',
            '2': 'Ruangan',
            '3': 'Kota',
            '4': 'Umur',
            '5': 'Status'
        }
        if a == '6':
            return
        elif a in pilihan.keys():
            ubahke = input(f"Ubah {pilihan[a]} Menjadi: ").capitalize()
            temp = {
                'index': index,
                'data': listPasien[index].copy()
            }
            temp['data'][pilihan[a]] = ubahke
            res = konfirmasi(temp, 'update', 'perbarui')
            if res:  # Jika data berhasil diupdate, kembali ke menu UpdatePasien
                break
        else:
            print("\n*** Input Invalid. Pilih 1 - 6 ***")
            print("________________________________")


def konfirmasi(data,aksi,pesan):
    checker = input(f"Konfirmasi {pesan} (Y/N) = ").upper()
    
    if(checker == 'N'):
        print(f"\n*** Data Batal di {pesan} ***")
        print("_____________________________")
        return 0
    elif(aksi == 'input' and checker == 'Y'):
        print("\n*** Data Berhasil Tersimpan ***")
        print("______________________")
        listPasien.append(data)
        return 1
    elif aksi == 'update' and checker == 'Y':
        print("\n *** Data Pasien Terupdate ***")
        print("_____________________________")
        listPasien.pop(data['index']) #menghapus data array (satu index key pasien)
        listPasien.insert(data['index'],data['data'])
        return 1
    else:
        print('\n *** Input Invalid. Pilih Y/N ***')
        print('________________________________')
    konfirmasi(data,aksi,pesan)


def DeletePasien():
    while True:
        print_PasienTabulate(listPasien)
        print('''
                1. Hapus Pasien Inap
                2. Kembali ke Menu Utama
                ''')
        a = input("Masukan angka 1 atau 2: ")
        if(a == '1'):
            tambah_NoRekMed = input('Masukkan Nomor Rekam Medis Pasien : ').upper()
            index = CariPasien(tambah_NoRekMed)
            if index == -1:
                print('\n*** Nomor Rekam Medis Invalid ***')
                print('_________________________________')
                continue
        
            while True:  
                checker = str(input("Konfirmasi Hapus (Y/N) : ")).upper()
                if(checker == 'Y'):
                    print("\n*** Data Pasien telah terhapus ***")
                    print("__________________________________")
                    pasienPulang.append(listPasien.pop(index))
                    break
                elif(checker == 'N'):
                    print("\n*** Batal hapus ***")
                    print("___________________")
                    break
                else:
                    print("\n*** Input Invalid. Pilih Y/N ***")
                    print("________________________________")
        elif('2' == a):
            break
        else:
            print("\n *** Input Invalid. Pilih 1 - 2 ***")
            print("__________________________________")


def cekHistoryPasien():
    print('''
        Pasien yang telah pulang dan Sehat
       ''')
    archivePasien = pasienPulang
    for i in range(len(archivePasien)):
        archivePasien[-1*i]['Status'] = 'Pulang'
    printarchivePasien(archivePasien)

def printarchivePasien(data2):
    print("Daftar Pasien Pulang\n")
    print_PasienTabulate(data2)

menu_utama()