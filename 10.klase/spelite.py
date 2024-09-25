import random
gajieni = ['akmens','papirs','skeres']
while True:
    cilveka_gajiens = input("Ievadi savu gājienu: ")
    dators_gajiens = random.choice(gajieni)

    print('Cilvēks:',cilveka_gajiens, 'vs. Dators:' ,dators_gajiens)
    if cilveka_gajiens == dators_gajiens:
            print('Neizšķirts!')

    elif cilveka_gajiens == 'akmens' and dators_gajiens == 'skeres':
        print('Cilvēks uzvar!')

    elif cilveka_gajiens == 'papirs' and dators_gajiens == 'akmens':
        print('Cilvēks uzvar!')

    elif cilveka_gajiens == 'skeres' and dators_gajiens == 'papirs':
        print('Cilvēks uzvar!')   

    else:
        print('Dators uzvar!')