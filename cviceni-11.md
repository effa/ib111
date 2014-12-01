# Cvičení 11: Regulární výrazy

Zpracování textu, regulární výrazy, práce se soubory a s odkazy.

### Práce se soubory

```python
# otevreni souboru pro cteni
input_file = open("input.txt", "r")
# nacteni celeho obsahu souboru do retezce
content = input_file.read()
# nacteni souboru souboru jako seznam radku
lines = input_file.readlines()
# otevreni souboru pro zapis
output_file = open("output.txt", "w")
# zapis retezce do souboru
output_file.write("This sentence has five words.")
# uzavreni souboru
some_file.close()

# alternativni konstrukce with, ktera zajisti uzavreni souboru:
with open("input.txt", "r") as input_file:
    pass
```

### Řetězce

Několik dalších užitečných funkcí řetězců:

```
>>> '  jablko, hruska, pomeranc \n'.strip()
'jablko, hruska, pomeranc'
>>> 'jablko, hruska, pomeranc'.split(', ')
['jablko', 'hruska', 'pomeranc']
>>> 'jablko, hruska, pomeranc'.replace(',', ' -')
'jablko - hruska - pomeranc'
>>> 'jablko, hruska, pomeranc'.find('hruska')
8
>>> 'JAKUB'.title()
'Jakub'
```

Standarně má symbol `\` speciální význam, zapisujume pomocí něho speciální znaky
(např. `\n` pro nový řádek) nebo apostrofy, resp. uvozovky (`\'`, resp. `\"`).
Pokud potřebujeme, aby řetězec obsahoval zpětné lomítko, musíme ho zvojit:

```
>>> print 'zpetne lomitko vypada takto \\'
zpetne lomitko vypada takto \
>>> print 'novy\nradek'
novy
radek
```

Protože zpětná lomítka mají speciální význam také v regulárních výrazech (a
tedy jich obvykle obsahují hodně), vyhovovalo by nám více takové chování, kdy
by se zpětná lomítka v řetězci nijak neinterpretovala. Toho lze dosáhnout
přídáním znaku `r` těsně před samotný řetězec, např. `r'raw string with \'`.

```
>>> print r'zpetne lomitko vypada takto \'
zpetne lomitko vypada takto \
>>> print r'\\\\'
\\\\
>>> print r'\n'
\n
```

### Regulární výrazy

Jednoduchá validace:

```python
import re

# vraci True, pokud zadany retezec reprezentuje cele cislo, jinak False
def is_integer(string):
    return bool(re.search(r'^-?\d+$', string))

>>> is_integer('42')
True
>>> is_integer('-42')
True
>>> is_integer('1a2')
False
```

Hledání řádků ve velkém souboru, které něco splňují:

```python
import re

# vypise radky, ktere splnuji zadany vzor
def search_in_file(pattern, file_name):
    # nacteme vsechny radky do seznamu
    with open(file_name) as f:
        lines = f.read().split('\n')
    # prochazime radky a hledame shodu
    for line in lines:
        if re.search(pattern, line):
            print line

>>> search_in_file(r'^T.*m$', 'names.txt')
Tom
Tim
Tam
Tatum
```

Nalezení všech výskytů:

```python
# nalezeni vsech cisel v textu
>>> print re.findall(r'\d+', 'aaa 123 bb 1560 72 k')
['123', '1560', '72']
```

Skupiny (označíme pomocí závorek):

```python
>>> import re
>>> match = re.search(r"(\w+) (\w+)", "Isaac Newton, fyzik")
>>> match.group(0)
"Isaac Newton"
>>> match.group(1)
"Isaac"
>>> match.group(2)
"Newton"
```


Výchozí chování kvantifikátorů (`*` a `+`) je hladové, tj. snaží se toho
obsáhnout co nejvíce. Pokud potřebujeme opačné chování (pojmout toho co
nejméně), lze použít nehladové verze kvantifikátorů přídáním otazníku
(`*?` a `+?`).

```python
# najde vsechny texty v uvozovkach
def quotes(text):
    return re.findall(r'"(.*?)"', text)

>>> quotes('abc "def" ghij "klmno"')
['def', 'klmno']
```
Delší regulární výrazy začnou být nepřehledné, proto je dobré využít
víceřádkový zápis, v němž se všechny bílé znáky ignorují a můžete doplnit
komentáře.

```python
import re

ROMAN_NUMERAL_RE = re.compile(r"""
    ^
    M*                              # tisice (libovolny pocet)
    (C{0,3} | CD | DC{0,3} | CM)    # stovky (000 - 900)
    (X{0,3} | XL | LX{0,3} | XC)    # desitky (00 - 90)
    (I{0,3} | IV | VI{0,3} | IX)    # jednotky (0 - 9)
    $
    """, re.VERBOSE)

if ROMAN_NUMERAL_RE.search('CMIV'):
    print 'CMIV is a roman numeral'
```

Kromě `re.VERBOSE` existují i další příznaky, kterými můžete ovlivnit
interpreteaci regulárního výrazu. Pro nás bude důležitý příznak `re.DOTALL`,
který změní chování `.` tak, že bude matchovat i znak nového řádku. Další
příznaky viz
[https://docs.python.org/2/howto/regex.html#compilation-flags](https://docs.python.org/2/howto/regex.html#compilation-flags).


Pro vymýšlení a testování regulárních výrazů použijte
[http://pythex.org/](http://pythex.org/), je tam i stručný přehled základních
prvků regulárních výrazů.
Podrobnější informace najdete třeba v tomto
[cheatsheetu](https://cloud.github.com/downloads/tartley/python-regex-cheatsheet/cheatsheet.pdf)
nebo v [dokumentaci](http://docs.python.org/2/library/re.html).

### Práce s odkazy

```python
import urllib2

# stazeni html na dane adrese
def get_html(url):
    f = urllib2.urlopen(url)
    content = f.read()
    f.close()
    return content

# ziskani vsech nadpisu na dane strance
def get_headlines(url):
    text = get_html(url)
    headlines = re.findall(r'<h(\d)>(.*?)</h\d>', text)
    for level, headline in headlines:
        print level, headline

>>> URL_FI = "http://www.fi.muni.cz"
>>> get_headlines(URL_FI)
[('1', 'Fakulta informatiky Masarykovy univerzity'),
('2', 'Studenti a zamestnanci'), ... ]
```

Všimněte si použití nehladového kvantifikátoru `*?`, proč je to důležité?


## Jména

Stáhněte si
[seznam anglických jmen](https://github.com/effa/ib111/blob/master/names.txt).

Nejprve ho zpracujte tak, aby jména měla pouze první počáteční písmeno (JOHN
-> John) a seřaďte jména v souboru podle abecedy.

Nyní napište funkci, která vypíše všechna jména, která splňují zadaný vzor.
Pokud by vám to nešlo, podívejte se na výše uvedenou funkci
`search_in_file(pattern, file_name)`.

Pomocí této funkce najděte (v příkazové řádce) všechna jména, která:

* obsahují `oo`
* obsahují alespoň 3 znaky `o` (ne nutně po hned sobě)
* obsahují pouze samohlásky
* obsahují pouze souhlásky [stačí přidat jediný znak do předchozího vzoru]
* začínají na B nebo D a končí na w nebo z
* obsahují buď `inf` nebo `rec`
* kromě prvního a posledního písmene obsahují pouze samohlásky a mají přesně 5
  písmen
* začínají a končí na `A` a mají nejvýše 4 písmena
* \* začínají na N nebo M a obsahují alespoň 5 samohlásek
* \* kromě `a` můžou obsahovat nejvýše 2 jiná písmena, což ale můžou být jedině
  `l`, `m` nebo `n`


## Validace vstupu

Napište funkce pro rozpoznávání desetinných čísel a emailových adres (podobně
jako výše uvedená funkce `is_interger()`).


```python
>>> is_number('42.01')
True
>>> is_number('-42')
True
>>> is_number('2.b')
False
>>> is_number('42.')
False
```


```python
>>> is_email_address('chuck@gmail.com')
True
>>> is_email_address('chuck.gmail.com')
False
>>> is_email_address('chuck@gmail')
False
>>> is_email_address('@gmail.com')
False
```

## Skupiny (groups)

Načtěte seznam e-mailových adres ze souboru a vytvořte seznam dvojic (jméno,
doména), využijte funkci `match.group(n)` (viz výše).

```python
>>> print load_email_addresses(src='email-addresses.txt')
[('chuck', 'gmail.com'), ('novak123', 'seznam.cz'), ('jan.kral', 'mail.muni.cz')]
```

## Nehladové čtení

Napište funkci, která najde všechny obsahy závorek v textu (pozor na to, že
závorky mají v regulárních výrazech speciální význam, pokud chcete říct, že se
má někde vyskytovat závorka, musíte ji tedy escapovat pomocí `\`).

```python
>>> brackets('Text (prvni poznamka) a (druha poznamka).')
['prvni poznamka', 'druha poznamka']
```


## Zpracování HTML

### Odkazy

Napište funkci, která pro zadané URL vypíše všechny odkazy, které se na stránce
objevují.

### Wikipedia

Z tabulky o počtech obyvatel jednotlivých států z
[Wikipedie](http://en.wikipedia.org/wiki/List_of_countries_by_population)
(zde v
[souboru](http://www.fi.muni.cz/~xrihak1/python/List_of_countries_by_population.html))
získejte seznam všech států a vypište je seřazené abecedně.

Můžete se inspirovat následujícím kódem pro výpis řádků tabulky (v HTML).
Zejména upozorňuji na důležitý příznak `re.DOTALL`, který změní chování `.`
tak, aby matchovala i znak nového řádku.

```python
with open("List_of_countries_by_population.html") as f:
    text = f.read()
    table = re.search(r'<table class="wikitable sortable.*?>(.*?)</table>',
                      text, re.DOTALL).group(1)
    rows = re.findall(r'<tr>(.*?)</tr>', table, re.DOTALL)
    for row in rows[1:]:
        print row
```

Na tento příklad navážeme v 5. domácí úloze.

### Laboratoře na FI

Napište program, který ze stránky
[http://www.fi.muni.cz/research/laboratories/](http://www.fi.muni.cz/research/laboratories/)
vytáhne jména všech laboratoří a k nim příslušné kontakty a webové stránky.


## Další úlohy k procvičení

### Regulární výrazy

* regex golf: [https://regex.alf.nu/](https://regex.alf.nu/)
* regex crosswords: [http://regexcrossword.com/](http://regexcrossword.com/)
* sada úloh Regulární výrazy na [http://tutor.fi.muni.cz/](http://tutor.fi.muni.cz/).


### Zpracovaní CSV

Stáhněte si [soubor s informacemi o studentech](http://www.fi.muni.cz/~xrihak1/python/seznam_export_mut.csv)
a implementujte následující funkce.

```python
# Nacte studenty ze souboru a vypise jmena serazena podle abecedy
def students(src):
    pass

# Nacte studenty ze souboru 'src' a ulozi jejich jmena
# serazena podle abecedy do souboru 'dest'.
def save_students(src, dest):
    pass

# Vypise jmena studentu studujicich v danem semestru.
def students_by_semester(src, semester):
    pass

# Vypise pocty studentu podle studovanych oboru (nejlepe sestupne podle poctu)
def students_by_fields(src):
   pass
```

## Pokročilé úlohy

### Substituce

Využijte funkci `re.sub()` (viz dokumentace), třeba k nahrazení všech amerických dat v zadaném textu
českým formátem dat (např. `12/24/2014` na `24. 12. 2014`) nebo k odstranění
všech poznámek v závorkách.

### grep a sed

Pokud pracujete na Linuxu, vyzkoušejte si nástroje `grep` a `sed` (viz
manuálové stránky nebo tutoriály na webu).

### Teorie jazyků

Zjistěte, jaký je vztah mezi regulárními výrazy, regulárními gramatikami a
konečnými automaty.
