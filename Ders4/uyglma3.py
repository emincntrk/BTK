import os
sec=input("Sil/Ekle")
for i in range(1, 10):
    if sec == "Sil":
        os.rmdir("elma" + str(i))
    elif sec == "Ekle":
        os.mkdir("elma" + str(i))
