#tukss sarakst, kur būs mašīnas
masinas = []
def pievienot_masinu(nosaukums,marka,gads):
    masinas.append({
        'nosaukums':nosaukums,
        'marka':marka,
        'gads':gads,
    })
    print(f"Mašīna '{nosaukums}' pievienot")
def paradit_masinas(): 
    if masinas:
        print("\nMašīnas sarakstā:")
    for masina in masinas:
        print(f"Nosaukums: {masina['nosaukums']},Marka: {masina['marka']},Gads: {masina['gads']}")   
    else :
        print("\nnoņemt no saraksta")
def atjaunot_masinu(nosaukums, jauna_marka, jauns_gads):
    for masina in masinas:
        if masina['nosaukums'] == nosaukums:
           masina['marka'] == jauna_marka
           masina['gads'] == jauns_gads 
           print(f"Mašīna '{nosaukums}'atjaunināt")
           return
        print(f"Mašīna'{nosaukums}' nav atrast sarakstā.")
def dzest_masinu(nosaukums):
    for masina in masinas:
        if masina['nosaukums'] == nosaukums:
            masinas.remove(masina)
            print(f"Mašīna '{nosaukums}'dzēst no saraksta.")
            return
        print(f"Mašīna'{nosaukums}' nav atrast sarakstā.")

while True:
    print("/nIzvēlies darbību:")
    print("1. Pievienot mašīnu")
    print("2. Parādīt visas mašīnas")
    print("3. Atjaunināt mašīnu")
    print("4. dzēst mašīnu")
    print("5. Iziet")

    izvele = input("Izvēlies daerbību(1-5):")
    if izvele == '1':
        nosaukums = input("Ievadiet mašīnas nosaukumu")
        marka = input("Ievadiet mašīnas marku")
        gads = int(input("Ievaiet mašīans gadu"))
        pievienot_masinu(nosaukums, marka, gads)

    elif izvele == '2':
        paradit_masinas()

    elif izvele == '3':
        nosaukums = input("Ievadiet nosaukumu, kuru vēlaties atjaunināt")
        jauna_marka = input ("Ievadiet jaunu marku:")
        jauns_gads = int(input("Jaunais gads:'"))
        atjaunot_masinu(nosaukums, jauna_marka, jauns_gads)

    elif izvele == '4':
        nosaukums = input("Ievadiet mašīnas nosaukumu, kuru vēlaties dzēst")
        dzest_masinu(nosaukums, marka, gads)