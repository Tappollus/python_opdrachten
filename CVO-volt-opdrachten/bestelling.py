#Maak voor de bestelling van de stoelen en banken een tekstbestandje waarbij alle informatie komt te staan
#zodanig dat dit makkelijk kan worden uitgeprint en meegenomen als je de bestelling gaat plaatsen.

def AantalKlassen():
    while True:
        try:
            klassen = int(input('In hoeveel klassen worden de tafels en stoelen vervangen?'))
            a = 'Aantal klassen: '
            bestand = open('Opdracht_39.txt', 'w').write(a)
            bestand = open('Opdracht_39.txt', 'a').write(str(klassen))
        except:
            print('Sorry, dit symbool kan ik niet lezen. Wilt u een integer getal invoeren?')
        else:
            break
    return klassen

def AantalLeerlingen(klassen):
    x = 1
    LeerlingenTotaal = []
    while klassen > 0:
        try:
            Leerlingen = int(input(f'Hoeveel leerlingen zitten er in klas {x}?'))
        except:
            print('Sorry, dit symbool kan ik niet lezen. Wilt u een integer getal invoeren?')
            break
        else:
            a = (f'\nKlas {x}: ', str(Leerlingen), ' Leerlingen')
            bestand = open('Opdracht_39.txt', 'a')
            bestand.writelines(a)
            LeerlingenTotaal.append(Leerlingen)
            Leerlingen = 0
            klassen -= 1
            x += 1
    return LeerlingenTotaal

def AantalStoelen(LeerlingenTotaal):
    Stoelen = sum(LeerlingenTotaal)
    return Stoelen

def AantalBanken(LeerlingenTotaal):
    x = 0
    BankenTotaal = []
    while len(LeerlingenTotaal) > x:
        BankenTotaal.append((LeerlingenTotaal[x]//2)+(LeerlingenTotaal[x]%2))
        a = (f'\nKlas {x+1}: ', str((LeerlingenTotaal[x]//2)+(LeerlingenTotaal[x]%2)), ' Banken')
        bestand = open('Opdracht_39.txt', 'a')
        bestand.writelines(a)
        x += 1
    Banken = sum(BankenTotaal)
    return (Banken)
    
klassen = AantalKlassen()
LeerlingenTotaal = AantalLeerlingen(klassen) #lijst
Stoelen = (AantalStoelen(LeerlingenTotaal))
print('Je hebt', Stoelen, 'stoelen nodig.')
Banken = (AantalBanken(LeerlingenTotaal))
print('je hebt', Banken, 'banken nodig.')
a = ('\nJe hebt ', str(Stoelen), ' stoelen nodig.')
bestand = open('Opdracht_39.txt', 'a').writelines(a)
a = ('\nJe hebt ', str(Banken), ' banken nodig.')
bestand = open('Opdracht_39.txt', 'a').writelines(a)

