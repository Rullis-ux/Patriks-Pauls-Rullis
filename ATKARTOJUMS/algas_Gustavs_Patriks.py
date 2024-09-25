algas = []

def aprekinat_videjo(skaitli):
    return sum(skaitli) / len(skaitli)


while True:
    try: 
        skaits = int(input("Cik algas vēlaties ievadīt [>0]: "))
        break
    except ValueError:
        print("Lūdzu ievadiet skaitli, kas lielāks par 0.")


for n in range(1, skaits+1):
    while True:
        try:
            alga = float(input(f'Ievadiet {n}. algu: '))
            if alga > 0:
                algas.append(alga)
                break
            else:
                raise ValueError
        except ValueError:
            print("Lūdzu ievadiet skaitli, kas lielāks par 0.")

videja_alga = aprekinat_videjo(algas)
print(f'Vidējā alga: {round(videja_alga, 2)}€')