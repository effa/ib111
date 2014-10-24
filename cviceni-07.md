# Cvičení 7: Pascal a řazení

## Pascalův trojúhelník: kombinační čísla

Napište funkci pro vypsání Pascalova trojúhelníka za využití výpočtu kombinačního čísla.

```
>>> pascaluv_trojuhelnik(10)

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
```

Kostra řešení:

```python
# Vrati n!
def faktorial(n):
    pass

# Vrati hodnotu kombinacniho cisla 'n nad k'.
def kombinacni_cislo(n, k):
    pass

# Vypise dany pocet radku Pascalova trojuhelnika za vyuziti vypoctu
# kombinacniho cisla
def pascaluv_trojuhelnik_kombinacne(pocet_radku):
    pass
```

## Pascalův trojúhelník: z předchozího řádku

Napište opět funkci pro vypsání Pascalova trojuhelnika, tentokrát ale za
použití iterativního přístupu, kde se pro výpočet čísla na řádku používají
hodnoty z řádku předchozího.

```python
# Vypise dany pocet radku Pascalova trojuhelnika za vyuziti
# iterativniho pristupu.
def pascaluv_trojuhlenik_iteracne(pocet_radku):
    pass
```

## Řadicí algoritmy

V praxi se používají zabudované funkce `list.sort` a `sorted`, viz [referenční
manuál](http://docs.python.org/2/howto/sorting.html).


Pro snazší testování správnosti řadících algoritmů si napište funkci, která
vygeneruje seznam dané délky obsahující náhodná čísla z daného rozsahu.

```
>>> nahodny_seznam(delka, rozsah)
[2, 8, 14, 7, 13, 7, 4, 20]
```

Naimplementujte sami funkce pro řazení podle následujících algoritmů:

* řazení výběrem (selection sort)
* řazení vkládáním (insertion sort)
* řazení výměnou (bubble sort)

```
def razeni_vyberem(seznam): ...

>>> s = [5, 4, 3, 2, 1]
>>> razeni_vyberem(s)
>>> print s
>>> [1, 2, 3, 4, 5]
```

## Řazení podle klíče

Přečtěte si část referenčního manuálu o [řazení podle vlastního
klíče](https://docs.python.org/2/howto/sorting.html#key-functions)
a napište funkce pro řazení seznamu slov podle následujících kriteríí:

  * vzestupně podle jejich délky
  * sestupně podle jejich délky
  * abecedně, ale pouze podle písmen na lichých pozicích

## Bonusové úlohy

### Rychlé řadící algoritmy

Implementujte některé rychlé řadící algoritmy, např. Quick sort (řazení
rozdělováním) nebo Merge sort (řazení slučováním).

### Superpomalé řadící algoritmy

Implementujte [Stupid sort](http://cs.wikipedia.org/wiki/Stupid_sort), který
náhodně promíchává prvky tak dlouho, dokud není posloupnost seřazená. Jaká je
časová složitost tohoto algoritmu?

### Analýza rychlosti řadících algoritmů

  Proveďte analýzu všech naimplementovaných řadících algoritmů &ndash; jak
  výpočtem, tak experimentálně. Buď můžete vaše funkce doplnit o počítání
  provedených elementárních operací (porovnávání a přiřazení) nebo prostě měřit
  čas nutný k seřazení velkých polí pomocí `time.time()`. Napište si pomocné
  funkce pro generování polí zadané délky (a s různými vlastnostmi: úplně
  náhodné, téměř seřazené, obrácená posloupnost) a zkoušejte, u kterých
  algoritmů se tyto vlastnosti seznamu projeví. Porovnejte svoje algoritmy i
  s vestavěnou metodou `list.sort()`.

### Specializované řadící algoritmy

Implementujte některý z řadících algoritmů vhodných pro speciální typ dat,
např. [Counting sort](http://cs.wikipedia.org/wiki/Counting_sort), který je
dobrý tehdy, pokud počet možných hodnot prvků je výrazně menší než jejich
počet. (Dále můžete vyzkoušet třeba Radix sort nebo Bucket sort.)

### Eratosthenovo síto

  Napište efetkviní funkci pro výpis všech prvočísel do zadané horní meze
  pomocí metody Eratosthenova síta.

