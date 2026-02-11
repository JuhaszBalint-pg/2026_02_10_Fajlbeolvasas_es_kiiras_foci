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
with open('beolvasando_adatok\labdarugok.txt', 'r', encoding='utf-8') as forrasfajl:
    next (forrasfajl)
    for sor in forrasfajl:

        adatok = sor.strip().split(';')
        Nev = adatok[0]
        Csapat = adatok[1]
        Golszam = int(adatok[2])
        Merkozesszam = int(adatok[3])
        jatekos = {'Játékos neve': Nev, 'Csapat neve': Csapat, 'Gólok száma': int(Golszam), 'Mérkőzések száma' : Merkozesszam}
        labdarúgók.append(jatekos)

print(f'{labdarúgók=}')

print('1. feladat')
jatekosokszama = len(labdarúgók)
print(f"A beolvasott fájlban összesen {jatekosokszama} játékos szerepel.")

legkevesebbgol_szam = 100000
print('2. feladat')
for jatekos in labdarúgók:
    if jatekos['Gólok száma'] < legkevesebbgol_szam: 
        legkevesebbgol_szam = jatekos['Gólok száma']
        legkevesebbgol = jatekos['Játékos neve']


print(f"A legkevesebb gólt szerző játékos: {legkevesebbgol}")

legtobbgolszam = 0
print('3. feladat')
for i in labdarúgók:
    if jatekos['Gólok száma'] > legtobbgolszam:
        legtobbgolszam = jatekos['Gólok száma']
        legtobbgol = jatekos['Játékos neve']
print(f"A legtöbb gólt szerző játékos: {legtobbgol}")

legtobbmerkozesszam = 0
print('4. feladat')
for jatekos in labdarúgók:
    if jatekos['Mérkőzések száma'] > legtobbmerkozesszam:
        legtobbmerkozesszam = jatekos['Mérkőzések száma']
        legtobbmerkozes = jatekos['Játékos neve']

print(f"A legtöbb mérkőzést játszó játékos: {legtobbmerkozes}")

osszgolszam = 0
print('5. feladat')
for jatekos in labdarúgók:
    osszgolszam += jatekos['Gólok száma']
    atlaggolok = osszgolszam/len(labdarúgók)
print(f"Az átlagos gólszám: {atlaggolok}")

print("***A legtöbb gólt szerző csapat: ____")

with open('kiirt_adatok\statisztika.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(f'A beolvasott fájlban összesen {jatekosokszama} játékos szerepel.\n')
    celfajl.write(f'A legkevesebb gólt szerző játékos: {legkevesebbgol}\n')
    celfajl.write(f'A legtöbb gólt szerző játékos: {legtobbgol}\n')
    celfajl.write(f'A legtöbb mérkőzést játszó játékos: {legtobbmerkozes}\n')
    celfajl.write(f'Az átlagos gólszám: {atlaggolok}')