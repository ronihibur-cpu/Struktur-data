#bagian 1 :verivikasi nama
nama=input("masukan nama pendek anda :")

if nama =="Roni":
    print("Lanjut ke program selanjutnya")
else :
    print("Silahkan coba lagi !")
    

#bagian 2 : tabel perkalian 
angka =int(input("masukan angka :"))
for i in range(1,11):
    hasil=angka*i
    print(f"{angka}x{i}={hasil}")