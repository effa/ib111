# Cvičení 1

## Základy Pythonu

### Čísla


```python
>>> 2 * 5
10
>>> 10 / 3
3
>>> 10.0 / 3
3.3333333333333335
```

### Proměnné

    >>> x = 2
    >>> y = 5
    >>> x * y
    10

### Podmínka

    if x > 10:
        print 'vetsi nez 10'
    else:
        print 'mensi nez 10'

### Cyklus

    for cislo in range(4):
        print cislo




TODO: promenna, vyraz, podminka, cyklus, funkce (demo nebo odkaza na online tutora),
mozna odkaz na zaklady Pythonu (stejne to budu ukazovat)


TODO: odkaz na uvodni seznamovaci program na PythonTutorovi

### Opakování
Pomocí for cyklu napište 100 krát větu *Na cviceni se chodi vcas*.

Pak napište funkci, která umožní výpis libovolné věty libovolněkrát.

    def opakuj(veta, kolikrat):
        ...

    >>> opakuj('Hello!', 4)
    Hello!
    Hello!
    Hello!
    Hello!


## Želví grafika


TODO: dve ukazky (shell, funkce, oboje kriz) a odkaz na tutorial

Nejprve si zkuste nejaké jednoduché obrázky jako trojúhelník, čtverec nebo domeček.

Pro další obrázky si už vždy napište obecnou funkci.

### Pětiúhelníky

    def petiuhelnik(delka_strany):
        ...

    >>> petiuhelnik(50)

![Pětiúhelník](img/petiuhelnik.png)

### Mnohoúhelníky

    def mnohouhelnik(n, delka_strany):
        ...

    >>> mnohouhelnik(3, 70)
    >>> mnohouhelnik(4, 60)
    ...

![Mnohoúhelníky](img/mnohouhelniky.png)

### Hvěždy

    def hvezda(n):
        ...

    >>> hvezda(?)

![Hvězdy](img/hvezdy.png)

### Diamant

    def diamant(n):
        ...

    >>> ...

![Diamant](img/diamant.png)

### Spirála

    def spirala(?):
        ...

    >>> ...

![Spirála](img/spirala.png)

