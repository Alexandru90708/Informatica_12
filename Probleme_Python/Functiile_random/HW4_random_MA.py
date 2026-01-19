import random
teme = ["Geografie", "Istorie", "Știință", "Sport", "Cultură generală"]
intrebari = {
    "Geografie": [
        ("Capitala Franței?", "Paris"),
        ("Cel mai mare ocean?", "Pacific"),
        ("Cea mai mare țară?", "Rusia"),
        ("Capitala Germaniei?", "Berlin"),
        ("Capitala Italiei?", "Roma"),
        ("Cel mai lung fluviu?", "Nilul"),
        ("Capitala Spaniei?", "Madrid"),
        ("Capitala României?", "București"),
        ("Cel mai înalt munte?", "Everest"),
        ("Ce mare spală România?", "Neagră")
    ],
    "Istorie": [
        ("Cine a fost Mihai Viteazul?", "Domnitor"),
        ("Când s-a unit Moldova cu Țara Românească?", "1859"),
        ("Cine a descoperit America?", "Columb"),
        ("Când a avut loc Revoluția Franceză?", "1789"),
        ("Cine a fost Napoleon?", "Împărat"),
        ("Cine a fost Ștefan cel Mare?", "Domnitor"),
        ("Când a început Primul Război Mondial?", "1914"),
        ("Când s-a terminat al Doilea Război Mondial?", "1945"),
        ("Cine a fost Alexandru cel Mare?", "Conducător"),
        ("Cine a fost Decebal?", "Rege")
    ],
    "Știință": [
        ("Formula apei?", "H2O"),
        ("Planeta cea mai apropiată de Soare?", "Mercur"),
        ("Ce gaz respirăm?", "Oxigen"),
        ("Cine a descoperit gravitația?", "Newton"),
        ("Câte planete sunt în sistemul solar?", "8"),
        ("Cine a inventat becul?", "Edison"),
        ("Ce organ pompează sângele?", "Inima"),
        ("Cine a descoperit penicilina?", "Fleming"),
        ("Ce organ controlează corpul?", "Creierul"),
        ("Ce este fotosinteza?", "Procesul prin care plantele produc oxigen")
    ],
    "Sport": [
        ("Câte minute are un meci de fotbal?", "90"),
        ("Ce sport folosește o rachetă?", "Tenis"),
        ("Câte cercuri are sigla olimpică?", "5"),
        ("Unde s-a născut Nadia Comăneci?", "România"),
        ("Cine este Messi?", "Fotbalist"),
        ("Cine este Michael Jordan?", "Baschetbalist"),
        ("Ce sport se joacă pe gheață?", "Hochei"),
        ("Câte jucătoare sunt într-o echipă de handbal?", "7"),
        ("Ce sport se joacă cu o minge ovală?", "Rugby"),
        ("Cine a câștigat CM 2018 la fotbal?", "Franța")
    ],
    "Cultură generală": [
        ("Câte litere are alfabetul românesc?", "31"),
        ("Cine a scris 'Luceafărul'?", "Eminescu"),
        ("Cine a pictat Mona Lisa?", "Da Vinci"),
        ("Ce monedă are SUA?", "Dolar"),
        ("Câte continente are Pământul?", "7"),
        ("Cel mai mare mamifer?", "Balena albastră"),
        ("Ce limbă se vorbește în Brazilia?", "Portugheză"),
        ("Culoarea smaraldului?", "Verde"),
        ("Câte zile are un an bisect?", "366"),
        ("Ce zi vine după joi?", "Vineri")
    ]
}
tema = random.choice(teme)
print(f"Tema aleasă: {tema}\n")
random.shuffle(intrebari[tema])
scor = 0
for i, (q, r) in enumerate(intrebari[tema],1):
    print(f"{i}. {q}")
    raspuns=input("Răspuns: ").strip()
    if raspuns.lower() == r.lower():
        print("Corect!\n")
        scor += 1
    else:
        print(f"Greșit! Răspuns corect: {r}\n")
print(f"Ai terminat! Ai avut {scor} răspunsuri corecte din 10.")
