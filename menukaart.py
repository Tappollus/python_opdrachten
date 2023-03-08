#Baseer je op de oefening van het menu.
#We gaan nu zorgen dat we de bestelling van een ganse tafel kunnen opnemen.
#Aan elk gerecht koppel je dus een prijs, eventueel apart voor sauzen of voor de smaak.
#Het kan dus ook zijn dat een gerecht meerdere keren wordt gekozen.
#Het eindresultaat moet een tekstbestandje zijn waarbij voor een tafel de afrekening wordt gemaakt.
#Het aantal keren dat een gerecht werd besteld,
#de totale prijs per gerecht en de totale prijs van de hele bestelling.
MenuSelect = {
    0: 'Biefstuk. 22,50 euro',
    1: 'Scampi. 19,75 euro',
    2: 'Mosselen. 20,40 euro',
    3: 'Quinoa. 15,75 euro'
}

MenuPrijs = {
    0: 22.50,
    1: 19.75,
    2: 20.40,
    3: 15.75
}

Bon = []
Totaal = []

x = int(input('Tafelnummer:'))

Selection = int(input('Selecteer een gerecht: '))

while Selection != 4:
    print('0. Biefstuk')
    print('1. Scampis')
    print('2. Mosselen')
    print('3. Quinoa')
    print('4. Stop')
   
    if Selection >= 0 and Selection < 4:
        Bon.append(Selection)
        Totaal.append(MenuPrijs[Selection])
        Selection = int(input('Selecteer een gerecht: '))
    else:
        int(input('verkeerde input, kies een getal uit het menu: '))

bestand = open('Opdracht_40.txt', 'w').write(f'Bon voor tafel {x}\n')

a = (str(Bon.count(0)), ' x ', str(MenuSelect[0]), ': ', str(MenuPrijs[0]*Bon.count(0)), ' euro\n')
bestand = open('Opdracht_40.txt', 'a').writelines(a)

a = (str(Bon.count(1)), ' x ', str(MenuSelect[1]), ': ', str(MenuPrijs[1]*Bon.count(1)), ' euro\n')
bestand = open('Opdracht_40.txt', 'a').writelines(a)

a = (str(Bon.count(2)), ' x ', str(MenuSelect[2]), ': ', str(MenuPrijs[2]*Bon.count(2)), ' euro\n')
bestand = open('Opdracht_40.txt', 'a').writelines(a)

a = (str(Bon.count(3)), ' x ', str(MenuSelect[3]), ': ', str(MenuPrijs[3]*Bon.count(3)), ' euro\n')
bestand = open('Opdracht_40.txt', 'a').writelines(a)

a = ('\nTotaal bedrag: ', str(sum(Totaal)), ' euro.')
bestand = open('Opdracht_40.txt', 'a').writelines(a)
