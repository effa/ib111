def print_board(state):
    # state - reprezentace stavu hry
    # funkce vypise na obrazovku stav hry v nejake pekne forme
    # nic nevraci
    pass

def play(rows, columns, player1 = "human", player2 = "human"):
    # rows - pocet radku hraciho pole (nabyva hodnot >= 1)
    # columns - pocet sloupcu (nabyva hodnot >= 3)
    # player1 / player2 - urcuje, kdo jsou hraci, player1 zacina (nabyva hodnot "human", "computer")
    # vraci 0 pokud remiza, jinak cislo vyherce
    pass

def check_win(state):
    # state - reprezentace stavu hry
    # vraci cislo vyherce nebo 0 pokud nikdo nevyhral
    pass

def human_play(state, number):
    # state - reprezentace stavu hry
    # number - cislo hrace (1 nebo 2)
    # vraci cislo sloupce, ktery hrac vybral
    pass
    
def computer_play(state, number):
    # state - reprezentace stavu hry
    # number - cislo hrace (1 nebo 2)
    # vraci cislo sloupce, ktery pocitac vybral
    pass
