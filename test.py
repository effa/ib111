# Vypise tabulku n krat n, v niz na i-tem radku a j-tem sloupci je soucin
# cisel i a j, ale pouze v pripade, ze je jednociferny (jinak nahradi *)
def tabulka(n):
    pass

# Vrati libovolne pismeno, ktere se nachazi v obou zadanych retezcich.
# Pokud takove pismeno neexistuje, vypise tuto informaci.
def spolecne_pismeno(slovo1, slovo2):
    pass

# Vrati pate nejmensi cislo v seznamu.
# Pokud ma seznam mene nez 5 prvku, vypise prislunou hlasku.
def pate_nejmensi(seznam):
    pass

# Vypise pismeno E v textove grafice o dane vysce.
# Minimalni vyska pismene je 5 (mensi hodnoty budou ignorovany).
def vykresliE(velikost):
    pass

# Provede dany pocet hodu sestistenou kostkou. Vypise pocty, kolikrat bylo
# hozeno ktere cislo a take informaci o hodnote, ktera padla nejvickrat.
def hazeni_kostkou(pocet_hodu):
    pass

# Bonusova uloha
# Vykresli fraktalovy hrad o zadanem poctu pater.
def fraktalovy_hrad(pocet_pater, podstava=200):
    pass


###############################################################################
# Test funkcnosti (nemazte, ale klidne si pridejte vlastni testy)

def hlavicka(num):
    print
    print "###################################################################"
    print "#", num
    print "###################################################################"
    print

hlavicka(1)
tabulka(5)

hlavicka(2)
print spolecne_pismeno("pomeranc", "mandarinka")
print spolecne_pismeno("darek", "oko")
print spolecne_pismeno("aaaaa", "bcd")

hlavicka(3)
print pate_nejmensi([7, 11, 12, 6, 4, 17, 1, 9, 2, 12])
print pate_nejmensi([1, 2, 3, 1, 2])
print pate_nejmensi([1, 2])

hlavicka(4)
for vyska in [5, 7, 9]:
    vykresliE(vyska)
    print

hlavicka(5)
for pocet in [10, 100, 1000]:
    print 'pocet: ' + str(pocet)
    hazeni_kostkou(pocet)
    print

#hlavicka(6)
#fraktalovy_hrad(5)
#exitonclick()
