# Cvičení 6: Binární vyhledávání

### Co budeme potřebovat

* [metoda binárního půlení](https://www.khanacademy.org/cs/search-space-splitting/5681908310081536)

* [logaritmus](http://www.matematika.cz/logaritmy)

* načítání vstupu od uživatele:

```python
>>> vstup = raw_input()
42
>>> vstup
'42'

>>> vstup = int(raw_input())
42
>>> vstup
42
```


## Hádání čísla člověkem

Napište funkci `hadani_cisla(horni_hranice)`, která umožňuje hrát s počítačem
hru na hádání čísla: počítač si myslí číslo (celé číslo v intervalu `1` až
`horni_hranice`), hrac se ho snaží uhodnout. Po každém pokusu dostane hráč od
počítače informaci, zda je hledané číslo menší nebo větší než to, které si
tipnul. Hru si můžete [vyzkoušet zde](https://www.khanacademy.org/cs/guess-my-number-2/6095780544249856).

    >>> hadani_cisla(10)
    --- pokus c. 1 ---
    Zadej svuj tip: 5
    Moje cislo je mensi.
    --- pokus c. 2 ---
    Zadej svuj tip: 3
    Moje cislo je vetsi.
    --- pokus c. 3 ---
    Zadej svuj tip: 4
    Jo, to je ono!


## Hádání čísla počítačem

Napište funkci `hadani_cisla_pc(horni_hranice)`, která umožňuje hrát s
počítačem hru na hádání čísla, tentokrát si však číslo myslí uživatel a počítač
hádá. Po každém pokusu si počítač vyžádá od uživatele informaci, zda je myšlené
číslo větší nebo menší než to, které si počítač tipnul.

    >>> hadani_cisla_pc(10)
    Mysli si cislo od 1 do 10.
    Je cislo 5 mensi (0), rovno (1), nebo vetsi (2) nez tvoje cislo?
    2
    Je cislo 2 mensi (0), rovno (1), nebo vetsi (2) nez tvoje cislo?
    2
    Tvoje cislo je 1.

## Hádání čísla: počítač vs. počítač

Napište funkci `hadani_cisla_pc_pc(horni_hranice)`, která vykoná hru v hádání
myšleného čísla počítače proti počítači. Na závěr vypíše počet pokusů.

    >>> hadani_cisla_pc_pc(10)
    A: Myslim si cislo od 1 do 10
    --- pokus c. 1 ---
    B: Tipuji 5
    A: Moje cislo je mensi.
    --- pokus c. 2 ---
    B: Tipuji 2
    A: Moje cislo je vetsi.
    --- pokus c. 3 ---
    B: Tipuji 3
    A: Jo, to je ono!
    Uhadnuto na 3 pokusu

## Binární vyhledávání

Napište funkci `binarni_vyhledavani(hodnota, seznam)`, která zjistí, zda se
`hodnota` nachází ve vzestupně uspořádanném `seznamu`. Funkce musí mít
logaritmickou časovou složitost.

    >>> binarni_vyhledavani(5, [1, 2, 5, 8])
    True
    >>> binarni_vyhledavani(4, [1, 2, 5, 8])
    False

## Binární vyhledávání pozice

Vylepšete předchozí funkci tak, aby vracela index pozice, kde se hledaný prvek
nachází. Pokud prvek v seznamu není, vraťte `-1`.

    >>> vyhledani_pozice(5, [1, 2, 5, 8])
    2
    >>> vyhledani_pozice(4, [1, 2, 5, 8])
    -1

## Binární vyhledávání seznamu pozic

Vylepšete předchozí funkci tak, aby vracela seznam indexů pozic, na kterých se
hledaný prvek vyskytuje. Pokud prvek v seznamu není ani jednou, vratíte prázdný
seznam.

    >>> vyhledani_pozic(5, [1, 2, 3, 3, 5, 5, 5, 8])
    [4, 5, 6]
    >>> vyhledani_pozic(4, [1, 2, 5, 8])
    []


## Bonusové příklady

* dokončení příkladů z minula (včetně frekvenční analýzy textu)
* rozměňování mincí (na vstupu je částka, kterou chceme rozměnit, a seznam
  hodnot mincí, úkolem je vyskládat částku pomocí co nejméně mincí)
* [tutor.fi.muni.cz](https://http://tutor.fi.muni.cz/) (Robotanik,
  Matematické pexeso, Regulární výrazy, ...)
