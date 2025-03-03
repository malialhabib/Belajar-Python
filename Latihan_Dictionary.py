import datetime
import os
import random
import string
# template dict mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':'0',
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}
while True:
    os.system("cls")

    print(f"{"Selamat Datang":^20}")
    print(f"{"DATA MAHASISWA":^20}")
    print(20*"=")

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    mahasiswa['nama'] = input("Nama Mahasiswa\t\t:")
    mahasiswa['nim'] = input("NIM Mahasiswa\t\t:")
    mahasiswa['sks'] = int(input("Jumlah SKS\t\t:"))

    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY)\t:"))
    BULAN_LAHIR = int(input("Bulan Lahir (MM)\t:"))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (DD)\t:"))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':^6} {'Nama':^25} {'NIM':^8} {'SKS':^4} {'Lahir':^9} ")
    print("="*60)
   
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        
        print(f"{KEY:<6} {NAMA:<18} {NIM:^8} {SKS:^3} {LAHIR:^10}")

    print("\n")
    is_done = input("Apakah ingin menambah data? (y/n)")
    if is_done == "n":
        break

print("Akhir dari program ini :)")