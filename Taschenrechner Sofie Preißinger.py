
def Willkommen():
    print('''
Willkommen! Viel Spaß beim rechnen.
-Sofie Preißinger
''')
def berechnen():
    calc = input('''
Bitte geben Sie die mathemathische Operation ein, die Sie ausführen möchten
''')
    if calc == ','
        print("','")
    print("Ergebnis: " + str(eval(calc)))
    nochmal()

def nochmal():

    calc_again = input('''
Wollen Sie nochmal etwas berechnen ?
Bitte geben Sie bitte "Ja" oder "Nein" ein.
''')

    if calc_again == 'Ja':
        berechnen()

    elif calc_again == 'Nein':
        print ('Berechnung beendet.')

    else:
        nochmal()

Willkommen()
berechnen()

