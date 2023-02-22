# Spørger Mark om det er ham
input('Mark is that you? ')
print('Det var heldigt, blev lidt bange der 😳')


# Inspo fra Mark https://github.com/Robotto/endnuNyereProjekt/commit/e5dc120b1a4f207f738877fe84dac601e079ecb0 B-)

# Definerer math funktionen
def math():
    # Beder om et tal
    try:
        etTal = int(input('Skriv dit yndlingstal: '))

        # Tallet må ikke være 0
        if etTal == 0:
            print('Du må ikke skrive 0, Mark ! Det ved du, da godt.')
            return math()

    # Error hvis der ikke skrives et gyldigt tal
    except ValueError:
        print('What det virkede ikke, dårlig stil Mark')
        print('CRINGE ONG 💀')
        return math()

    # Spørger om endnu et tal
    try:
        etAndetTal = int(input('Et til: '))

        # Tallet må ikke være 0
        if etTal == 0:
            print('Du må ikke skrive 0')
            return math()

    # Error hvis der ikke skrives et gyldigt tal
    except ValueError:
        print('What det virkede ikke, dårlig stil Mark')
        print('CRINGE ONG 💀')
        return math()

    # Definerer de forskellige math outputs
    summenAfTallene = etTal + etAndetTal
    differensenAfTallene = etTal - etAndetTal
    produktetAfTallene = etTal * etAndetTal
    kvotientenAfTallene = etTal / etAndetTal

    # Printer math outputs
    print('Summen af tallene er: ', summenAfTallene, '')
    print('Differensen af tallene er: ', differensenAfTallene, '')
    print('Produktet af tallene er: ', produktetAfTallene, '')
    print('Kvotienten af tallene er: ', kvotientenAfTallene, '')

# Kalder math funktionen
math()