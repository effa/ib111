# Cvičení 5: Řetězce a seznamy

▶ [Seznamy v Pythonu](https://developers.google.com/edu/python/lists)

▶ [Řetězce v Pythonu](https://developers.google.com/edu/python/strings)

## Seznamy

Rozhodněte, jak se v konzoli vyhodnotí (nebo jaké změny provedou) následující
příkazy, a vyzkoušejte si, že to tak opravdu je:

    >>> s = [7, 5, 8, 5, 9]
    >>> s[0]
    >>> s[2]
    >>> s[-1]

    >>> s.append(2)
    >>> s
    >>> s[1] = 10
    >>> s
    >>> x = s
    >>> x[0] = 20
    >>> x
    >>> s

    >>> s[1:3]
    >>> s[1:-1]
    >>> s[:4]

    >>> len(s)
    >>> min(s)
    >>> max(s)
    >>> sum(s)
    >>> 8 in s
    >>> 4 in s

    >>> range(10)
    >>> range(1, 10)
    >>> range(1, 10, 2)

## Maximum, součet, prohledávání

Napište ekvivalenty operací `max`, `sum` a `in` (s použitím pouze
základních operací nad seznamy).

    >>> maximum([6, 5, 11, 8])
    11
    >>> soucet([6, 5, 11, 8])
    30
    >>> prohledavani(5, [6, 5, 11, 8])
    True
    >>> prohledavani(4, [6, 5, 11, 8])
    False

## Řetězce

Rozhodněte, jak se v konzoli vyhodnotí (nebo jaké změny provedou) následující
příkazy, a vyzkoušejte si, že to tak opravdu je:

    >>> s = 'velbloud'
    >>> s[0]
    >>> s[2]
    >>> s[-1]
    >>> len(s)
    >>> s[1:3]
    >>> s[1:-1]
    >>> s[:4]
    >>> 'b' in s

    >>> s[3] = 'k'
    >>> s[:3] + 'k' + s[3:]
    >>> s
    >>> x = s + 'i'
    >>> x
    >>> s

    >>> 'petr' + 'klic'
    >>> 'kos' * 3
    >>> 3 * 'pra' + 'babicka'

    >>> ord('a')
    >>> ord('b')
    >>> chr(99)
    >>> chr(ord('x') + 1)
    >>> ord('e') - ord('a')
    >>> chr((ord('z') + 3 - ord('a')) % 26 + ord('a'))

    >>> 'Zelva'.upper()
    >>> 'Zelva'.lower()

## Prokládání

Napište funkci, která mezi písmena daného textu vloží libovolný text.

    def prokladani(text, vycpavka):
        pass

    >>> prokladani('pampeliska', 'XX')
    'pXXaXXmXXpXXeXXlXXiXXsXXkXXa'

## Caesarova šifra

Napište funkci, která zašifruje text tak, že posune všechna jeho písmena v abecedě o `n` dopředu
(cyklicky), můžete se inspirovat [popisem Caesarovy šifry](http://cs.wikipedia.org/wiki/Caesarova_%C5%A1ifra).

    def caesar(text, klic):
        pass

    >>> caesar('zirafa', 3)
    'cludid'

## Vigenèrova šifra

Napište funkci, která zašifruje text podle předem daného klíče. Pro posun písmen zdrojového textu
se postupně používají písmena z klíče: 'a' posouvá o 0, 'b' o 1, ... 'z' o 25.  Pokud je klíč kratší než zdrojový text, jsou použita písmena
z klíče opět od začátku. Můžete se inspirovat popisem [Vigenèrovy šifry](http://cs.wikipedia.org/wiki/Vigen%C3%A8rova_%C5%A1ifra).

    def vigenere(text, klic):
        pass

    >>> vigenere('pampeliska', 'klic')
    'zlurowquul'


## Prohazovací šifra

Napište funkci, která zašifruje text tak, že prohází jeho písmana ob daný počet
(tj. zašifrované slovo se pak dešifruje čtením ob 'n').

    def prohazej(text, n):
        pass

    >>> prohazej('heslojeprase', 3)
    'horejaseslpe'


## Víceřádkové transpozice

Napište funkce `schody()`, `sikmo()` a `cikcak()`, které vypíší předaný text
podle následujících vzorů:

    >>> schody("OPILECDOSELDOMU", 3)
    OPI
       LEC
          DOS
             ELD
                OMU

    >>> sikmo("OPILECDOSELDOMU", 3)
    O     L     D     E     O
      P     E     O     L     M
        I     C     S     D     U

    >>> cikcak("OPILECDOSELDOMU", 3)
    O       E       S       O
      P   L   C   O   E   D   M
        I       D       L       U

## Dešifrování

Napište k předchozím šifrám (prokládání, Caesarova šifra, Vigenèrova šifra,
prohazovací šifra) funkce, které zašifrovaný text dešifrují.


## Bonusové příklady

* frekvenční analýza textu
  - analýza písmen: kolikrát se které písmeno vyskytuje v zadaném řetězci
  - analýza slov: kolikrát se zadané slovo vyskytuje v zadaném řetězci
* převod Morseovky na text (a obráceně)
* dále viz [Rozcestník (Zdroje úloh k procvičkování)][2]
[2]: https://github.com/effa/ib111#zdroje-%C3%BAloh-k-procvi%C4%8Den%C3%AD
