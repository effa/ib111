# Cvičení 9: Datové struktury

### Seznam

Seznam je kolekce prvků, v níž můžeme k jednotlivým prvkům přistupovat pomocí
celočíselného indexu. Můžeme nový prvek kamkoliv přidat, přepsat již existující
prvek nebo kterýkoliv prvek odebrat. Seznam je v Pythonu implementován jako typ
*list*, který už dávno známe.


```python
# vytvoreni seznamu
seznam = [1, 3, 2]

# pridani prvku na konec seznamu
seznam.append(10)
# seznam: [1, 3, 2, 10]

# pridani cisla 10 do seznamu na index 1
seznam.insert(1, 10)
# seznam: [1, 10, 3, 2, 10]

# odebrani prvniho vyskytu cisla 10 ze seznamu
seznam.remove(10)
# seznam: [1, 3, 2, 10]

# odebrani prvku na indexu 1
del seznam[1]
# seznam: [1, 2, 10]

# otoceni seznamu
seznam.reverse()
# seznam: [10, 2, 1]

# serazeni seznamu
seznam.sort()
# seznam: [1, 2, 10]
```

▶ [vizualizace uvedeného kódu][1]
[1]: http://pythontutor.com/visualize.html#code=%23+vytvoreni+seznamu%0Aseznam+%3D+%5B1,+3,+2%5D%0A%0A%23+pridani+prvku+na+konec+seznamu%0Aseznam.append(10)%0A%23+seznam%3A+%5B1,+3,+2,+10%5D%0A%0A%23+pridani+cisla+10+do+seznamu+na+index+1%0Aseznam.insert(1,+10)%0A%23+seznam%3A+%5B1,+10,+3,+2,+10%5D%0A%0A%23+odebrani+prvniho+vyskytu+cisla+10+ze+seznamu%0Aseznam.remove(10)%0A%23+seznam%3A+%5B1,+3,+2,+10%5D%0A%0A%23+odebrani+prvku+na+indexu+1%0Adel+seznam%5B1%5D%0A%23+seznam%3A+%5B1,+2,+10%5D%0A%0A%23+otoceni+seznamu%0Aseznam.reverse()%0A%23+seznam%3A+%5B10,+2,+1%5D%0A%0A%23+serazeni+seznamu%0Aseznam.sort()%0A%23+seznam%3A+%5B1,+2,+10%5D&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0

### Zásobník

Zásobník je speciální variantou seznamu &ndash; umožnuje prvky vkládat
a odebírat pouze z vrcholu zásobníku (princip LIFO: *Last In &ndash; First Out*).

Pro zásobník lze použít již známý *list*:

```python
# vytvoreni zasobniku
zasobnik = [1, 2, 3]

# pridani do zasobniku
zasobnik.append(4)
# zasobnik: [1, 2, 3, 4]

# odebrani ze zasobniku
top = zasobnik.pop()
# zasobnik: [1, 2, 3], top: 4

# dalsi odebrani ze zasobniku
top = zasobnik.pop()
# zasobnik: [1, 2], top: 3
```

### Fronta

Fronta je kolekce, do které lze též prvky přidávat a odebírat, pořadí
odebírání se však řídí principem FIFO (*First In &ndash; First Out*), tak jako
v klasické frontě v obchodě. Jedná se tedy opět jen o speciální variantu
seznamu, umožňující vkládat prvky na jeden konec a odebírat z druhého konce.
Mohli bychom tedy klidně využít typ *list*, tento způsob však není moc
efektivní (přidávání nebo odebírání prvklů ze začátku seznamu zabere dost času,
protože se musí všechny prvky dál posunout o 1 pozici). Lepší je tedy použít
specializovaný typ *deque* z knihovny *collections*.

```python
from collections import deque

# 3 studenti cekaji ve fronte na obed
fronta = deque(["Petr", "Zdenek", "Filip"])

# Kuba prisel na konec fronty
fronta.append("Kuba")
# fronta: deque(["Petr", "Zdenek", "Filip", "Kuba"])

# Roman prisel na konec fronty
fronta.append("Roman")
# fronta: deque(["Petr", "Zdenek", "Filip", "Kuba", "Roman"])

# prvni student ve fronte (Petr) dostal obed
student = fronta.popleft()
# fronta: deque(["Zdenek", "Filip", "Kuba", "Roman"]), student: "Petr"

# dalsi student ve fronte (Zdenek) dostal obed
student = fronta.popleft()
# fronta: deque(["Filip", "Kuba", "Roman"]), student: "Zdenek"
```

### Množina

V množině nemají jednotlivé prvky své indexy, ale můžeme prvky přidávat i
odebírat a testovat, zda je nějaký prvek v množině. Množina neobsahuje
duplicity (když do ní třikrát  přidáme číslo 4, pořád ho bude obsahovat pouze
jedenkrát). Přestože nemůžeme přistupovat k jednotlivým prvkům pomocí indexů,
můžeme projít celou množinu (a provést nějakou operaci pro každý prvek
množiny).

```python
# vytvoreni prazdne mnoziny
mnozina = set()

# pridani prvku do mnoziny
mnozina.add(5)
# mnozina: {5}

# pridani stejneho prvku do mnoziny vickrat
mnozina.add(6)
mnozina.add(6)
# mnozina: {5, 6}

# pridani kolekce prvku do mnoziny
mnozina.update([1, 3, 10, 15])
# mnozina: {1, 3, 5, 6, 10, 15}

# odebrani prvku z mnoziny
mnozina.remove(5)
# mnozina: {1, 3, 6, 10, 15}

# zjisteni velikosti mnoziny
pocet_prvku = len(mnozina)
# pocet_prvku: 5

# test vyskytu
if 10 in mnozina:
  print '10 je prvkem mnoziny'

# iterovani pres prvky mnoziny
for x in mnozina:
   print x, x * x
```

Ukázka množinových operací:

```python
# vytvoreni 2 mnozin
>>> a = {1, 3, 5, 7}
>>> b = {2, 3, 4, 5}

# sjednoceni mnozin
>>> a | b
set([1, 2, 3, 4, 5, 7])

# prunik mnozin
>>> a & b
set([3, 5])

# mnozinovy rozdil
>>> a - b
set([1, 7])
```

Množina se dá využít k odstranění duplicitních výskytů ze seznamu:

```python
kosik = ['hruska', 'jablko', 'jablko', 'hruska', 'banan', 'hruska']

# konstruktor mnoziny muze vzit jako parametr libovolnou iterovatelnou kolekci
ovoce = set(kosik)
# ovoce: {’hruska’, ’jablko’, ’banan’}

# pokud potrebujete mit ve vysledku seznam
ovoce = list(set(kosik))
# ovoce: ['hruska', 'jablko', 'banan']
```

### Slovník

Slovník (mapa, asociativní pole) mapuje klíče na hodnoty. Je podobný
seznamu, ale jeho prvky nejsou indexovány pomocí posloupnosti celých čísel, ale
pomocí klíčů (klíčem může být např. číslo, řetězec nebo jiný neměnitelný objekt).

```python
# vytvoreni slovniku
body = {"Filip":66, "Petr":0, "Denis":0}

# pristup k hodnote pod klicem "Filip"
print body["Filip"]
# vypise 66

# pridani nove hodnoty do slovniku
body["Dan"] = 60
# body: {"Filip":66, "Petr":0, "Denis":0, "Dan":60}

# zmena hodnoty pod nejakym klicem
body["Petr"] += 60
# body: {"Filip":66, "Petr":60, "Denis":0, "Dan":60}

# smazani zaznamu s klicem "Denis"
del body["Denis"]
# body: {"Filip":66, "Petr":60, "Dan":60}

# iterace pres klice slovniku
for jmeno in body:
    print jmeno, ':', body[jmeno]

# zjisteni, zda uz je nejaky klic ve slovniku
if "Terka" in body:
    print "Zaznam pro Terku jiz existuje."
else:
    print "Zaznam pro Terku neexistuje."
```

▶ [vizualizace uvedeného kódu][2]
[2]: http://pythontutor.com/visualize.html#code=%23+vytvoreni+slovniku%0Abody+%3D+%7B%22Filip%22%3A66,+%22Petr%22%3A0,+%22Denis%22%3A0%7D%0A%0A%23+pristup+k+hodnote+pod+klicem+%22Filip%22%0Aprint+body%5B%22Filip%22%5D%0A%23+vypise+66%0A%0A%23+pridani+nove+hodnoty+do+slovniku%0Abody%5B%22Dan%22%5D+%3D+60%0A%23+body%3A+%7B%22Filip%22%3A66,+%22Petr%22%3A0,+%22Denis%22%3A0,+%22Dan%22%3A60%7D%0A%0A%23+zmena+hodnoty+pod+nejakym+klicem%0Abody%5B%22Petr%22%5D+%2B%3D+60%0A%23+body%3A+%7B%22Filip%22%3A66,+%22Petr%22%3A60,+%22Denis%22%3A0,+%22Dan%22%3A60%7D%0A%0A%23+smazani+zaznamu+s+klicem+%22Denis%22%0Adel+body%5B%22Denis%22%5D%0A%23+body%3A+%7B%22Filip%22%3A66,+%22Petr%22%3A60,+%22Dan%22%3A60%7D%0A%0A%23+iterace+pres+klice+slovniku%0Afor+jmeno+in+body%3A%0A++print+jmeno,+'%3A',+body%5Bjmeno%5D&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0


## Vyhodnocení postfixového výrazu

Napište funkci pro vyhodocení výrazu v [postfixové notaci](http://cs.wikipedia.org/wiki/Postfixov%C3%A1_notace).
Můžete předpokládat, že zadaný výraz je nad celými číslý a obsahuje pouze
operace sčítání, odčítání a násobení.

```
>>> vyhodnot("3 2 +")
5
>>> vyhodnot("3 2 -")
1
>>> vyhodnot("2 3 -")
-1
>>> vyhodnot("1 5 + 10 8 - *")
12
```

Kostra programou s implementací funkce pro zjišťování, zda nějaký řetězec
reprezentuje číslo.

```python
# vrati True, pokud predany retezec reprezentuje cislo
def je_cislo(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# vyhodnoti vyraz v postfixu (predany jako retezec)
def vyhodnot(vyraz):
    # rozdeleni vyrazu na tokeny
    tokeny = vyraz.split(' ')
    # ...
```


## Frekvenční analýza slov

Napiště funkci, která vypíše počet výskytů jednotlivých slov v textu. Pak ji
rozšiřte tak, aby vypisovala slova sestupně podle počtu jejich výskytů.

```
>>> frekvence_slov("hruska jablko jablko hruska banan hruska hruska")
4  hruska
2  jablko
1  banan
```

## Řazení podle klíče

Seřaďte v příkazové řádce následující seznam

* podle čísel osob
* abecedně podle jmen osob


```python
X = [ { "jmeno" : "Franta", "cislo" : 763 },
      { "jmeno" : "Pepa", "cislo" : 45 },
      { "jmeno" : "Adam", "cislo" : 22 },
      { "jmeno" : "Zuzana", "cislo" : 100 } ]
```

## Kontrola řádku Sudoku

Napište funkci, která zkontroluje, zda předaný seznam reprezentuje správný
řádek vyplněného Sudoku, tj. obsahuje pouze čísla 1 až 9 a každé z nich právě
jedenkrát. [nápověda: množiny]

```
>>> pouzity_vsechny_cislice([1, 2, 8, 9, 3, 5, 6, 7, 4])
True
>>> pouzity_vsechny_cislice([1, 2, 8, 9, 3, 5, 7, 4])
False
>>> pouzity_vsechny_cislice([1, 1, 2, 8, 9, 3, 5, 7, 4])
False
>>> pouzity_vsechny_cislice([0, 1, 2, 3, 4, 5, 6, 7, 8])
False
```

## Všechny samohlásky

Určete, na kterém indexu (při čtení zleva) předaného řetězce už bylo využito
všech šesti samohlásek a, e, i, y, o, u.

```
>>> vsechny_samohlasky('aeiyou')
5
>>> vsechny_samohlasky('iwyoerouapsaaik')
8
```

## Bonusové úlohy

### Pořádné vyhodnocování postfixového výrazu
Vylepšit vyhodnocování postfixového výrayzu tak, aby bylo možné zadávat i
  desetinná čísla, další operace a aby byly ošetřené chybné vstupy.

### Pořádná frekvenční analýza slov
Vylepšit frekvenční analýzu slov tak, aby ze vstupního textu nejprve
  odstranila interpunkci a aby ignorovala velikost písmen (např. *logika* a
  *Logika* se bere jako stejné sltak, aby ze vstupního textu nejprve odstranila
  interpunkci a aby ignorovala velikost písmen (např. *logika* a *Logika* se
  bere jako 2 výskyty stejného slova).

### Frekvenční analýza písmen
Vypiště relativní zastoupení zastoupení znaků v textu (sestupně od nejčastějších
po méně časté).


### Převod infixového výrazu na postfixový

Napište funkci pro převod infixového výrazu na postfixový (a tu můžete následně
využít k vyhodnocování infixového výrazu). Opět využijeme zásobník, tentokrát
však bude sloužit k zapamatování viděných operátorů (+, - , \*) a levých
závorek, zatímco čísla můžeme rovnou přidávat do rozestavěného řetězce
prefixového výrazu. Vstupní infixový výraz procházíme po jednotlivých tokenech
zleva doprava. Je potřeba rozmyslet, co se stane: když navštívím operátor
(nezapomeňte, že různé operátory mají různou prioritu, závorky mají nejvyšší
prioritu) a když navštívím pravou závorku (chceme dokončit zpracování výrazu v
závorce).


### Vyhodnocení logického výrazu v postfixové notaci
Funkce vrátí True, pokud je předaný výrok pravdivý, jinak False. Výraz se skládá z
následujícíh znaků:

* 'T': True
* 'F': False
* 'N': negace
* 'K': konjunkce
* 'A': disjunkce
* 'C': implikace

```
>>> vyhodnot_logicky_vyraz("TFK")
False

>>> vyhodnot_logicky_vyraz("FNTFCNK")
True
```
