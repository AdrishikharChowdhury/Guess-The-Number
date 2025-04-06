import random
from gamemodes import choose_game_mode,single_player,two_player
from game_logic import difficulty

def main():
    start, end, turns = difficulty()
    target = random.randint(start, end)
    mode = choose_game_mode()
    
    if mode == 1:
        win = single_player(turns, target)
        if not win:
            print("You lost the game.")
    elif mode == 2:
        two_player(turns, target)
    else:
        print("Invalid mode. Try again.")
    
    print("===== GAME OVER =====")

if __name__ == "__main__":
    main()