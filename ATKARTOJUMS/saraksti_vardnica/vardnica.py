#pievienot skaitlus saraksat
def pievienot_skaitli():
    skaitli=[] #tukss saraksts
    while True:
        try:
            skaitlis=int(input("Ievadiet skailti(0, Lai partrauktu darbu)"))
            if skaitlis==0:
               break
            skaitli.append(skaitlis)
        except ValueError:
            print ("Ievadiet skaitli.")
    print ("Saraksts:", skaitli)

pievienot_skaitli()
