#print("BTK"deneme) syntax error
#print(10/0) ZeroDivisionError:hatası verir
#int("5a")ValueError:hatası verir
try:
    sayi1=int(input("Bir sayı giriniz"))
    sayi2=int(input("Bir sayı giriniz"))
    print("Bölüm:",sayi1/sayi2)
except ValueError:
    print("Lütfen bir sayı gir! Harf girme!")
except ZeroDivisionError:
    print("0'a bölme yapılamaz")
except SyntaxError:
    print("Yazım hatan var!")
except NameError:
    print("Böyle bir değişken yok!")
except:
    print("Genel bir hata oluştu")
print("Program buradan çalışmaya devam eder")







