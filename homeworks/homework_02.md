# Domácí úloha 2
* Termín odevzdání: soft deadline je 15.10., ale odevzdávat můžete až do 22.10.
* Za úlohu můžete dostat až 25 bodů
* Budete odevzdávat jeden soubor `homework_02.py` s funkcemi pojmenovanými podle zadání
* Odevzdávárna  [IS / Student / FI:IB111 / Odevzdávárny / Domácí úloha 2](https://is.muni.cz/auth/el/1433/podzim2017/IB111/ode/s03/ode_hw2/)
* Funkce a proměnné pojmenovávejte výstižně, ale stručně
* Snažte se držet společného jazyka programátorů (angličtiny) jak v kódu, tak i ve výpisu
* Komentáře jsou jako sůl. Je potřeba, ale neobraťte tam celou solničku ;)
* Pracujte samostatně

## Hadi a žebříky
Vaším úkolem bude naprogramovat zjednodušenou verzi Hadů a žebříků ([Snakes and Ladders](https://en.wikipedia.org/wiki/Snakes_and_Ladders)).

### Pravidla:
* hraje se na hracím plánu délky `length`
* figurka začíná na jednom z konců
* háže se standardní šestistěnnou koskou
* pokud padne 6, tak se háže znovu (stále se počítá jako jeden tah)
* figurka se posune o součet hodů, ale zůstane stát pokud by se dostala za cíl (tj. musí se trefit přesně)
* každé `n`-té políčko je had, který figurku posune o `k` políček zpět (pouze jednou za tah)

### Poznámky
* pro délku hracího plánu `length < 2` nebo pro `n <= 0` funkci skončete a vypište smysluplnou hlášku

### Kostra
```
from random import randint, random

def game(length, n, k, output = True):
    pass
  
def game_analysis(length, n, k, count):
    pass
    
def game_average_length(count):
    pass
```

### Úkol
* funkce `game` nasimuluje jednu hru a vrací počet tahů, pokud je parametr `output` roven `True`, pak funkce průběžě vypisuje stav hry (viz níže)
* funkce `game_analysis` nasimuluje `count` her se zadanými parametry a vrací průměrný počet tahů
* funkce `game_average_length` nasimuluje `count` her pro kombinace parametrů `length` 10 - 20, `n` 2 - 4 a `k` 1 - 3 a pro každou kombinaci vypíše průměrný počet tahů v nějakém pěkném formátu

### Ukázkový výpis funkce `game`
```
>>> game(20, 4, 2)
Turn 1: 3 -> new position: 3
Turn 2: 1 -> new position: 2
Turn 3: 6 3 -> new position: 11
Turn 4: 5 -> new position: 14
Turn 5: 4 -> new position: 18
Turn 6: 3 -> new position: 18
Turn 7: 2 -> new position: 20
Game finished at turn 7
```

### Bonus
Za tuto úlohu bude možné získat nějaké bonusové body za úpravu první funkce, aby stav hry znázorňovala graficky (pomocí různých znaků).
