# Domácí úloha 3
* soft deadline je 12. 11., nejpozději však odevzdávejte do 19. 11.
* úloha je za 30 bodů
* odevzdávejte jeden soubor pojmenovaý `homework_03.py`
* odevzdávárna [IS / Student / FI:IB111 / Odevzdávárny / Domácí úloha 3](https://is.muni.cz/auth/el/1433/podzim2017/IB111/ode/s03/ode_hw3/)
* nezapomeňte program psát pěkně, hezky dělit na funkce a rozumně komentovat

## Connect four
Tentokrát budete programovat [Connect four](https://cs.wikipedia.org/wiki/Cestovní_piškvorky) (také známé jako padající nebo cestovní piškvorky).

### Pravidla
Hru hrají dva hráči, kteří střídavě do hracího pole umisťují svoje hrací kameny (v našem případě označené X a O). Hráč, který dostane 4 své hrací kameny do řady, sloupce nebo diagonály vyhrál. Hráči ovšem vybírají pouze sloupec, do kterého kámen umístí a ten "spadne" na nejnižší prázdné místo v daném sloupci. Pokud je hrací pole zaplněné a žádný z hráčů nevyhrál, nastává remíza.

### Poznamky
* herní pole si reprezentujte jako pole polí po řádcích
* pro lidského hráče vypisujte nějaký dotaz na zadání sloupce
* pro počítačového hráče nejdříve implementujte strategii, která hraje náhodně, lepší můžete udělat později

### Kostra
* [kostra](homework_03.py)
* v kostře máte předdefinované hlavičky několika funkcí, ale určitě můžete (a měli byste) si dělat i nějaké pomocné funkce
* nemusíte se omezovat na `human_play` a `computer_play`, můžete si naprogramovat i další (např. `better_computer_play`)

### Příklad výpisu stavu hry
```
  X
  X   O
  O X O
_ _ _ _
1 2 3 4
```

### Bonus
Bonusem k této úloze na naimplementovat nějakou jinou než náhodnou strategii. Funkci se strategií pojmenujte `bonus_play` a stejně jako ostatní funkce pro hráče bude brát stav hry, číslo hráče a bude vracet číslo sloupce.

Bonus pro tuto úlohu je zajímavý tím, že část bonusových bodů dostanete za samotnou implementaci a část soutěžením se strategiemi ostatních. Vyhodnocení soutěžní části si potom uděláme na cvičení po hard deadlinu.
