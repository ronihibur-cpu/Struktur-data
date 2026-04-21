# Menggunakan huruf kecil untuk float dan nama variabel yang konsisten
angka = float(input("masukkan angka positif : "))

# Loop akan terus berjalan selama angka kurang dari 0
while angka < 0:
    print("masukkan angka positif, silahkan ulang !")
    angka = float(input("masukkan angka positif : "))

# Bagian ini hanya akan dijalankan jika angka >= 0
print("angka benar, terimakasih")
