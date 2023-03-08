#Het is tijd voor het rapport.
#Geef de naam en de voornaam van de cursist in en vervolgens de punten voor
#de vakken Nederlands, Frans, wiskunde en geschiedenis.
#Om te slagen moet de cursist voor elk vak minstens de helft halen.
#Vraag dus ook het maximaal aantal punten dat je per vak kan behalen.
#De output is een tekstbestand waarbij de naam van de cursist wordt vermeld,
#de punten per vak en het totaal dat ze konden behalen en het totaal voor de vier vakken samen.
#Op het einde verschijnt de melding of de cursist al dan niet geslaagd is.

#vraag naam
def Naam():
    Voornaam = str(input('Wat is de voornaam?'))
    Achternaam = str(input('Wat is de achternaam?'))
    return Voornaam, Achternaam

#voldoend of onvoldoende
def Nederlands(maxNl, PuntenNl):
    if PuntenNl >= (MaxNl/2):
        ResultaatNl = 'Voldoende'
    else:
        ResultaatNl = 'Onvoldoende'
        
    return ResultaatNl

def Frans(maxFr, PuntenFr):
    if PuntenFr >= (MaxFr/2):
        ResultaatFr = 'Voldoende'
    else:
        ResultaatFr = 'Onvoldoende'
        
    return ResultaatFr

def Wiskunde(maxWi, PuntenWi):
    if PuntenWi >= (MaxWi/2):
        ResultaatWi = 'Voldoende'
    else:
        ResultaatWi = 'Onvoldoende'
        
    return ResultaatWi

def Geschiedenis(maxGs, PuntenGs):
    if PuntenGs >= (MaxGs/2):
        ResultaatGs = 'Voldoende'
    else:
        ResultaatGs = 'Onvoldoende'
        
    return ResultaatGs

def Slaging(ResultaatNl, ResultaatFr, ResultaatWi, ResultaatGs):
    if ResultaatNl != 'Voldoende' or ResultaatFr != 'Voldoende' or ResultaatWi != 'Voldoende' or ResultaatGs != 'Voldoende':
        Slaging = 'Gezakt'
    else:
        Slaging = 'Geslaagd'
        
    return Slaging

#Integere getallen omzetten naar string zodat deze naar het tekstbestand verplaatst kunnen worden
def Con(converted):
    converted = str(converted)
    return converted


#Naam opslaan
Naam = Naam()
Naam
# maximaal aantal punten en behaald aantal punten per vak
MaxNl = int(input('Wat is het maximum te behalen aantal punten voor Nederlands?'))
PuntenNl = int(input('Wat is het behaald aantal punten voor Nederlands?'))
MaxFr = int(input('Wat is het maximum te behalen aantal punten voor Frans?'))
PuntenFr = int(input('Wat is het behaald aantal punten voor Frans?'))
MaxWi = int(input('Wat is het maximum te behalen aantal punten voor Wiskunde?'))
PuntenWi = int(input('Wat is het behaald aantal punten voor Wiskunde?'))
MaxGs = int(input('Wat is het maximum te behalen aantal punten voor Geschiedenis?'))
PuntenGs = int(input('Wat is het behaald aantal punten voor Geschiedenis?'))

#slagingsgegevens koppelen aan variabelen
ResultaatNl = Nederlands(MaxNl, PuntenNl)
ResultaatFr = Frans(MaxFr, PuntenFr)
ResultaatWi = Wiskunde(MaxWi, PuntenWi)
ResultaatGs = Geschiedenis(MaxGs, PuntenGs)
Slaging = Slaging(ResultaatNl, ResultaatFr, ResultaatWi, ResultaatGs)

#tekstbestand schrijven, naam
a = 'Rapport 2022'
bestand = open('Opdracht_37.txt', 'w').write(a)
a = '\nVoornaam: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(Naam[0])
a = '\nAchternaam: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(Naam[1])

#Nederlands
a = '\n\nNederlands:'
bestand = open('Opdracht_37.txt', 'a').write(a)
a = '\nBehaald aantal punten: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(Con(PuntenNl))
a =  '\nMaximaal aantal punten: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(Con(MaxNl))
a = '\nUitslag: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(ResultaatNl)

#Frans
a = '\n\nFrans:'
bestand = open('Opdracht_37.txt', 'a').write(a)
a = '\nBehaald aantal punten: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(Con(PuntenFr))
a =  '\nMaximaal aantal punten: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(Con(MaxFr))
a = '\nUitslag: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(ResultaatFr)

#Wiskunde
a = '\n\nWiskunde:'
bestand = open('Opdracht_37.txt', 'a').write(a)
a = '\nBehaald aantal punten: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(Con(PuntenWi))
a =  '\nMaximaal aantal punten: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(Con(MaxWi))
a = '\nUitslag: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(ResultaatWi)

#Geschiedenis
a = '\n\nGeschiedenis:'
bestand = open('Opdracht_37.txt', 'a').write(a)
a = '\nBehaald aantal punten: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(Con(PuntenGs))
a =  '\nMaximaal aantal punten: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(Con(MaxGs))
a = '\nUitslag: '
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(ResultaatGs)

#Geslaagd?
a = '\n\nUitslag:'
bestand = open('Opdracht_37.txt', 'a').write(a)
bestand = open('Opdracht_37.txt', 'a').write(Slaging)