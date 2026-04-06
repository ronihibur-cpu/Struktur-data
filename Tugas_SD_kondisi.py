nama=input("MASUKKAN NAMA PENDEK ANDA :")
if nama == "Roni":
    print("selamat datang Roni")
else:
    print("program selesai")
    
umur=int(input("MASUKAN UMUR ANDA :"))
#kondisi
if umur <=0:
    print("Anda belum lahir")
elif umur>60:
    print("banyakin ibadah bentar lagi mati")
elif umur>=18:
    print("Anda cukup umur")
else:
    print("program selesai")