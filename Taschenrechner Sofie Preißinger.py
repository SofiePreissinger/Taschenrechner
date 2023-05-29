
def Willkommen():
    print('''
Willkommen! Viel Spaß beim rechnen.
-Sofie Preißinger
''')
def berechnen():
    calc = input('''
Bitte geben Sie die mathemathische Berechnung ein, die Sie ausführen möchten
''')
    
    print("Ergebnis: " + str(eval(calc)))
    nochmal()

def nochmal():

    calc_again = input('''
Wollen Sie nochmal etwas berechnen ?
Bitte geben Sie "Ja" oder "Nein" ein.
''')

    if calc_again == 'Ja':
        berechnen()

    elif calc_again == 'Nein':
        print ('Berechnung beendet.')

    else:
        nochmal()

Willkommen()
berechnen()

