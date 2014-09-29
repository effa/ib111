# Cvičení 2: Jednoduché výpočty

## Součet čísel 1 .. N

    def soucet(n): ...

    >>> soucet(4)
    10
    >>> soucet(1)
    1
    >>> soucet(10)
    55


## Faktoriál

    def faktorial(n): ...

    >>> faktorial(4)
    24
    >>> faktorial(7)
    5040
    >>> faktorial(0)
    1

## Ciferný součet

    def ciferny_soucet(n): ...

    >>> ciferny_soucet(157)
    13

## Test prvočíselnosti

    def je_prvocislo(n): ...

    >>> je_prvocislo(17)
    True

## Výpis prvočísel

    def prvocisla(kolik): ...

    >>> prvocisla(8)
    2 3 5 7 11 13 17 19

## Rozklad na součin prvočísel

    def rozklad(n): ...

    >>> rozklad(252)
    2 ^ 2
    3 ^ 2
    7 ^ 1

## Největší společný dělitel

    def nsd(a, b): ...

    >>> nsd(6, 8)
    2
    >>> nsd(15, 8)
    1
    >>> nsd(504, 180)
    36

## Nejmenší společný násobek

    def nsn(a,b): ...

    >>> nsn(6, 8)
    24
    >>> nsn(504, 180)
    2520

## Číselné řady

Napište funkci pro výpočet sinu zadaného úhlu (v radiánech) pomocí
[Taylerovy řady](http://cs.wikipedia.org/wiki/Taylorova_%C5%99ada)
(sekce Příklady Taylorova rozvoje: sin x) s přesností na tisíciny.

    def sinus(x): ...

    >>> sinus(1.2)
    0.932
    >>> sinus(0)
    0.0
    >>> sinus(pi/4)
    0.707

## Bonusové příklady

* převod čísla z desítkové soustavy do dvojkové soustavy
* převod čísla z dvojkové soustavy do desítkové soustavy
* převod čísla z desítkové do jiné soustavy obecně (soustava, do které
  převádíme, bude zadána řetězcem znaků, které používá, např.
  "0123456789ABCDEF")

