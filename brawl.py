import random

P1name = input("Player 1 name?: ")
P2name = input("Player 2 name?: ")

P1life = 10
P2life = 10
P1wins = 0
P2wins = 0
round = 0
while True :
    while True :
        round += 1
        print(f"Round {round}")
        P1dice = random.randint(1,6)
        P2dice = random.randint(1,6)
        print(f"{P1name} rolls {P1dice}")
        print(f"{P2name} rolls {P2dice}")
        if P1dice == P2dice :
            print("Tie!")
        elif P1dice > P2dice :
            P2life -= P1dice - P2dice
            print(f"{P1name} wins")
            print(f"{P2name} takes {P1dice - P2dice} damage and now has {P2life} left")
        else :
            P1life -= P2dice - P1dice
            print(f"{P2name} wins")
            print(f"{P1name} takes {P2dice - P1dice} damage and now has {P1life} left")
        if P1life < 1 :
            print(f"{P1name} loses!")
            P2wins += 1
            break
        elif P2life < 1 :
            print(f"{P2name} loses!")
            P1wins += 1
            break
    print(f"{P1name}: {P1wins}  {P2name}: {P2wins}")
    playagain = input("Do you want to play agian? (y/n) ")
    if "n" in playagain.lower() :
        break
    if "y" in playagain.lower() :
        round = 0
        P1life = 10
        P2life = 10