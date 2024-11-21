print('=== ganjil dan genap ===')
# bilangan ganjil & genap
angka = int(input("masukkan bilangan angka"))
ganjil = "bilangan ganjil"
genap = "bilangan genap"

if angka % 2 == 0:
  print(genap)
elif angka % 2 != 0:
  print(ganjil)
else:
  print("input tidak valid ")


print('=== raport ===')
# input nilai rapot
angka = int(input("Masukkan nilai raport "))
if angka >= 75:
    print("Lulus")
else :
    print ("Tidak Lulus")


print('=== Usia ===')
# input usia
usia = int(input("Masukkan usia "))
if usia >= 18:
  print ("Dewasa")
elif usia <= 18 or usia >= 13:
  print ("remaja")
else:
  print ("anak-anak")


print('=== Status anggota ===')
# input status anggota
member = input ("Masukkan status keanggotaan ")

if member == "gold" or member == "silver":
  print ("Selamat anda mendapatkan diskon")
elif member == "GOLD" or member == "SILVER":
  print ("Selamat anda mendapatkan diskon")
else :
  print ("Mohon maaf anda tidak mendapatkan diskon")


print('=== Total belanja ===')
# input belanjaan
jumlahpembelian= int(input("Masukkan total belanja: "))
hargaitem = 1000
hargadiskon = hargaitem * jumlahpembelian *(10/100)
hargatotal = hargaitem * jumlahpembelian
totaldengandiskon = hargatotal - hargadiskon

if jumlahpembelian > 100:
    print(f"Anda mendapat diskon 10%, harga per item {hargaitem} jadi total yang harus dibayar {totaldengandiskon}")
else:
    print(f"Harga per item {hargaitem}, jadi total yang  harus dibayar adalah {hargatotal}")