liste=[]   #boş bir liste tanımlar
liste=["Elma","Armut",20]
sayilar=[14,13,78,90,5]
isimler=["Ayşe","Emre","Hasan","Ahmet","Ali"]
gunler=["Pazartesi","Salı","Çarşamba"]
print(gunler)
print("0. indeksdeki eleman",gunler[0])
print(gunler[1])
print(gunler[2])
gunler.append("Perşembe")
print(gunler)
print(len(gunler))
print("Eleman Sayısı:",len(gunler))
gunler.pop()
print(gunler)
gunler.pop(0)
print(gunler)
print(sayilar)
sayilar.sort()
print(sayilar)
sayilar.sort(reverse=True)
print(sayilar)
isimler.sort()
print(isimler)
isimler.sort(reverse=True)
print(isimler)