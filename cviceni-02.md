# Posloupnosti

## Výpis

    def vypis_vsechna(n): ...

    >>> vypis_vsechna(10)

    1 2 3 4 5 6 7 8 9 10

## Sudá čísla

    def vypis_suda(n): ...

    >>> vypis_suda(9)

    2 4 6 8

## Mocniny

    def mocniny(zaklad, n): ...

    >>> mocniny(2, 10)

    1 2 4 8 16 32 64 128 256 512

## Dělitelé

    def delitele(n): ...

    >>> delitele(14)

    1 2 7 14



## Fibonacci

    def fibonacci(n): ...

    >>> fibonacci(10)

    1 1 2 3 5 8 13 21 34 55

## Podposloupnosti

    def podposloupnosti(n): ...

    >>> podposloupnosti(10)

    1 1 2 1 2 3 1 2 3 4

# Textová grafika

## Čtverec

    def ctverec(n): ...

    >>> ctverec(5)

    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #

## Prázdny čtverec

    def prazdny_ctverec(n): ...

    >>> prazdny_ctverec(5)

    # # # # #
    # . . . #
    # . . . #
    # . . . #
    # # # # #

## Pyramida

    def pyramida(n): ...

    >>> pyramida(5)

            #
          # # #
        # # # # #
      # # # # # # #
    # # # # # # # # #

## Vnořené čtverce

    def vnorene_ctverce(n): ...

    >>> vnorene_ctverce(3)

    * * * * * * * * *
    *               *
    *   * * * * *   *
    *   *       *   *
    *   *   *   *   *
    *   *       *   *
    *   * * * * *   *
    *               *
    * * * * * * * * *


## Šachovnice

    def sachovnice(n): ...

    >>> sachovnice(5)

    .#.#.
    #.#.#
    .#.#.
    #.#.#
    .#.#.

## Velká šachovnice


    def velka_sachovnice(celkova_velikost, velikost_policka): ...

    >>> velka_sachovnice(5, 2)

    ..##..##..
    ..##..##..
    ##..##..##
    ##..##..##
    ..##..##..
    ..##..##..
    ##..##..##
    ##..##..##
    ..##..##..
    ..##..##..
