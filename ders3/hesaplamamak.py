

print("""
     1- Toplama
     2 - Çıkarma
     3 - Bölme
     4 - Çarpma""")
secenek = input("Lütfen Bir Seçim Yapınız:")
if secenek == "1" :
    sayı1 = int(input("1.Sayıyı Giriniz:"))
    sayı2 = int(input("2.Sayıyı Giriniz:"))
     print("Sayılarınızın Toplamı:", sayı1+sayı2)

 elif secenek == "2" :
sayı1 = int(input("1.Sayıyı Giriniz:"))
sayı2 = int(input("2.Sayıyı Giriniz:"))
sayı2 = int(input("2.Sayıyı Giriniz:"))
     print("Sayılarınızın Farkı:", sayı1 - sayı2)

    elif secenek == "3" :
sayı1 = int(input("1.Sayıyı Giriniz:"))
sayı2 = int(input("2.Sayıyı Giriniz:"))
      print("Sayılarınızın Bölümü:", sayı1 / sayı2)
elif secenek == "4" :
     sayı1 = int(input("1.Sayıyı Giriniz:"))
     sayı2 = int(input("2.Sayıyı Giriniz:"))
     print("Sayılarınızın Çarpımı:", sayı1 * sayı2)
else:
    print("Lütfen 1-4 arası bir seçim yapınız")