import random
while True:
    seviye=input("Seviye Seçiniz:Kolay/Orta/Zor")
    if seviye=="Kolay":
        uret=random.randint(1,10)
        break
    elif seviye=="Orta":
        uret = random.randint(1, 50)
        break
    elif seviye=="Zor":
        uret = random.randint(1, 100)
        
    while True:
        tahmin=int(input("Bir Tahminde Bulunun"))

        if tahmin<uret:
            print("Sayıyı büyültün")

        elif tahmin>uret:
            print("Sayıyı küçültün")
        else:
            print("Tebrikler Bildiniz")
            break
