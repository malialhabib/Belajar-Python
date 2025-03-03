'''Latihan Fungsi'''

import os

def header():
    '''fungsi header'''
    os.system("cls")
    print(f"{"PROGRAM MENGHITUNG LUAS":^40}")
    print(f"{"DAN KELILING PERSEGI PANJANG":^40}")
    print(f"{40*'='}")

def input_user():
    '''fungsi input user'''
    #mengambil input user
    lebar = int(input("Masukkan nilai lebar : ")) 
    panjang = int(input("Masukkan nilai panjang : "))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''fungsi hitung luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling luas'''
    return 2*(lebar+panjang)

def display(message,value):
    print(f"Hasil perhitungan {message} = {value}")

#Program utamanya
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = LEBAR * PANJANG
    KELILING = 2 * (LEBAR + PANJANG)
    opsi = input("pilih 1 untuk luas dan 2 untuk keliling :")
    if opsi == "1":
       display("luas", LUAS) 
    
    elif opsi == "2":
        display("keliling", KELILING)
    else:
        print("Kan 1 atau 2 bro!!!!!")

    isContinue = input("Apakah lanjut? (y/n)")
    if isContinue == "n":
        break
