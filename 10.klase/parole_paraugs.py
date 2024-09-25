import sys

i=0
user='skolotaja'
password='12345'

def check_quit(inp): #lietoju šo funkciju kodā pēc katra ievada, lai pārbaudītu, vai lietotājs grib iziet no programmas
    if inp == 'stop':
        print('Programmas beigas!')
        sys.exit(0)

while i <= 5: #Cikls strādā kamēr mēģinājumu skaits nav pārsniedzis 5
    i+=1 #Pieskaita klāt mēģinājumu skaitam
    enteredUser=input('Lūdzu, ievadiet savu lietotājvārdu: ')
    check_quit(enteredUser)

    enteredPassword=input('Lūdzu, ievadiet savu paroli: ')
    check_quit(enteredPassword)

    if enteredUser==user and enteredPassword==password: #Tiek pārbaudīts, vai viss ievadīts pareizi
        print('Pieslēgšanās veiksmīga')
        #Sākas 2. solis
        num1=input('Ievadiet 1. veselo skaitli: ')
        check_quit(num1)
        num1=int(num1)

        num2=input('Ievadiet 2. veselo skaitli: ')
        check_quit(num2)
        num2=int(num2)

        if num1<0 or num2<0: #Pārbauda, lietotāja ievadītie dati nav negatīvi
            print('Nedrīkst būt negatīvs skaitlis!')
            break
        elif num1>=num2: #Pārbauda, vai pirmais skaitlis nav lielāks vai vienāds ar otru
            print(f'Veselu secīgi pieaugošu skaitļu no {num1} līdz {num2} summa ir 0.') #Tā kā pirmais skaitlis ir lielāks par otru, tur nav secīgi pieaugošu skaitļu to starpā
            break
        else: #Ja skaitļi nav negatīvi vai vienādi, programma turpinās
            res=num1
            count=num1
            while count<num2: #Cikls darbojas, kamēr skaitītājs nav pārsniedzis 2. skaitļa vērtību
                count+=1
                res+=count #Rezultātam pieskaita skaitītāja tā brīža vērtību
            print(f'Veselu secīgi pieaugošu skaitļu no {num1} līdz {num2} summa ir {res}.')
            break

    else:
        if len(enteredPassword)!=5: #Pārbauda, vai parole nav tikai 5 rakstzīmes gara
            print('Parole ir jābūt 5 rakstzīmes garai!')

        if i == 5: #Ja ir bijuši 5 mēģinājumi, programma apstājās
            print('Atļauts mēģināt 5 reizes!')
            break
        elif i == 4: #Pārbauda, vai ir 1 mēģinājums palicis (šis ir gramatikas dēļ)
            print('Ir atlicis vēl 1 mēģinājums!')
        else:
            print(f'Ir atlikuši vēl {5-i} mēģinājumi!') #Paziņo lietotājam, cik viņam ir palikuši mēģinājumi
            continue