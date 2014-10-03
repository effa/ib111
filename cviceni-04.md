# Cvičení 4: Náhodná čísla

Ukázka práce s náhodnými čísly v Pythonu:

    >>> from random import random, randint
    >>> randint(1, 6)
    3
    >>> random()
    0.5956438760824407

▶ [dokumentace knihovny `random`](http://docs.python.org/2/library/random.html).

## Statistiky

Napiště funkci, která vygeneruje `n` čísel z daného rozsahu `[a,b]` a zjistí
základní statistiky &ndash; minimum, maximum a průměr.

    def statistiky(pocet, spodni_mez=0, horni_mez=100): ...

    >>> statistiky(20, 0, 100)
    77 30 58 61 78 18 11 10 98 24 38 35 26 20 17 61 38 16 25 57
    minimum: 10
    maximum: 98
    prumer: 39.9


## Simulace opilce

Opilec je na půli cesty mezi domovem a hospodou, každý krok udělá náhodně jedním
směrem. Napiště funkci, která bude simulovat opilcův pohyb. Jejímy parametry
budou vzdálenost mezi domovem a hospodou a počet kroků do opilcova usnutí (tj.
maximální délka simulace). Simulace skončí buď tehdy, když opilec dojede domů
nebo do hospody, případně po vyčerpání počtu kroků.


    def simulace_opilce(delka, pocet_kroku): ...

    >>> simulace_opilce(10, 100)

    doma . . . . . * . . . . hospoda
    doma . . . . * . . . . . hospoda
    doma . . . * . . . . . . hospoda
    doma . . . . * . . . . . hospoda
    doma . . . * . . . . . . hospoda
    doma . . . . * . . . . . hospoda
    doma . . . * . . . . . . hospoda
    doma . . * . . . . . . . hospoda
    doma . * . . . . . . . . hospoda
    doma . . * . . . . . . . hospoda
    doma . . . * . . . . . . hospoda
    doma . . * . . . . . . . hospoda
    doma . . . * . . . . . . hospoda
    doma . . * . . . . . . . hospoda
    doma . . . * . . . . . . hospoda
    doma . . . . * . . . . . hospoda
    doma . . . . . * . . . . hospoda
    doma . . . . * . . . . . hospoda
    doma . . . . . * . . . . hospoda
    doma . . . . * . . . . . hospoda
    doma . . . . . * . . . . hospoda
    doma . . . . . . * . . . hospoda
    doma . . . . . * . . . . hospoda
    doma . . . . . . * . . . hospoda
    doma . . . . . . . * . . hospoda
    doma . . . . . . . . * . hospoda
    doma . . . . . . . . . * hospoda
    doma . . . . . . . . * . hospoda
    doma . . . . . . . . . * hospoda
    doma . . . . . . . . . . hospoda
    Dosel do hospody.

# Analýza opilce

Nejprve upravte funkci pro simulaci opilce tak, aby vracela `True`, pokud se
opilcovi podaří dojít domů, jinak `False`. Dále přidejte funkci parametr
`vypis`, který bude určovat, zda se má průběh simulace vypisovat. Pak napiště
funkci, která provede daný počet simulací opilcovi procházky a vrátí úspěšnost
dojití domů.

Kostra řešení:

```python
from random import randint

# vypise stav simulace, napriklad:
# >>> vypis_radek(10, 6)
# doma . . . . . * . . . . hospoda
def vypis_radek(delka, poloha):
    pass

# provede simulaci opilcova pohybu
def simulace_opilce(delka, pocet_kroku, vypis=True):
    pass

# provede dany pocet simulaci opilcova pohybu a vypise
# procentualni uspesnost dojiti domu, napriklad:
# >>> analyza_opilce(100, 10, 100)
#
# Procento dojiti domu: 45.9
def analyza_opilce(pocet_pokusu, delka, pocet_kroku):
    pass
```

## Průměrná vzdálenost dvou bodů ve čtverci

Napište funkci, která náhodně zvolí dva body ze čtverce dané velikosti a vrátí
jejich vzdálenost. Následně napište funkci, která tento výběr bude opakovat a
vypíše průměrnou vzdálenost.

## Odhad čísla PI

Naprogramujte funkci využívající náhodná čísla pro odhad čísla PI, inspirovat
se můžete [zde](http://math.fullerton.edu/mathews/n2003/montecarlopimod.html).

Shrnutí algoritmu:

* vygenerujte `n` náhodných bodů ze čtverce o straně `a`
* z vygenerovaných `n` bodů leží `m` v kruhu, který je vepsán do čtverce
* obsah čtverce je `a^2`
* obsah kruhu je `PI * (a/2)^2`
* odhad `PI`: `PI = 4 * (m/n)`

## Bonusové příklady

* výpočet odmocniny pomocí metody binárního půlení
* výpočet čísla PI dalšími způsoby (viz [Wiki: Approximations of PI][1]) a
  srovnání jejich časové náročnosti vzhledem k požadované přesnosti (pro měření
  času využijte např. knihovnu `time`)
[1]: http://en.wikipedia.org/wiki/Approximations_of_%CF%80
* měření času můžete vyzkoušet také pro různé příklady z minulého cvičení (např.
  součet n čísel různými způsoby, největší společný dělitel - hrubou silou,
  "školní algoritmus", Eukleidův algoritmus)
* dále viz [Rozcestník (Zdroje úloh k procvičkování)][2]
[2]: https://github.com/effa/ib111#zdroje-%C3%BAloh-k-procvi%C4%8Den%C3%AD
