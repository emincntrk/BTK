#kendisine gönderilen kullanıcı adı ve şifreyi kontrol ederek sonucunda True ya da False gönderen
#fonksiyonun python kodu kullanıcıadı: admin , şifre:=123456 olmalı
def kontrol(kullanici,sifre):
    if kullanici=="admin" and sifre=="123456":
        return  "Dogru Girdiniz"
    else:
        return  "Yanlış Girdiniz"
kullanici=input("Kullanıcı Adınız:")
sifre=input("Şifreniz:")
sonuc=kontrol(kullanici,sifre)
print(sonuc)