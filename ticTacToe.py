N = 3
def empty_plan():
    return [[0 for i in range(N)]
            for j in range(N)]
    

def determine_winner(plan):
    for i in range(N):
        all_same = True
        for j in range(N):
            if plan[i][j] != plan[i][0]:
                all_same = False
        if all_same and plan[i][0] != 0:
            return plan[i][0]
            
        all_same = True
        for j in range(N):
            if plan[j][i] != plan[0][i]:
                all_same = False
        if all_same and plan[0][i] != 0:
            return plan[0][i]
    return 0


def print_plan(plan):
    symbol = {0: ".", 1: "X", 2: "O"}
    for i in range(N):
        for j in range(N):
            print(symbol[plan[i][j]], end=" ")
        print()
    
    
def play():
    plan = empty_plan()
    player = 1
    while determine_winner(plan) == 0:
        print_plan(plan)
        move = input("Player "+str(player)+" move:")
        x, y = list(map(int, move.split(" ")))
        plan[y-1][x-1] = player
        player = 3 - player
    print_plan(plan)
    print("Player "+str(determine_winner(plan))+" wins.")

        
play()
