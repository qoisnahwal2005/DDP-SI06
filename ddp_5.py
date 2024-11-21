#Menghitung luas bangun datar

pilihan = int(input("Masukkan pilihan Anda : "))

match pilihan:
  case 1:
    sisi = int(input("Masukkan sisi persegi: "))
    luas = sisi * sisi
    print("Luas persegi: yang sisinya",sisi,"adalah",luas)
  case 2:
    jari_jari = int(input("Masukkan jari-jari lingkaran: "))
    luas = 3.14 * jari_jari * jari_jari
    print("Luas lingkaran:", luas)
  case 3:
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = 0.5 * alas * tinggi
    print("Luas segitiga:", luas)
  case _:
    print("Salah pilih")

print('== kendaraan ==)
spek_kendaraan = [ "bermotor", "kecil", 150, "biru", "roda dua", "Rp. 33.000", "motor"]

index_kecil = spek_kendaraan.index("kecil")

spek_kendaraan.insert(index_kecil, "suzuki")
print(spek_kendaraan)