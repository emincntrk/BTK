#for s1 in range(1,100000):
#    s1 = int(input("Bir sayi giriniz"))
#   print(s1 * s1)
while True:
    try:
        s1 = int(input("Bir sayi giriniz"))
        break
    except ValueError:
        print("Sadece sayıları kabul etmekteyim!")
print("Karesi",s1**2)






