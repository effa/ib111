# Cvičení 13: OOP

S objekty jsme už pracovali několikrát. Například:

```
>>> a = set([2, 5, 8])
>>> print a
set([8, 2, 5])
>>> a.add(9)
>>> print a
set([8, 9, 2, 5])
```

Také knihovna `turtle` umožňuje vytvořit objekt želvy,
můžete tak kreslit více želvami zároveň:

```python
from turtle import Turtle, done

turtle1 = Turtle()
turtle2 = Turtle()
turtle1.right(30)
turtle1.forward(100)
turtle2.right(150)
turtle2.forward(200)
done()
```

Tentokrát si ale vyzkoušíme napsat vlastní třídu a vytvářet objekty (instance)
této naší třídy. Definice jednoduché třídy může vypadat třeba takto:

```python
class Student(object):
    def __init__(self, name):
        self._name = name
        self._points = 0

    def add_points(self, new_points):
        self._points += new_points

    def __str__(self):
        return '{name} ({points} points)'.format(
            name=self._name,
            points=self._points)
```

A následné použítí:

```
>>> s1 = Student('John')
>>> print s1
John (0 points)
>>> s1.add_points(20)
>>> print s1
John (20 points)
```

Podrobněji viz slidy nebo třeba
[oficiální návod](https://docs.python.org/2/tutorial/classes.html).

## Příšera

Doplňte následující kostru třídy a vyzkoušejte její funkčnost.

```python
class Creature(object):

    def __init__(self, name, level, health_max):
        """Inicialize atributu objektu
        """
        pass

    def __str__(self):
        """Vraci textovou reprezentaci prisery.
        """
        pass

    def get_level(self):
        """Vraci level prisery
        """
        pass

    def new_level(self):
        """Zvysi level o 1
        """
        pass

    def attack(self, enemy):
        """Provede utok na protivnika.

        Vysledek zavisi na rozdilu meho a protivnikova levelu,
        ale mel by byt aspon trochu nahodny.
        """
        pass

    def undertake_attack(self, damage):
        """Podstoupi utok o dane sile
        """
        pass

    def is_dead(self):
        """Vraci True, pokud prisera uz nema zadne zivoty
        """
        pass
```


## Geometrické útvary

Napište třídy pro několik jednoduchých geometrických útvarů
(čtverec, kruh, rovnostranný trojúhelník). Každá třída bude mít metody pro
výpočet obvodu, výpočet obsahu a vypsání (`__str__`).

```
>>> square1 = Square((10, 20), 100)
>>> square2 = Square((0, 0), 15)
>>> circle1 = Circle((-130, -130), 100)
>>> print square1
Square at (10, 20) of size 100
>>> print circle1
Circle at (-130, -130) with radius 100
>>> square1.get_perimeter()
400
>>> square1.get_area()
10000
```

Ukázka dynamické vazby jmen metod na jejich definice:

```python
for shape in [square1, circle1, square2]:
    print shape
    print 'perimeter:', shape.get_perimeter()
    print '---'
```

```
Square at (10, 20) of size 100
perimeter: 400
---
Circle at (-130, -130) with radius 100
perimeter: 628.318530718
---
Square at (0, 0) of size 15
perimeter: 60
---
```

Vyzkoušejte si také dynamickou vazbu, vypisujte i obsah útvarů.

*(Bonusová úloha: Přidejte do každé třídy metodu pro vykreslování, to můžete
implementovat buď pomocí želví grafiky, knihovny Image nebo vytváření vlastního
SVG souboru.)*


## Zápasy

Naprogramujte hru simulující zápas dvou příšer, robotů, čarodějů, Pokémonů, ...
Můžete využít třídu `Creature` výše a libovolně ji upravit
(například přidat energii, rychlost, přesnost, ...).

Kromě třídy pro zápasníka je vhodné vytvořit také třídu pro zápas (např. s metodami
pro inicializaci, spuštění hry, provedení 1 kola, výpisu stavu, výběru útoku) a
pokud chcete mít různé útoky, tak i třídu pro útok (např. s metodami pro výpis
textové reprezentace útoku a pro zjištění aktuální síly útoku závislé částečně
na náhodě).

Spuštění zápasu mezi Charizardem a Machampem pak může vypadat následovně:

```
# vytovreni utoku a zapasniku (lepe by bylo nacitat ze souboru)
seknuti = Utok('seknuti', 15, 5, 90)
kridlovy_utok = Utok('kridlovy utok', 30, 15, 90)
...

charizard = Pokemon('Charizard', 300, 120, 100,
    [seknuti, kridlovy_utok, plamenomet, seismicky_vrh])

machamp = Pokemon('Machamp', 280, 130, 100,
    [rana_pesti, mega_rana, kop_s_otockou, zly_pohled])

zapas = Zapas(machamp, charizard)
zapas.start()
```

A ukázka konkrétní hry (2 hráči se střídají po 1 tahu):

```
Machamp        |##########| 180/180    |##########| 130/130
-------         pocet zivotu            energie

Charizard      |##########| 200/200    |##########| 120/120
---------       pocet zivotu            energie

+------------------- Machamp --------------------+
nazev                    sila  presnost  narocnost
1 - rana pesti             15        90          5
2 - mega rana              70        75         40
3 - kop s otockou          50        85         30
4 - zly pohled              0        50          0
+------------------------------------------------+
Zvolte utok:  2

> Machamp pouzil mega rana, ale netrefil se!

Machamp        |##########| 180/180    |#######---| 90/130
-------         pocet zivotu            energie

Charizard      |##########| 200/200    |##########| 120/120
---------       pocet zivotu            energie

+------------------- Charizard --------------------+
nazev                    sila  presnost  narocnost
1 - seknuti                15        90          5
2 - kridlovy utok          30        90         15
3 - plamenomet             60        80         35
4 - seismicky vrh         110        70         60
+--------------------------------------------------+
Zvolte utok:  2

> Charizard pouzil kridlovy utok
> Machamp byl zasazen a prisel o 35 zivotu

Machamp        |#########-| 145/180    |########--| 103/130
-------         pocet zivotu            energie

Charizard      |##########| 200/200    |#########-| 105/120
---------       pocet zivotu            energie

+------------------- Machamp --------------------+
nazev                    sila  presnost  narocnost
1 - rana pesti             15        90          5
2 - mega rana              70        75         40
3 - kop s otockou          50        85         30
4 - zly pohled              0        50          0
+------------------------------------------------+
Zvolte utok:  2

> Machamp pouzil mega rana
> Charizard byl zasazen a prisel o 73 zivotu

Machamp        |#########-| 145/180    |#####-----| 63/130
-------         pocet zivotu            energie

Charizard      |#######---| 127/200    |##########| 117/120
---------       pocet zivotu            energie

+------------------- Charizard --------------------+
nazev                    sila  presnost  narocnost
1 - seknuti                15        90          5
2 - kridlovy utok          30        90         15
3 - plamenomet             60        80         35
4 - seismicky vrh         110        70         60
+--------------------------------------------------+
Zvolte utok:  4

> Charizard pouzil seismicky vrh
> Machamp byl zasazen a prisel o 121 zivotu

Machamp        |##--------| 24/180     |######----| 76/130
-------         pocet zivotu            energie

Charizard      |#######---| 127/200    |#####-----| 57/120
---------       pocet zivotu            energie

+------------------- Machamp --------------------+
nazev                    sila  presnost  narocnost
1 - rana pesti             15        90          5
2 - mega rana              70        75         40
3 - kop s otockou          50        85         30
4 - zly pohled              0        50          0
+------------------------------------------------+
Zvolte utok:  3

> Machamp pouzil kop s otockou
> Charizard byl zasazen a prisel o 54 zivotu

Machamp        |##--------| 24/180     |####------| 46/130
-------         pocet zivotu            energie

Charizard      |####------| 73/200     |######----| 69/120
---------       pocet zivotu            energie

+------------------- Charizard --------------------+
nazev                    sila  presnost  narocnost
1 - seknuti                15        90          5
2 - kridlovy utok          30        90         15
3 - plamenomet             60        80         35
4 - seismicky vrh         110        70         60
+--------------------------------------------------+
Zvolte utok:  2

> Charizard pouzil kridlovy utok
> Machamp byl zasazen a prisel o 24 zivotu

Machamp        |----------| 0/180      |####------| 46/130
-------         pocet zivotu            energie

Charizard      |####------| 73/200     |#####-----| 54/120
---------       pocet zivotu            energie

Zvitezil Charizard
```

Náměty na rozšíření: načítání útoků a příšer ze souborů, ošetření kontroly
vstupu (pomocí výjimek), grafické uživatelské rozhraní.

## A co dál?

Spoustu zajímavých a důležitých věcí týkajících se programování a Pythonu
jsme v tomto úvodním kurzu nepokryli. Pokud někdy budete mít náladu naučit se
něco dalšího, zde je seznam, který vám pomůže. Stačí vzít libovolnou položku,
přeložit do angličtiny, připojit slovo Python a hodit do Googlu.

* výjimky
* testování (unit testy)
* grafické uživatelské rozhraní
* webovky (Django, Google App Engine, ...)
* algoritmy a datové struktury
* ipython, ipython notebook, virtualenv
* vědecké výpočty (SciPy, NumPy, matplotlib, NLTK, ...)
* prvky funkcionálního programování (např. list comprehensions)
* vlákna
* JSON
* generátory a iterátory
* uzávěry
* dekorátory
* ...

