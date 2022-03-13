#kullanıcı adını ve parolasını sorsun,admin ve parolaya 123456 yazılınca  hoşgeldin desin. Admin yazılmadığı sürece tekrar kullanıcı adı istesin(sürekli)
kullanici = ""
sifre = int
while kullanici != "admin" or sifre != 123456:
    kullanici = input(("Kullanıcı Adıniz:")).lower()
    sifre = int(input("Şifreniz"))
    if kullanici == "admin" and sifre == 123456:
        print("Hoşgeldiniz")
    else:
        print("Kullanıcı adı veya parolanız hatalı")
print("Sisteme giriş yapıldı")