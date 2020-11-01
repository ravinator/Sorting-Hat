import textwrap


# Leest het txt document
def vragen_ophalen(vragen):
    with open(vragen)as lees:
        text = lees.read()
    return(text)


# Krijgt een antwoord binnen met een vraagnummer en geeft het correcte reeks punten terug
def puntensysteem(antwoord, vraagnummer):
    systeem = {1: {'A': [2, 0, 0, 0], 'B': [1, 0, 0, 0], 'C': [0, 0, 0, 0]},
               2: {'A': [2, 0, 0, 0], 'B': [0, 2, 0, 0], 'C': [0, 0, 0, 2], 'D': [0, 0, 2, 0]},
               3: {'A': [2, 0, 0, 0], 'B': [1, 0, 0, 0], 'C': [0, 0, 0, 0], 'D': [-1, 0, 0, 0]},
               4: {'A': [0, 0, 0, 2], 'B': [0, 0, 0, 1], 'C': [0, 0, 0, 0]},
               5: {'A': [0, 0, 0, 2], 'B': [2, 0, 0, 0], 'C': [0, 0, 0, 0]},
               6: {'A': [0, 0, 2, 0], 'B': [2, 0, 0, 0], 'C': [0, 0, 0, 2], 'D': [0, 2, 0, 0]},
               7: {'A': [0, 0, 2, 0], 'B': [0, 2, 0, 0], 'C': [0, 0, 0, 0]},
               8: {'A': [0, 0, 2, 0], 'B': [0, 0, 1, 0], 'C': [0, 0, 0, 0]},
               9: {'A': [0, 2, 0, 0], 'B': [0, 0, 0, 2], 'C': [2, 0, 0, 0], 'D': [0, 0, 2, 0]},
               10: {'A': [2, 0, 0, 0], 'B': [0, 0, 2, 0], 'C': [0, 2, 0, 0], 'D': [0, 0, 0, 2]},
               11: {'A': [0, 1, 0, 0], 'B': [0, 2, 0, 0], 'C': [0, 0, 0, 0], 'D': [0, -1, 0, 0]},
               12: {'A': [0, 2, 0, 0], 'B': [0, 1, 0, 0], 'C': [0, 0, 0, 0]},
               13: {'A': [0, 0, 0, 2], 'B': [0, 0, 0, 1], 'C': [0, 0, 0, 0], 'D': [0, 0, 0, -1]},
               14: {'A': [0, 0, 2, 0], 'B': [0, 0, 1, 0], 'C': [0, 0, 0, 0], 'D': [0, 0, -1, 0]},
               15: {'A': [0, 0, 0, 2], 'B': [0, 0, 2, 0], 'C': [0, 2, 0, 0], 'D': [2, 0, 0, 0], 'E': [0, 0, 0, 0]}
               }

    punten = systeem[vraagnummer][antwoord]
    return punten


# Stelt de vragen in de vragenlijst die gesplitst zijn met 2 nieuwregels
# Schrijft ook meteen de gegeven antwoorden in een tekstdocument
def vraag_en_antwoord(data):
    totaal = "Dit zijn de antwoorden die gegeven zijn bij de vorige vragenlijst:"
    data = data.split('\n\n')
    ov_antwoord = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    vraagnummer = 1
    iat = 0
    bdam = 0
    se = 0
    fict = 0
    for vraag in data:
        split_vraag = vraag.split('\n')
        vraag = vraag + '\n'
        aant_opt = len(split_vraag)
        if aant_opt == 4:
            keuzes = ['A', 'B', 'C']
        elif aant_opt == 5:
            keuzes = ['A', 'B', 'C', 'D']
        else:
            keuzes = ['A', 'B', 'C', 'D', 'E']
        antwoord = input(vraag)
        antwoord = antwoord.upper()

        while antwoord not in keuzes:
            antwoord = input("Ongeldig antwoord! Probeer opnieuw\n")
            antwoord = antwoord.upper()

        # Puntentelling
        puntenreeks = puntensysteem(antwoord, vraagnummer)
        vraagnummer = vraagnummer + 1
        iat += puntenreeks[0]
        bdam += puntenreeks[1]
        se += puntenreeks[2]
        fict += puntenreeks[3]

        # Systeem zodat het gekozen antwoord ook bij de laatste uitslag tonen optie staat
        terugblik = ov_antwoord[antwoord]
        totaal = totaal + '\n' + \
            split_vraag[0] + '\n' + split_vraag[terugblik] + '\n'

        with open('antwoorden_gebruiker.txt', 'w')as f:
            f.write(totaal)

    if iat > bdam and iat > se and iat > fict:
        input(textwrap.dedent("""
        Gefeliciteerd, jouw aanbevolen specialisatie op basis van deze vragenlijst is Interactie Technologie!\n
        Druk op enter om verder te gaan
        """))
    elif bdam > iat and bdam > se and bdam > fict:
        input(textwrap.dedent("""
        Gefeliciteerd, jouw aanbevolen specialisatie op basis van deze vragenlijst is Business Data Management!\n
        Druk op enter om verder te gaan
        """))
    elif se > iat and se > bdam and se > fict:
        input(textwrap.dedent("""
        Gefeliciteerd, jouw aanbevolen specialisatie op basis van deze vragenlijst is Software Engineering!\n
        Druk op enter om verder te gaan
        """))
    elif fict > iat and fict > bdam and fict > se:
        input(textwrap.dedent("""
        Gefeliciteerd, jouw aanbevolen specialisatie op basis van deze vragenlijst is Forensisch ICT!\n
        Druk op enter om verder te gaan
        """))
    else:
        input(textwrap.dedent("""
        Het lijkt erop dat het een gelijkspel is geworden...\n
        Druk op enter om verder te gaan
        """))


# Het hoofdmenu
def main():
    meerkeuzevragen = vragen_ophalen('sorteerhoed_vragenlijst.txt')
    menu = True

    # Mocht er meer menuknoppen komen moet die bij de lijst 'menukeuze' worden toegevoegd
    menukeuze = ['1', '2', 'Q']
    while menu:
        i = input(textwrap.dedent("""
            Wat wil je doen?
            Maak een keuze door een van de onderstaande opties te typen.\n
            1 = vragenlijst doorlopen
            2 = laatste uitslag tonen
            q = quit
            """))
        i = i.upper()
        if i not in menukeuze:
            print('Die spreuk kent dit programma niet, probeer een andere!\n')
            continue
        while menu:
            if i == 'Q':
                menu = False
                break
            if i == '1':
                vraag_en_antwoord(meerkeuzevragen)
                break
            if i == '2':
                with open('antwoorden_gebruiker.txt') as o:
                    print(o.read() + '\n')
                break


if __name__ == "__main__":
    main()
