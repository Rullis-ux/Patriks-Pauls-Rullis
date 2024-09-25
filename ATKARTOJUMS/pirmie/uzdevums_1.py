#uz ekrāna izdrukāt visus nepāra skaitļu no  lietotāja ievadītajā dieapazonā
sakums = int(input("sakums:"))
beigas = int(input("beigas:"))

for skaitlis in range(sakums, beigas+1):
    if skaitlis%2 != 0:
        print(skaitlis)

