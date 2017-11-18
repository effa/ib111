# Domácí úloha 4: Objekty
* Termín odevzdání: neděle 3. 12 (soft deadline).
* Pro případ nouze bude odevzdávárna otevřená až do 10. 12. (hard deadline).
* Odevzdejte jediný soubor `homework_04.py` s implementací požadovaných metod a funkcí.
* Odevzdávárna:
  [IS / Student / FI:IB111 / Odevzdávárny / Domácí úloha 4](https://is.muni.cz/auth/el/1433/podzim2017/IB111/ode/s03/ode_hw4/)
* Pište přehledný kód, používejte vhodná jména proměnných, odstraňte duplicitní kód.
* Případné složitější konstrukce opatřete komentářem.
* Nepoužívejte diakritiku (ani v komentářích).
* Úlohu vypracujte zcela samostatně.
* Řešení domácí úlohy si užijte :-)

## Zadání

V souboru [members.txt](members.txt) jsou data o členech fakultního Spolku přátel severské zvěře.
O každém členovi evidujeme jeho jméno, rok narození a stupeň studia.
(O jménech můžete předpokládat, že jsou unikátní.)
Každý člen spolku, kromě jeho zakladatele, má právě jednoho mentora.
Např. řádek `Martin->Tom` vyjadřuje, že Martin je Tomův mentor.
Mentorství tvoří stromovou hierarchii (tj. nejsou tam cykly).
Poslední částí souboru jsou týmy pro jednotlivé soutěže, které Spolek organizuje.
Každý tým má název a seznam členů.
Můžete předpokládat, že vstupní soubor má přesně takový formát jako ten ukázkový (netřeba ošetřovat prázdné řádky navíc a jiné odchylky od formátu).

Vaším úkolem je tento soubor načíst
a vytvořit reprezentaci jednotlivých členů (třída `Person`) a týmů (třída `Team`).
K reprezentaci kolekcí využijte slovníky mapující jména na objekty,
takže např. `people['Martin']` bude odkazovat na objekt třídy `Person` reprezentující Martina.
Každý objekt třídy `Person` má kromě jména, roku narození a stupně studia
také mentora a seznam svých mentorovaných (`mentees`).

S členy spolku a týmy pak budeme chtít např.
  najít nejdelší jméno,
  vykreslit strom mentorství,
  či vypsat přehled všech týmů (viz vzorový výstup níže).
Připravená kostra obsahuje popis všech požadovaných funkcí včetně vzorového chování
v tzv. dokumentačních řetězcích (uzavřené do trojitých uvozovek hned za hlavičkou funkce).

Některé funkce využívají pojmu *transitive mentors* a *transitive mentees*.
Pokud osoba A má mentora B, B má mentora C, C má mentora D a D žádného mentora nemá (tj. je to zakladatel), pak tranzitivními mentory osoby A jsou B, C i D.
A naopak, tranzitivními mentorovanými (*transitive mentees*) osoby D
jsou A, B, C (a všichni další mentorovaní těchto osob a jejich mentorovaní, atd.)


## Kostra
Vyjděte z [připravené kostry](homework_04.py), zachovejte hlavičky funkcí, dokumentační řetězce i testy.
Z kostry maže pouze zástupné `pass` a `TODO` značky -
ty ale mažte až poté, co danou metodu či funkci implementujete.
Pokud některou funkci zvládnete implementovat jen částečně (např. bude fungovat jen pro některé vstupy), tak `TODO` komentář v kódu ponechte a doplňte jej o popis, co už vaše funkce umí a co jí chybí k dokonalosti.

Kostra obsahuje funkci `main()`,
která načte soubor a volá implementované funkce pro načtená data,
a funkci `test()`, která ověří, že funkce fungují na ukázkových případech popsaných v dokumentačních řetězcích.
Odkomentováním volání funkce `test()` na posledním řádku si tak můžete ověřit,
jestli vaše implementace fungují aspoň na ukázkových případech.
(Pokud ne, tak značku `TODO` u takové funkce neodstraňujte.)
Podobně si zkontrolujte, zda výstup funkce `main()` odpovídá vzorovému výstupu níže.

## Bodování
Kostra obsahuje 4 metody a 18 funkcí k doplnění (označené pomocí `TODO`).
Za každou funkční metodu získáte 1 bod, za každou funkci 2 body.
Celkem tedy můžete získat až 40 bodů.
Podmínkou k získání plného počtu bodů je kromě funkčnosti také přehledný a čitelný kód.
Ověřte si i dodržovaní konvencí (jména proměnných, mezery) pomocí pylintu.

Pokud některé funkce nezvládnete implementovat,
zakomentujte před odevzdáním část metody `main` tak, aby byl soubor spustitelný.

## Sebehodnocení
Před odevzdáním doplňte na začátek souboru komentář s odhadem získaných bodů.
Vzhledem k tomu, že by počet bodů měl jít přímočaře spočítat z počtu
chybějících `TODO`, zkuste případnou odchylku stručně vysvětlit.


## Vzorový výstup
```
longest name: Dominika
founder: Martin
Martin (1991)
  Lukas (1991)
    Radka (1994)
      Anicka (1997)
      Dominika (1995)
      Tyna (1993)
      Viki (1995)
    Vlada (1991)
  Maara (1989)
    Jan (1993)
  Tom (1993)
    Honza (1995)
      Ondra (1997)
    Katka (1994)
transitive mentees of Lukas: 6
transitive mgr mentees of Lukas: 2
transitive mentors of Ondra: ['Honza', 'Tom', 'Martin']
person with most mentees: Radka
--------------
Team: InterLoS
--------------
Vlada (1991)
Jan (1993)
Radka (1994)
Katka (1994)
Dominika (1995)
--
median year of birth: 1994
most common degree: mgr
--------------
Team: InterSoB
--------------
Lukas (1991)
Tom (1993)
Radka (1994)
Dominika (1995)
--
median year of birth: 1993
most common degree: mgr
---------
Team: KSI
---------
Vlada (1991)
Honza (1995)
Dominika (1995)
Viki (1995)
Anicka (1997)
Ondra (1997)
--
median year of birth: 1995
most common degree: bc
--------------
Team: PoznejFI
--------------
Maara (1989)
Martin (1991)
Tom (1993)
Tyna (1993)
Anicka (1997)
--
median year of birth: 1993
most common degree: bc
common members of InterSoB and KSI: {'Dominika'}
common teams of Dominika and Vlada: {'InterLoS', 'KSI'}
```
