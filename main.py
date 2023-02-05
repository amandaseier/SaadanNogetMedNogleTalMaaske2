# Definerer tre globale variabler
global etTal
global etAndetTal
global math


# Spørger Mark om det er ham
input('Mark is that you? ')
print('Det var heldigt, blev lidt bange der 😳')


# Definerer en funktion som beder om at få et tal
def givMigEtTal():
    # Beder om et tal
    try:
        global etTal
        etTal = int(input('Skriv dit yndlingstal: '))

        # Tallet kan ikek være lig med 0
        if etTal == 0:
            print('Du må ikke skrive 0')

        # Lykkedes det så bliver næset funktion kaldt
        else:
            givMigEtTalTo()

    # Error hvis der ikke skrives et tal
    except ValueError:
        print('What det virkede ikke, dårlig stil Mark')
        print('CRINGE ONG 💀')
        givMigEtTal()


# Definerer en funktion som beder om at få endnu et tal
def givMigEtTalTo():
    # Spørger om endnu et tal
    try:
        global etAndetTal
        etAndetTal = int(input('Et til: '))

        # Tallet må ikke være 0
        if etTal == 0:
            print('Du må ikke skrive 0')

        # Lykkedes det bliver math funktionen kaldt
        else:
            math()

    # Error hvis der ikke skrives et tal
    except ValueError:
        print('What det virkede ikke, dårlig stil Mark')
        print('CRINGE ONG 💀')
        givMigEtTalTo()


# Definerer math funktionen
def math():
    # Definerer de forskellige math features
    summenAfTallene = etTal + etAndetTal
    differensenAfTallene = etTal - etAndetTal
    produktetAfTallene = etTal * etAndetTal
    kvotientenAfTallene = etTal / etAndetTal

    # Printer math features'ne
    print('Summen af tallene er: ', summenAfTallene, '')
    print('Differensen af tallene er: ', differensenAfTallene, '')
    print('Produktet af tallene er: ', produktetAfTallene, '')
    print('Kvotienten af tallene er: ', kvotientenAfTallene, '')

givMigEtTal()