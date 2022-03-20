import os
try:
    os.mkdir("elma")
except FileExistsError:
    print("aga bu isimde dosya var zaten!")