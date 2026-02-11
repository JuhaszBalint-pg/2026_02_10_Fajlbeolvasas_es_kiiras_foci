"""
Olvasd be a labdarugok.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány játékos szerepel a fájlban?
2. Melyik játékos szerezte a legkevesebb gólt?
3. Melyik játékos szerzett a legtöbb gólt?
4. Ki játszott a legtöbb mérkőzést?
5. Átlagosan hány gólt szerzett egy játékos?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerzett a legtöbb gólt? (feltételezve, hogy egy játékos csak egy csapatban játszott)


A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""


labdarúgók= []
with open('adatok/autok_listaja.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        next in forrasfajl
        adatok = sor.strip().split(';')
        Nev = adatok[0]
        Csapat = adatok[1]
        Golszam = int(adatok[2])
        Merkozesszam = int(adatok[3])
        jatekos = {'Játékos neve': Nev, 'Csapat neve': Csapat, 'Gólok száma': Golszam, 'Mérkőzések száma' : Merkozesszam}
        labdarúgók.append(jatekos)

print(f'{jatekos=}')
print("A beolvasott fájlban összesen ____ játékos szerepel.")
print("A legkevesebb gólt szerző játékos: ____")
print("A legtöbb gólt szerző játékos: ____")
print("A legtöbb mérkőzést játszó játékos: ____")
print("Az átlagos gólszám: ____")
print("***A legtöbb gólt szerző csapat: ____")