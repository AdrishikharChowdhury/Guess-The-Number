from game_logic import get_valid_input,guesser

def choose_game_mode():
    print("Choose game mode:")
    print("1. Single Player\n2. Two Player")
    while True:
        try:
            return int(input("Your choice: "))
        except ValueError:
            print("Invalid input! Please enter 1 or 2.")

def single_player(turns, target):
    name = input("Enter your name player: ")
    while turns > 0:
        x = get_valid_input("Enter the number to guess or Quit: ")
        if x == "quit":
            return False
        elif x is None:
            continue
        if guesser(name, x, target) == False:
            return True
        turns -= 1
        print("Turns left:", turns)
    print(f"Out of turns! The correct number was {target}")
    return False

def two_player(turns, target):
    name1 = input("Enter your name player 1: ")
    name2 = input("Enter your name player 2: ")
    while turns > 0:
        for name in [name1, name2]:
            x = get_valid_input(f"{name}, enter the number to guess or Quit: ")
            if x == "quit":
                winner = name2 if name == name1 else name1
                print(f"{name} quit the game. {winner} wins!")
                return None
            elif x is None:
                continue
            if guesser(name, x, target) == False:
                loser = name2 if name == name1 else name1
                print(f"{loser} lost. Better luck next time!")
                return True
        turns -= 1
        print("Turns left:", turns)
    print(f"Both players lost! The correct number was {target}")
    return False