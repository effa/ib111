# Domácí úloha 1

**soft deadline: neděle 28. 9.**
(hard deadline: neděle 5. 10.)

* Úloha se skládá z 5 příkladů, za každý můžete získat 4 body, takže celkem až
  20 bodů.
* Pro absolvování předmětu je potřeba odevzdat všechny úlohy a celkově z úloh
  získat alespoň 80 bodů.
* Odevzdejte jediný soubor `uloha01.py` s definicemi požadovaných funkcí.
* Funkce pojmenujte stejně, jako je v zadání.
* Pište přehledný kód, používejte vhodná jména proměnných a případné složitější
  konstrukce opatřete komentářem.
* Nepoužívejte diakritiku (ani v komentářích).
* Pokud se vám nějakou úlohu nepodaří úplně vyřešit, napište alespoň část
  řešení a popište váš problém.
* Pracujte samostatně, za opisování je -30 bodů.

## Posloupnost 1

Napište funkci `posloupnost1(n)`, která vypíše prvních n členů posloupnosti,
ve které se střídají násobky 7 s číslem 1.

    def posloupnost1(n): ...

    >>> posloupnost1(10)
    7 1 14 1 21 1 28 1 35 1

## Posloupnost 2

Napište funkci `posloupnost2(n)`, která vypíše prvních n členů posloupnosti,
která začíná čísly 1, 2 a každý další člen získáme jako poslední dvě cifry
součinu dvou předchozích čísel.

    def posloupnost2(n): ...

    >>> posloupnost2(10)
    1 2 2 4 8 32 56 92 52 84

Tip: poslední dvě cifry získáte pomocí operace "zbytek po dělení stem", např.
`(8 * 32) % 100 = (256 % 100) = 56`


## Posloupnost 3

Napište funkci `posloupnost3(n)`, která vypíše čísla od 1 do n, která jsou
dělitelná 8, ale přitom nejsou dělitelná 3.

    def posloupnost3(n): ...

    >>> posloupnost3(100)
    8 16 32 40 56 64 80 88

Tip: Pro spojení dvou podmínek, které musí platit současně, použijte klíčové
slovo `and`.

## Obdélník

Funkce `obdelnik(a, b)` vykreslí prázdný obdélník o rozměrech (a, b), kde `a`
je šířka a `b` je výška. Prázdností je myšleno rozlišení okraje a vnitřku
obdélníku pomocí různých znaků.

    def obdelnik(a, b): ...

    >>> obdelnik(10, 7)

    + + + + + + + + + +
    + . . . . . . . . +
    + . . . . . . . . +
    + . . . . . . . . +
    + . . . . . . . . +
    + . . . . . . . . +
    + + + + + + + + + +


## Diamant

Funkce `diamant(n)` vykreslí diamant (kosočtverec) o straně délky n.

    def diamant(n):

    >>> diamant(5)

              #
            # # #
          # # # # #
        # # # # # # #
      # # # # # # # # #
        # # # # # # #
          # # # # #
            # # #
              #
