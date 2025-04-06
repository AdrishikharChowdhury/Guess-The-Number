def get_valid_input(prompt):
    x = input(prompt)
    if x.lower() == "quit":
        return "quit"
    try:
        return int(x)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return None

def guesser(name,x,target):
    if x==target:
        print(f"{name} won.You have guessed the correct number:\nAns: {target}")
        return False
    elif x<target:
        print(f"{name} you have entered a small number.Guess bigger number: ")
    else:
        print(f"{name} you have guessed big number.Guess smaller number: ")

def difficulty():
    print("Enter the game difficulty:")
    print("1.Easy\n2.Medium\n3.Hard\n4.Nightmare")
    while True:
        try:
            ch = int(input("Your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue
        match(ch):
            case 1:
                print("Chosen Difficulty: Easy")
                print("No. of turns: ",15)
                return 1,50,14
            case 2:
                print("Chosen Difficulty: Medium")
                print("No. of turns: ",12)
                return 1,100,12
            case 3:
                print("Chosen Difficulty: Hard")
                print("No. of turns: ",10)
                return 1,500,10
            case 4:
                print("Chosen Difficulty: Nightmare")
                print("No. of turns: ",8)
                return 1,1000,8
            case _:
                print("Wrong Input!!!!Try Again")