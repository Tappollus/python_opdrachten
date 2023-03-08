#Pas je oefening van breek de code zodanig aan dat alles wat tot nu toe op het scherm verscheen
#in een tekst bestand komt te staan.
#Je moet dus de informatie van alle pogingen kunnen zien en als je het fout hebt geraden ook wat de code wel.

import random

#genereert de geheime code
def generator():
    geheime_code = []
    nummer = random.randint(1,7)

    while True:
        while len(geheime_code) <4:
            geheime_code.append(nummer)
            nummer = random.randint(1,7)
        if geen_dubbele(geheime_code):
            return geheime_code
        else:
            geheime_code.clear()

#controleert of er geen dubbele cijfers worden gebruikt
def geen_dubbele(num):
    lijst = num
    check = list(dict.fromkeys(lijst))
    if len(lijst) == len(check):
        return True
    else:
        return False

#telt het aantal cijfers op de juiste plek en welke op de verkeerde plek staan
def nummer_goed_plek(goed,plek):
    goed_plek = [0,0]
    geheimecode = geheime_code
    poging = gok
    
    for a, b in zip (geheimecode, poging):
        if b in geheime_code:
            if  b == a:
                goed_plek[0] += 1
            else:
                goed_plek[1] += 1
    return goed_plek


geheime_code = generator()
pogingen = 10
print(geheime_code)

# Tutorial met spelregels.
print('Hallo beste deelnemer! In dit spel gaan we een code raden. Hieronder de spelregels:')
print('1. Je moet een code raden van 4 getallen')
print('2. De code bestaat alleen uit cijfers tussen de 1 en de 7.')
print('3. Elk cijfer mag maar één keer voorkomen.')
print('4. Je krijgt 10 beurten om het getal te raden.')
print('5. Ben je het beu? gebruik code 9999 om te stoppen')
a = 'Welkom! Laten we beginnen'
bestand = open('Opdracht_38.txt', 'w').write(a)


#beurtafhandeling
while pogingen > 0:
    gokgetal = (int(input('Voer je gok in:')))
    a = (f'\ninvoer: {gokgetal}')
    bestand = open('Opdracht_38.txt', 'a').write(a)
    if gokgetal == 9999:
        y = input('weet je het zeker? ja/nee')
        a =  ('\nSpeler geeft aan te willen stoppen')
        bestand = open('Opdracht_38.txt', 'a').write(a)
        if y == 'ja':
            print('game over')
            a = ('\nInvoer was ja. Game over')
            bestand = open('Opdracht_38.txt', 'a').write(a)
            break
        else:
            a = ('\nSpeler verkoos toch door te spelen')
            bestand = open('Opdracht_38.txt', 'a').write(a)
            continue
        
    gok = [int(z) for z in str(gokgetal)]
    if not geen_dubbele(gok):
        print('Het nummer mag geen herhalende nummers bevatten. Probeer opnieuw.')
        a = ('\nHet nummer mag geen herhalende nummers bevatten. Probeer opnieuw.')
        bestand = open('Opdracht_38.txt', 'a').write(a)
        continue
    
    if len(gok) != 4:
        print('Voer 4 cijfers in. Probeer opnieuw.')
        a = ('\nVoer 4 cijfers in. Probeer opnieuw.')
        bestand = open('Opdracht_38.txt', 'a').write(a)
        continue
    
    if 0 in gok or 8 in gok or 9 in gok:
        print('gebruik getallen tussen de 1 en 7. Probeer opnieuw.')
        a = ('\ngebruik getallen tussen de 1 en 7. Probeer opnieuw.')
        bestand = open('Opdracht_38.txt', 'a').write(a)
        continue
    
    goed_plek = nummer_goed_plek(geheime_code,gok)
    print(goed_plek[0], 'goed,', goed_plek[1], 'niet op de juiste plek')
    a = (f'\n{goed_plek[0]} goed, {goed_plek[1]} niet op de juiste plek')
    bestand = open('Opdracht_38.txt', 'a').write(a)
    pogingen -= 1
    print('nog', pogingen, 'beurten')
    a = (f'\nnog {pogingen} beurten')
    bestand = open('Opdracht_38.txt', 'a').write(a)
    
    if goed_plek[0] == 4:
        print('gefeliciteerd! je hebt de code gekraakt!')
        a = ('\nGefeliciteerd! Je hebt de code gekraakt!')
        bestand = open('Opdracht_38.txt', 'a').write(a)
        break

else:
    print('Je pogingen zijn op. Het nummer was', geheime_code)
    a = (f'\nJe pogingen zijn op. Het nummer was {geheime_code}')
    bestand = open('Opdracht_38.txt', 'a').write(a)
    