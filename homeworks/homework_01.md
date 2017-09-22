# Domácí úloha 1

* Termín odevzdání: neděle 1. 10 (soft deadline). Pro případ nouze bude odevzdávárna otevřená až do 8. 10. (hard deadline). Později už úlohu odevzdat nepůjde.
* Úloha se skládá z 5 příkladů, za každý můžete získat 5 bodů, takže celkem až 25 bodů.
* Odevzdejte jediný soubor `homework_01.py` s implementací požadovaných funkcí. Funkce pojmenujte stejně jako v zadání.
* Můžete použít připravenou [kostru programu](`homework_01.py`).
* Odevzdávárna: [IS / Student / FI:IB111 / Odevzdávárny / Domácí úloha 1](https://is.muni.cz/auth/el/1433/podzim2017/IB111/ode/s03/ode_hw1).
* Pište přehledný kód, používejte vhodná jména proměnných a případné složitější konstrukce opatřete komentářem.
* Nepoužívejte diakritiku (ani v komentářích).
* Pokud se vám nějakou úlohu nepodaří úplně vyřešit, tak nezoufejte, zkuste si zadaný problém zjednodušit a vyřešit tento zjednodušený problém. Do komentáře pak napište, v čem zjednodušení spočívá (např. "Funguje pouze pro dvojciferna cisla n.") a úplně nejlépe zkuste taky popsat překážku, kvůli které se vám nedaří vyřešit původní problém rozsahu.
* Úlohy vypracovávejte zcela samostatně.
* Řešení domácích úloh si užívejte :-)


## Alternující posloupnost

Napište funkci `alternating_sequence(n, a, b)`,
která vypíše prvních `n` členů posloupnosti,
ve které se střídají násobky čísla `a` s konstantní hodnotou `b`.

```
def alternating_sequence(n, a, b): ...

>>> alternating_sequence(10, 7, 1)
7 1 14 1 21 1 28 1 35 1
```

## Vybraná čísla

Napište funkci `selected_numbers(a, b)`,
která vypíše všechna dvojciferná čísla,
jejichž první cifra je dělitelná číslem `a`
a druhá cifra je dělitelná číslem `b`:

```
def selected_numbers(a, b): ...

>>> selected_numbers(3, 5)
30 35 60 65 90 95
```

Tip: Pro spojení dvou podmínek, které musí platit současně, použijte klíčové
slovo `and`.

## Skorodělitelé

Napište funkci `near_divisors(n)`, která vypíše všechna kladná čísla,
která sice nejsou dělitelé čísla `n`,
ale od některého dělitele čísla `n` se liší pouze o 1.

```
def near_divisors(n): ...

>>> near_divisors(20)
3 6 9 11 19 21
```

Tip: Pro spojení dvou podmínek, ze kterých stačí, aby platila alespoň jedna, použijte klíčové slovo `or`.
     Dejte si pozor na pořadí vyhodnocování u složitějších aritmetických a logických výrazů a využijte závorek k jeho ovlivnění.

## Pruhovaný obdélník

Funkce `striped_rectangle(width, height)` vykreslí pomocí textové grafiky obdélník o zadaných rozměrech,
který bude mít znakově rozlišený okraj, liché řádky a sudé řádky.

```
def striped_rectangle(width, height): ...

>>> striped_rectangle(9, 6)
# # # # # # # # #
# - - - - - - - #
# ~ ~ ~ ~ ~ ~ ~ #
# - - - - - - - #
# ~ ~ ~ ~ ~ ~ ~ #
# # # # # # # # #
```



## Tabulka rozdílů

Funkce `differences_table(n)` vypíše tabulku s daným počtem řádků a sloupců (+ popisný řádek a sloupec),
kde v každé buňce se nachází absolutní rozdíl čísla řádku a čísla sloupce.
(Pro jednoduchost formátování klidně předpokládejte, že `n` je jednociferné.)


```
def differences_table(n): ...

>>> differences_table(5)
    1 2 3 4 5
    - - - - -
1 | 0 1 2 3 4
2 | 1 0 1 2 3
3 | 2 1 0 1 2
4 | 3 2 1 0 1
5 | 4 3 2 1 0
```
