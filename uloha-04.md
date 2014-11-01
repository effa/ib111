# Domácí úloha 4: Jednorozměrné piškvorky

**soft deadline: neděle 9. 11.**
(hard deadline: neděle 16. 11.)

Vytvořte program hrající hru *Jednorozměrné piškvorky* proti uživateli. Tato
variace piškvorek se hraje na jednorozměrném hracím plánu o zadané velikosti,
tj. hrací plán je řada políček. Stejně jako u běžných piškvorek se hráči
střídají a dělají značky do zatím neobsazených políček, tentokrát však oba
hráči dělají křížky. Vyhrává hráč, který jako první vytvoří alespoň 3 křížky
vedle sebe. Nelze hrát na již obsazenou pozici ani se vzdát tahu.

## Zadání

Vaším úkolem je implementovat:

* Funkci `strategie(plan)`, která pro daný plán vrátí pozici optimálního
  tahu. Plán je reprezentován polem znaků `X` (křížek) a `_` (neobsazené
  pole).


    >>> plan = ['_', '_', '_', 'X', 'X', '_', '_', 'X']
    >>> strategie(plan)
    2


* Funkci `piskvorky(velikost_planu, zacina_hrac=True)`, která umožňuje hrát hru
  jednorozměřných piškvorek s počítačem. Můžete předpokládat, že zadaná
  velikost plánu je rozumná (alespoň 3 a méně než 50). Parametr `zacina_hrac`
  určuje, zda začíná hráč nebo počítač. Výpis průběhu hry by měl vypadat
  stejně, jako v následujících příkladech. Funkce kontroluje, zda jsou tahy
  zadané hráčem platné a pokud nejsou, vyzve ho k novému zadání. Pro hru
  počítače volejte výše uvedenou funkci `strategie(plan)`.

## Příklady hry

Příklad, v němž začíná hráč:

    >>> piskvorky(26, zacina_hrac=True)
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
             0         |         1         |     2

    Na tahu: hrac
    Zadej tah: 1

    X _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
             0         |         1         |     2

    Na tahu: pocitac
    Zahral na pozici: 4

    _ X _ _ X _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
             0         |         1         |     2

    Na tahu: hrac
    Zadej tah: 6

    _ X _ _ X _ X _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
             0         |         1         |     2

    Na tahu: pocitac
    Zahral na pozici: 5

    _ X _ _ X X X _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
             0         |         1         |     2

    Prohrál jsi!


Příklad s pokusem o neplatný tah, v němž začíná počítač:

    >>> piskvorky(15, zacina_hrac=False)

    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
             0         |    1

    Na tahu: pocitac
    Zahral na pozici: 0

    X _ _ _ _ _ _ _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
             0         |    1

    Na tahu: hrac
    Zadej tah: 20
    Neplatny tah, zadej jinou pozici.

    X _ _ _ _ _ _ _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
             0         |    1

    Na tahu: hrac
    Zadej tah: 0
    Neplatny tah, zadej jinou pozici.

    X _ _ _ _ _ _ _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
             0         |    1

    Na tahu: hrac
    Zadej tah: 3

    X _ _ X _ _ _ _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
             0         |    1

    Na tahu: pocitac
    Zahral na pozici: 6

    X _ _ X _ _ X _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
             0         |    1

    Na tahu: hrac
    Zadej tah: 1

    X X _ X _ _ X _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
             0         |    1

    Na tahu: pocitac
    Zahral na pozici: 2

    X X X X _ _ X _ _ _ _ _ _ _ _
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
             0         |    1

    Prohrál jsi!

## Bodování

Funkce `piskvorky(velikost_planu, zacina_hrac=True)` musí korektně provádět
hru hráče a počítače, kontrolovat zadané tahy hráče a určit výhru. Výpis se
musí shodovat s výše uvedenými ukázkami.

Základní variantou `strategie` je funkce, která dodržuje pravidla, ale jinak hraje
náhodně. Za takové řešení obdržíte až 15 bodů (při splnění všech požadavků na
funkci `piskvorky()`). Abyste získali 20 bodů, musí
program hrát alespoň trochu rozumně, např. když může jedním tahem
vyhrát, tak to udělá, a nenahrává na výhru, pokud se tomu lze vyhnout.
Pokud váš program bude hrát "inteligentně", získáte bonusové
body. Čím inteligentněji, tím více bodů.

V každém případě napiště do komentáře stručné vysvětlení, jak moc inteligentně
program hraje. Kvalita tohoto pohopisu je také důležitá.


## Několik tipů

*  Než začnete psát kód, rozmyslete si (nejlépe si i nakreslete) dekompozici
   problému na jednodušší funkce. Jinak se v tom ztratíte. Problém lze rozložit
   různě, příklady užitečných funckí: `vykresli_plan(plan)`, `vyhra(plan)`,
   `povoleny_tah(tah, plan)`, ale v průběhu řešení by vás pak měly napadnout
   ještě další. Kdykoliv zjistíte, že máte v programu duplicitní kód, zbavte se
   ho (např. právě pomocí nové pomocné funkce). A všechny funkce by měly zůstat
   dostatečně krátké a přehledné.
* Začněte variantou s náhodnými tahy, rozumnné chování přidejte až potom. Při
  dobré dekompozici by rozšiřování neměl být problém.
* Zkuste si tuto hru pákrát zahrát (s někým nebo i sami se sebou), pomůže vám
  to lépe pochopit, jak by měl počítač optimálně hrát.

## Důležité poznámky

* Odevzdejte jediný soubor `uloha04.py`, s definicemi funkcí `strategie(plan)`
  a `piskvorky(velikost_planu, zacina_hrac=True)` (a dalšími pomocnými funkcemi
  dle vaší dekompozice). Dodržte tyto názvy funkcí a parametrů (kvůli částečně
  automatickému opravování úlohy).
* Nepoužívejte diakritiku (ani v komentářích).
* Pracujte samostatně, za opisování je -30 bodů.
* Pro jistotu ještě jednou: dodržte kostru programu i výpis průběhu hry tak, jak
  je uvedené v zadání.
