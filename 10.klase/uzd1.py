#izveidot funkciju ar nosaukumu myFunction, kurai nav parametru
#šī f-ja pie izsaukšanas izdrukā Hello World

#izsaukt funkciju tad, ja lietotāja ievadītie veselie skaitļi(a un b)ir vienādi
#pretējā gadījumā parādīt uz ekrāna tekstu 'Nesanāca 😶'

def myFunction():
    print('Hello, World!')

a = int(input("1:"))
b = int(input("2:"))

if a == b: 
    myFunction()
else:
    print('Nesanāca 😶')

def info(vards, vecums, darbs):
    print("Vārds: ",vards)
    print("Vecums: ",vecums)
    print("Amats: ",darbs)
    return

info(vards='Jānis',vecums='35',darbs='pavārs')

#uzrakstīt programmā f-ju, kas saskaita visus skaitļus sarakstā
list = [1,2,7,9,5,7]
def summa():
    print(sum(list))
summa()


