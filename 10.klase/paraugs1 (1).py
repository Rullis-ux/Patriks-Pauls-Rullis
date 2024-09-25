'''def atnemsana():  #funkcijai netiek nodoti parametri
    print(34-4)

print('Sveika, ziema!')
atnemsana() #funkcija atnemsana() pie izsaukšanas izvada rezultātu 30
'''

#funkcijai 'plus' tiek padoti 2 parametri
#konsolē jāparāda summa
#funkciju izsauc, norādot šīs 2 vērtības(argumenti)

def plus(num1, num2):
    print(num1+num2)
plus(4,5)

#nodefinēta f-ja reizinat(), iedodot parametru num1
def reizinat(num1):
    return num1*8
rez = reizinat(8)
print(rez)
#izsauc f-ju, nodot skaitli 8 kā argumentu num1 un 
#f-jas izsaukumu piešķir mainīgajam rez