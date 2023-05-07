
def Wilkommen():
    print('''
Wilkommen! Viel spaß beim rechnen.
-Sofie Preißinger
''')
def berechnen():
    operator = input('''
Bitte geben Sie die mathemathische Operation ein, die Sie ausführen möchten)
+ für addieren
- für subtrahieren 
* für multiplizieren 
/ für dividieren 
''')

    num1 = float(input("Geben Sie die erste Nummer ein:"))
    num2 = float(input("Geben Sie die zweite Nummer ein:"))

    if operator == "+":
        result = num1 + num2
        print(round(result, 3))
    elif operator == "-":
        result = num1 - num2
        print(round(result, 3))
    elif operator == "*":
        result = num1 * num2
        print(round(result, 3))
    elif operator == "/":
        result = num1 / num2
        print(round(result, 3))
    else:
        print(f"{operator} ist keine gültige Eingabe, bitte versuchen Sie es erneut")
    nochmal()
def nochmal():

    calc_again = input('''
Wollen Sie nochmal etwas berechnen ?
Bitte geben Sie Ja oder Nein ein.
''')

    if calc_again == 'Ja':
        berechnen()

    elif calc_again == 'Nein':
        print ('Berechnung beendet.')

    else:
        nochmal()
Wilkommen()
berechnen()

