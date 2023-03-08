"""Dit is de eindopdracht van de CVO-volt cursus python. Het programma bevat 10 mini-games die je moet oplossen. Je kunt zelf kiezen
    hoeveel spellen je wilt spelen. Na afloop kun je je behaalde score van je laatst gespeelde spel terugvinden in een textbestand.
    Veel plezier!"""

import random

def Int(Input):
    while True:
        if Input.isdigit():
            return int(Input)
        else:
            Input = input('Dit is geen integer getal. Probeer opnieuw:')

def Test(Let):
    Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ,'m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Test = []
    while True:
        try:
            for letter in Let:
                Test.append(Letters.index(letter))
        except:
            Let = input('Oeps.... Hoofdletters gebruikt? Alleen kleine letters')
        else:
            break
    return Let

def Bereik(Max):
    while True:
        if Max > 0 and Max <= 10:
            return (Max)
        else:
            Max = Int(input('Kies een getal tussen 1 en 10!'))

def Welkom():
    print(
    'Welkom in de Escape Room!\n'
    'In deze Escape Room vind je 10 puzzels.\n'
    'Probeer zoveel mogelijk puzzels correct op te lossen om de hoogste score te krijgen!\n'
    'Kies zelf hoeveel puzzels je wilt spelen.\n'
    'Veel speelplezier!\n'
    )
    a = input('Voordat we beginnen, Wat is je naam?')
    b = ('Speler: ', a)
    open('Eindopdracht.txt', 'w').writelines(b)
    print(f'Welkom {a}! Laten we beginnen!\n')

def Keuzes():
    Keuzes = []
    Aantal = Int(input('Hoeveel puzzels wil je maken?'))
    while True:
        if Aantal >0 and Aantal <=10:
            while True:
                while len(Keuzes) < Aantal:
                    Randomiser = random.randint(0,9)
                    Keuzes.append(Randomiser)
                if NoDuo(Keuzes):
                    return Keuzes
                else:
                    Keuzes.clear()
        elif Aantal == 0:
            return False
        else:
            Aantal = Int(input('Je kunt maximaal 10 puzzels kiezen. Hoeveel puzzels wil je maken?'))

def Punten(Punt):
    goed = Goed
    fout = Fout
    if Punt == False:
        print('\nHelaas! Dit spel heb je niet gewonnen. Misschien de volgende wel!\n')        
        open('Eindopdracht.txt', 'a').write('Verloren =(')
        fout.append('fout')
    else:
        print('\nGefeliciteerd! Dit spel heb je gewonnen! Op naar de volgende!\n')
        open('Eindopdracht.txt', 'a').write('Gewonnen =D')
        goed.append('goed')

def NoDuo(num):
    lijst = num
    check = list(dict.fromkeys(lijst))
    if len(lijst) == len(check):
        return True
    else:
        return False
    
def Puzzel1():
    getal = random.randint(1, 10)
    print(
        '\nWelkom bij Puzzel 1\n'
        'In deze puzzel moet je een getal raden tussen de 1 en de 10.\n'
        'Je krijgt 3 pogingen om het te raden. Succes!\n'
          )
    a = Bereik(Int(input('Raad een getal tussen de 1 en de 10:')))
            
    for x in range (1, 4):
        if x < 3:
            if a > getal:
                a = Bereik(Int(input('Te hoog. Probeer nog eens:')))
            elif a < getal:
                a = Bereik(Int(input('Te laag. Probeer nog eens:')))
            else:
                print('Goed geraden!')
                open('Eindopdracht.txt', 'a').write('\nPuzzel 1: ')
                Punten(True)
                break        
        else:
            if a == getal:
                open('Eindopdracht.txt', 'a').write('\nPuzzel 1: ')
                print('Goed geraden!')
                Punten(True)
                break    
    else:
        open('Eindopdracht.txt', 'a').write('\nPuzzel 1: ')
        print('game over. Het getal was', getal,)
        Punten(False)
    
def Puzzel2():
    print(
        '\nWelkom bij puzzel 2!\n'
        'In deze puzzel gaan we rekenen.\n'
        'Beantwoord de vragen en veel plezier!\n'
          )
    a = Bereik(Int(input('Geef een getal tussen 1 en 10:')))
    print(
        'Vermenigvuldig jou gekozen getal nu tot drie keer toe met zichzelf.\n'
        'Vermenigvuldig de uitkomst met 2 en trek hier 1 vanaf.'
        )
    Uitkomst = int(((a**4)*2-1))
    Antwoord = Int(input('Wat is het antwoord van de rekensom?'))
    if Antwoord == Uitkomst:
        open('Eindopdracht.txt', 'a').write('\nPuzzel 2: ')
        print('Gefeliciteerd! Goed gerekend!')
        Punten(True)
    else:
        open('Eindopdracht.txt', 'a').write('\nPuzzel 2: ')
        print('Helaas. Het juist antwoord was', Uitkomst)
        Punten(False)
    

def Puzzel3():
    print(
        '\nPuzzel 3. Tadaaa!\n'
        'In deze puzzel mag je een kleur raden!\n'
        'Úit een lijst wordt een kleur gekozen.\n'
        'Je krijgt een hint mee, zodat het niet zwart voor de ogen wordt.\n'
        'je hebt 3 pogingen.\n'
        'Let op! Gebruik geen hoofdletters, punten of andere tekens.\n'
        'Het programma leest deze niet bij deze opdracht.\n'
        'Succes!\n'
          )
    
    Kleuren = ['rood', 'blauw', 'oranje', 'groen', 'paars', 'roze', 'geel', 'bruin']
    getal = random.randint(0,7)
    
    Hints = {
        0: 'Kleur van de liefde',
        1: 'De lucht',
        2: 'Sinaasappel',
        3: 'Gras',
        4: 'Aubergine',
        5: 'Kauwgombal...',
        6: 'Zonnebloem',
        7: 'Wat wordt je als je lang in de zon zit?'
        }

    print(Hints[getal])
    gok = Test(input('Welke kleur wordt er gevraagd?'))
    
    for x in range(1, 4):
        if x<3:
            if gok != Kleuren[getal]:
                print('Hint: ', Hints[getal])
                gok = Test(input('Helaas, verkeerde kleur. Welke kleur wordt er gevraagd?'))
            else:
                print('helemaal correct!')
                open('Eindopdracht.txt', 'a').write('\nPuzzel 3: ')
                Punten(True)
                break
        else:
            if gok == Kleuren[getal]:
                print('helemaal correct!')
                open('Eindopdracht.txt', 'a').write('\nPuzzel 3: ')
                Punten(True)
                break
    else:
        print('Helaas! Het juiste antwoord was', Kleuren[getal])
        open('Eindopdracht.txt', 'a').write('\nPuzzel 3: ')
        Punten(False)
        

def Puzzel4():
    print(
        '\nPuzzel 4 let\'s goooo.\n'
        'Ok. Eigenlijk is dit een raadsel.\n'
        'Geen hoofdletters gebruiken in je antwoord, anders is het automatisch fout.\n'
        'Je hebt drie pogingen.\n'
        )

    Antwoord = 'gras'
    Vraag = Test(input('Het is groen en als je het niet scheert wordt het heel lang.'))

    for x in range(1, 4):
        if x<3:
            if Vraag != Antwoord:
                print('Helaas, probeer opnieuw.')
                Vraag = Test(input('Het is groen en als je het niet scheert wordt het heel lang.'))
            else:
                print('Gefeliciteerd! Dat is correct!')
                open('Eindopdracht.txt', 'a').write('\nPuzzel 4: ')
                Punten(True)
                break
        else:
            if Vraag == Antwoord:
                print('Gefeliciteerd! Dat is correct!')
                open('Eindopdracht.txt', 'a').write('\nPuzzel 4: ')
                Punten(True)
                break
               
    else:
        print('Helaas. Je hebt het niet geraden. Het antwoord was', Antwoord)
        open('Eindopdracht.txt', 'a').write('\nPuzzel 4: ')
        Punten(False)

def Puzzel5():
    print(
        '\nPuzzel 5!\n'
        'In deze puzzel gaan we de tafels oefenen.\n'
        'Gegeven wordt een getal. Jou taak is om in één keer de tafel correct in te geven.\n'
        'Succes?\n'
        )
    Tafel = random.randint(1, 10)
    Check = []
    Antwoord = []
    x=1
    while len(Check) <10:
        Check.append(Tafel*x)
        x+=1

    print('De tafel van',Tafel)
    x=1
    y=0
    Antwoord.append(Int(input(f'Geef getal {x}:')))
    x+=1
    while len(Antwoord)<10:
        if Antwoord[y] == Check[y]:
            Antwoord.append(Int(input(f'Geef getal {x}:')))
            x+=1
            y+=1
        else:
            print('Helaas. Het is niet gelukt in één keer de tafel van', Tafel, 'te geven.')
            open('Eindopdracht.txt', 'a').write('\nPuzzel 5: ')
            Punten(False)
            break
    else:
        print('Goed gedaan! Ik wist dat je het kon!')
        open('Eindopdracht.txt', 'a').write('\nPuzzel 5: ')
        Punten(True)    

def Puzzel6():
    print(
        '\nPuzzel6. Kraak de code!\n'
        'Je hebt een kistje gevonden.\n'
        'In het kistje ligt een bedankje, je hoeft hem alleen maar te openen.\n'
        'Openen doe je het kistje door eerst een cijfer te raden, daarna een kleine letter.\n'
        'Na 10 pogingen is het slot kapot en vernietigd het kistje zichzelf.\n'
        'Succes!\n'
        )
    Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ,'m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    GeheimeCode = [(random.randint(1, 9)), (Letters[random.randint(0, 25)])]

    Cijf = []
    Let= []
    x=0
    Cijfer = Int(input('Geef een cijfer: '))
    Letter = Test(input('Geef een letter: '))
    while x<10:
        if Cijfer != GeheimeCode[0] and Letter != GeheimeCode[1]:
            print('Beide antwoorden zijn niet juist. Probeer opnieuw: ')
            Cijf.append(Cijfer)
            Let.append(Letter)
            print(Cijf, Let)
            x+=1
            Cijfer = Int(input('Geef een cijfer: '))
            Letter = Test(input('Geef een letter: '))
        elif Cijfer == GeheimeCode[0] and Letter != GeheimeCode[1]:
            print('Het cijfer', Cijfer, 'is juist. Probeer de letter opnieuw: ')
            Let.append(Letter)
            print(Let)
            x+=1
            Letter = Test(input('Geef een letter: '))
            if Letter == GeheimeCode[1]:
                print('Gefeliciteerd! Je hebt het correct!')
                Punten(True)
                break       
        elif Letter == GeheimeCode[1] and Cijfer != (GeheimeCode[0]):
            print('De letter', Letter, 'is juist. Probeer het cijfer opnieuw: ')
            Cijf.append(Cijfer)
            print(Cijf)
            x+=1
            Cijfer = Int(input('Geef een cijfer: '))
            if Cijfer == GeheimeCode[0]:
                print('Gefeliciteerd! Je hebt het correct!')
                open('Eindopdracht.txt', 'a').write('\nPuzzel 6: ')
                Punten(True)
                break
        else:
            print('Gefeliciteerd! je hebt het correct!')
            open('Eindopdracht.txt', 'a').write('\nPuzzel 6: ')
            Punten(True)
            break
    else:
        print('Helaas, je hebt het fout.')
        open('Eindopdracht.txt', 'a').write('\nPuzzel 6: ')
        Punten(False)
    
def Puzzel7():
    print(
        'Puzzeltje 7.\n'
        'We gaan weer woorden raden.\n'
        'Dit keer met getallen!\n'
        'Je krijgt een hint. Op basis daarvan moet je raden wat het getal is.\n'
        'Driemaal is scheepsrecht!\n'
          )
    
    Kleuren = [1, 2, 3, 4, 5, 6, 7, 8]
    getal = random.randint(0,7)
    
    Hints = {
        0: 'Hoeveel exemplaren zijn er van de aarde?',
        1: 'Hoeveel handen heb je? Hopelijk?',
        2: 'Hoeveel biggetjes at de wolf op?',
        3: 'Hoeveel op een rij?',
        4: 'Welk getal is vrijdag?',
        5: 'De helft van een dozijn?',
        6: 'Dit getal x3 levert je veel geld op.',
        7: 'octopus.'
        }

    print(Hints[getal])
    gok = Int(input('Welk nummer wordt er gevraagd?'))
    
    for x in range(1, 4):
        if x<3:
            if gok != Kleuren[getal]:
                print('Hnit: ', Hints[getal])
                gok = Int(input('Helaas, verkeerd nummer. Welk nummer wordt er gevraagd?'))
            else:
                print('helemaal correct!')
                open('Eindopdracht.txt', 'a').write('\nPuzzel 7: ')
                Punten(True)
                break
        else:
            if gok == Kleuren[getal]:
                print('helemaal correct!')
                open('Eindopdracht.txt', 'a').write('\nPuzzel 7: ')
                Punten(True)
                break
    else:
        print('Helaas! Het juiste antwoord was', Kleuren[getal])
        open('Eindopdracht.txt', 'a').write('\nPuzzel 7: ')
        Punten(False)

def Puzzel8():
    print(
        '\nWelkom bij puzzel 8!\n'
        'In deze puzzel gaan we weer rekenen\n'
        'Beantwoord de vragen en veel plezier!\n'
          )
    a = Bereik(Int(input('Geef een getal tussen 1 en 10:')))
    print(
        'Vermenigvuldig jou gekozen getal nu tot 5 keer toe met zichzelf.\n'
        'Vermenigvuldig de uitkomst met 4 en deel door twee.\n'
        'Tel hier 100 bij op en haal er 16 vanaf.\n'
        )
    Uitkomst = int(((a**5)*4/2+100-16))
    Antwoord = Int(input('Wat is het antwoord van de rekensom?'))
    if Antwoord == Uitkomst:
        open('Eindopdracht.txt', 'a').write('\nPuzzel 8: ')
        print('Gefeliciteerd! Goed gerekend!')
        Punten(True)
    else:
        open('Eindopdracht.txt', 'a').write('\nPuzzel 8: ')
        print('Helaas. Het juist antwoord was', Uitkomst)
        Punten(False)

def Puzzel9():
    print(
        '\nPuzzel 9.\n'
        'Ok. Eigenlijk is dit nog een raadsel.\n'
        'Geen hoofdletters gebruiken in je antwoord, anders is het automatisch fout.\n'
        'Je hebt drie pogingen.\n'
        )

    Antwoord = 'zon'
    Vraag = Test(input('Het is geel en als je er te lang naar staart wordt je blind.'))

    for x in range(1, 4):
        if x<3:
            if Vraag != Antwoord:
                print('Helaas, probeer opnieuw.')
                Vraag = Test(input('Het is geel en als je er te lang naar staart wordt je blind.'))
            else:
                print('Gefeliciteerd! Dat is correct!')
                open('Eindopdracht.txt', 'a').write('\nPuzzel 9: ')
                Punten(True)
                break
        else:
            if Vraag == Antwoord:
                print('Gefeliciteerd! Dat is correct!')
                open('Eindopdracht.txt', 'a').write('\nPuzzel 9: ')
                Punten(True)
                break
               
    else:
        print('Helaas. Je hebt het niet geraden. Het antwoord was', Antwoord)
        open('Eindopdracht.txt', 'a').write('\nPuzzel 9: ')
        Punten(False)

def Puzzel10():
    print(
        'Puzzel 10!!!.'
        'We gaan kijken hoeveel jou naam waard is.\n'
        'Elke letter heeft een waarde, dezelfde waarde als zijn plek in het alfabet.\n'
        'A is bijvoorbeeld 1, en D is 4. Snap je?'
        'Laten we beginnen!'
          )
    Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ,'m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Naam = Test(input('Voer je naam in: '))
    Waarde = []    
    for letter in Naam:
        Waarde.append(Letters.index(letter))
    
    gok = Int(input('Goed rekenen, want je hebt 1 poging! Wat is jou naam waard?'))
    if gok == sum(Waarde):
        print('gefeliciteerd! Jij bent je eigen waarde in goud waard!')
        open('Eindopdracht.txt', 'a').write('\nPuzzel 10: ')
        Punten(True)
    else:
        print('Wat jammer! Ik vind je wel veel waard hoor. Je was', sum(Waarde), 'waard!')
        open('Eindopdracht.txt', 'a').write('\nPuzzel 10: ')
        Punten(False)
        
def Puzzelzoeker(Keus):
    Puzzels = {
        0:Puzzel1,
        1:Puzzel2,
        2:Puzzel3,
        3:Puzzel4,
        4:Puzzel5,
        5:Puzzel6,
        6:Puzzel7,
        7:Puzzel8,
        8:Puzzel9,
        9:Puzzel10
    }
    Puzzels[Keus]()

Welkom()
x=1
while True:
    Keuze = Keuzes()
    Totaal = len(Keuze)
    Goed = []
    Fout = []
    print(len(Keuze), 'puzzels? Komt in orde ! Op naar de eerste.\n')
    a = ('\nAantal puzzels: ', str(len(Keuze)))
    open('Eindopdracht.txt', 'a').writelines(a)

    if Keuze == False:
        print('Bedankt voor het spelen! Tot ziens!')
    else:
        while len(Keuze) != 0:
            Puzzelzoeker(Keuze[0])            
            Keuze.pop(0)
    print('Op naar de volgende? De volgende is op!\n')
    score = ('\nAantal goed: ', str(len(Goed)), '\nAantal fout: ', str(len(Fout)), '\nScore: ', str((len(Goed)/Totaal*100)), '%\n')
    open('Eindopdracht.txt', 'a').writelines(score)
    vervolg = input('Dit was de escaperoom. Nog eens spelen? ja/nee')
    if vervolg == 'ja':
        print('Let\'s go!')
        x+=1
        open('Eindopdracht.txt', 'a').write(f'\nPoging {x}.\n')
    else:
        print('Bedankt voor het spelen!')
        break