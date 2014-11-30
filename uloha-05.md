# Domácí úloha 5: Zpracování textu

**soft deadline: neděle 7. 12.**
(hard deadline: neděle 14. 12.)


## Jména (4+ body)

S využítím souboru anglických křestních jmen `names.txt` (který obsahuje vždy 1
jméno na 1 řádku, jména mají velké pouze počáteční písmeno) implementujte
následující funkce:

```python
# vypise vsechna jmena, ktera obsahuji alespon 2 'i' a konci na 'ed'
def special_names():
    pass

# vypise jmena, ktere zacinaji a konci na zadana pismena
def names_by_letters(first_letter, last_letter):
    pass

# funkce pro nalezeni vhodneho jmena pro dite
def name_for_your_child():
    pass
```

Funkce `name_for_your_child()` pomůže interaktivně vybrat vhodné jméno
(případně více jmen) pro dítě pomocí několika otázek, např. první písmeno,
maximální délka jména, minimální počet samohlásek atp. Jako základ stačí 3 jednoduchá kritéria.
Za propracovanější verzi lze získat bonusové body.

Složitější regulární výrazy (nebo klidně i všechny) zapisujte ve VERBOSE formě
(viz podklady ke cvičení) a jednotlivé části výrazů dobře okomentujte.


## Zpracování HTML (8+ bodů)

Zpracujte tabulku o počtech obyvatel jednotlivých států z
[Wikipedie](http://en.wikipedia.org/wiki/List_of_countries_by_population)
(zde v
[souboru](http://www.fi.muni.cz/~xrihak1/python/List_of_countries_by_population.html))
do formátu, kde na jednom řádku je název státu a jeho počet obyvatel, oddělené
tabulátorem (`\t`). Výsledek uložte do souboru.

Dále napište funkci, která s využitím tohoto souboru umožní vypsat státy,
jejichž počet obyvatel leží v zadaném intervalu.

```python
def extract_info(input_name='List_of_countries_by_population.html',
                 output_name='population.txt'):
    pass

def countries_by_population(minimum, maximum):
    pass
```

```
>>> minimum = 2 * (10 ** 8)  # 200,000,000
>>> maximum = 10 ** 9      # 1,000,000,000
>>> countries_by_population(minimum, maximum)
317121000 United States
237641326 Indonesia
201032714 Brazil
```

Bonusové body můžete získat za funkci `info(country_name)`, která pro daný název
státu vypíše několik zajímavých údajů. Za tímto účelem můžete samozřejmě
využívat i další webové stránky.


## Imitace textu (8+ bodů)

Napište funkci `text_generation(text_file, word_count, output_file=None)`,
která provede analýzu
četnosti slov a dvojic slov (tj. která slova následují po kterých slovech a jak
často) a využijte těchto informací k vygenerování textu o dané délce.
Pokud je specifikovaný výstupní soubor, zapíše vygenerovaný text do něj. V
opačném případě ho vypíše na standardní výstup.

```
>>> text_generation("krakatit.txt", 30)

S hrůzou prstzy. Potom vyslechl domovnici; zvěděl sice na tom, co budeš sebou
výsměšná a rudé, jako vždy. A nám ztratil. Ovšem něco vyžvanil, uvědomoval
si dokotři stopy jejího nitra.
```

Existuje mnoho způsobů jak k tomu přistoupit, jedna z možností je tato: vyjdete
z analýzy počtu slov v textu (kterou jsme kdysi dělali). Nezapomeňte, že text k
analýze by se měl načítat ze souboru. Nyní nás ale nebude zajímat počet výskytů
daného slova v textu, ale to, která slova po něm následují (a jak často). Pro
každé slovo si proto zapamatujeme všechna slova, která po něm následují (v
jednodušším případě seznamem slov; efektivnější, ale komplikovanější možností
je pomocí dalšího - vnořeného - slovníku udávajícího frekvence slov, která po
tomto následují). Takto vytvořená slovníková struktura už umožňuje snadno
imitovat původní text: začnete libovolným slovem a pak opakovaně vybíráte
náhodně jednoho z jeho následníků. Za sofistikovanější řešení můžete získat
bonusové body.


## Důležité poznámky

* Odevzdejte jediný soubor `uloha05.py`, s definicemi funkcí uvedenými v zadání
  (dodržte názvy funkcí a parametrů kvůli částečně automatickému opravování úlohy).
* Nepoužívejte diakritiku (ani v komentářích).
* Každý regulární výraz (nebo alespoň ty složitější) zapisujte ve VERBOSE formě
  (viz podklady ke cvičení) a jednotlivé části výrazů dobře okomentujte.
* Pracujte samostatně, za opisování je -30 bodů.
