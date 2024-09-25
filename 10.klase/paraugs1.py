atbilde = input('Vai šodien ir Tava dzimšanas diena?(j/n)')
if atbilde == 'j':#salīdzināšana veicama ar 2 vienādības zīmēm
    print('Daudz baltu dieniņu!')

tests = input('Vai šodien ir Jaungada diena?(j/n)')
if tests == 'j':
    print('Laiks salūtam!')
else: #pie else nosacījuma nebūs(tas ir tas,kas paliek pāri)
    print('Bēdīgi..') #šis tiek palaists tikai tad, 
    #ja lietotājs neieraksta 'j'