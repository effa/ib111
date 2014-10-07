# Domácí úloha 2: Člověče, nezlob se

**soft deadline: neděle 12. 10.**
(hard deadline: neděle 19. 10.)

* Odevzdejte jediný soubor `uloha02.py` s definicemi požadovaných funkcí.
* Funkce pojmenujte stejně, jako je v zadání.
* Pokud budete psát všechen kód do jediné funkce, snadno se v tom ztratíte.
  Úlohu si proto rozložte, napište si vhodné pomocné funkce.
* Pište přehledný kód, používejte přiléhavá jména proměnných a funkcí.
* Případné složitější konstrukce opatřete komentářem.
* Nepoužívejte diakritiku (ani v komentářích).
* Pracujte samostatně, za opisování je -30 bodů.


## Simulátor hry

Napište funkci pro simulaci zjednodušené verze hry "Člověče, nezlob se" pro
jednoho hráče.

* Hraje se na jednorozměrném hracím plánu, jehož délka je určena prvním
  argumentem funkce (`pocet_poli`). Pole jsou číslována od 1 do `pocet_poli`.
* Hráč začíná na 1. poli, úkolem je dostat se na poslední pole.
* V každém kole se háže kostkou, v lichém kole čtyřstěnnou (1-4) a v sudém
  osmistěnnou (1-8). Pokud padne nejvyšší možné číslo (4 u čtyřstěnné, 8 u
  osmistěnné kostky), házení se opakuje (tak dlouho, dokud nepadne něco jiného)
  a tyto hody se sčítají.
* Figurka se posune o tolik polí, kolik padlo (výsledný součet), ale pouze v
  případě, že by se tím neocitla mimo hrací plán.
* Hra končí, když figurka dorazí přesně na poslední pole.

Funkce pro simulaci hry má také parametr `vypis`, který určuje, zda se má
průběh hry vypisovat. Návratovou hodnotou funkce je počet kol.

    >>> hra_clovece(20, vypis=True)
    kolo 1, hod: 2
    pozice: 3
    kolo 2, hod: 7
    pozice: 10
    kolo 3, hod: 4 4 1
    pozice: 19
    kolo 4, hod: 8 2
    pozice: 19
    kolo 5, hod: 2
    pozice: 19
    kolo 6, hod: 1
    pozice: 20
    Hra dokoncena v 6. kole


## Analýza hry

Napište funkci, která vypočítá průměrnou délku hry na plánu velikosti
`pocet_poli`. Počet pokusů, který se k výpočtu použije, je také parametrem
funkce. Funkce pro analýzu hry bude volat funkci `hra_clovece()` s parametrem
`vypis` nastaveným na `False`. Do řešení přiložte výpis průměrných délek her pro
plány o velikosti 1 &ndash; 50.

    >>> analyza_clovece(20, 1000)
    prumerny pocet kol: 9.791
    >>> analyza_clovece(2, 1000)
    prumerny pocet kol: 5.164
    >>> analyza_clovece(1, 5)
    prumerny pocet kol: 0.0

## Kostra řešení

```python
# simuluje hru "Clovece, nezlob se"
def hra_clovece(pocet_poli, vypis=True):
    pass


# vypocita prumerny pocet kol nutny k dohrani hry na planu
# o velikost pocet_poli
def analyza_clovece(pocet_poli, pocet_opakovani):
    pass


# pridejte kod pro vypis prumernych delek her na planech o velikostech 1-50,
# vzdy na zaklade 100 pokusu
```

Pokud si nejste úplně jistí, začněte radši jednodušším úkolem (např. bez
střídání kostek v lichém a sudém tahu, bez parametru pro výpis, ...) a až toto
dokončite, rozšiřujte řešení do plné podoby.
