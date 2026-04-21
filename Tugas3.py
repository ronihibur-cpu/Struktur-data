angka = float(input("Masukkan angka positif : "))

# akan mengulang selama angka kurang dari 0 atau angka negatif 
while angka < 0:
    print("Masukkan angka positif, silahkan ulang !")
    angka = float(input("Masukkan angka positif : "))

#jika angka sudah di atas 0 atau angka positif 
print("Angka benar, terimakasih")
