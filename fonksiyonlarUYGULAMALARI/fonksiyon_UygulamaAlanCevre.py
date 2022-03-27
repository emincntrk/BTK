#dikdörtgenin alanını vs cevresini hesaplayan 2 ayrı
#fonksiyon yazınız .Kullanıcıdan aldıgınız degere  göre
#alanı ve cevreyi ekrana yazdırınız
def cevre(a,b):
    return (a+b)*2
kisakenar=int(input("Kısa kenarı giriniz:"))
uzunkenar=int(input("Uzun kenarını giriniz:"))
print("Dikdörtgenin çevresi:",cevre(kisakenar,uzunkenar))
def alan(a,b):
    return a*b
print("Dikdörtgenin alanı:",alan(kisakenar,uzunkenar))