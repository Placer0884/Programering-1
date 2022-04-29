import random

money = 200


while True:
    hero = 0
    villain = 0
    villain_strenght = 0
    hero_strenght = 0
    hero_team = []
    villain_team = []
    heroes = ["Ant man", "Black Panther", "The Flash", "Iron Man", "Hulk", "Thor", "Superman"]
    villains = ["Zimo", "Winter Solider", "Mysterio", "Ultron", "Steppenwolf", "Thanos", "Darkseid"]

    bet = ""



    for i in range (3):
        hero = random.randint(1, len(heroes)-1)

        hero_strenght += hero
        hero_team.append(heroes[hero])
        del heroes[hero]

        villain = random.randint(1, len(villains)-1)
        villain_strenght += villain
        villain_team.append(villains[villain])
        del villains[villain]




    print("In this battle:", end="\n\n")
    print("Heroes:")
    for i in range (3):
        print(hero_team[i], end="     ")

    print("\n\nVillains:")
    for i in range (3):
        print(villain_team[i], end="     ")
    print("\n")

    side_picking = True
    while side_picking:
        bet = input("Which side do you bet on?\n")
        if bet == "heroes" or bet == "Heroes" or bet == "Villains" or bet == "villains":
            break

    print("\n")

    betting = True
    while betting:
        print("You currently have:", money, "coins")
        betted_money = int(input("How much do you want to bet?"))
        try:
            if betted_money > money:
                print("\nYou do not have that money!!")
                print("Get a job and stop your gambling addiction!\n")
            else:
                break
        except:
            pass



    print("\n")

    if bet == "heroes" or bet == "Heroes" and hero_strenght > villain_strenght:
        print("The heroes won!")
        money += betted_money
        print("You now have:", money, "coins")

    elif bet == "villains" or bet == "Villains" and hero_strenght > villain_strenght:
        print("The villains won!")
        money += betted_money
        print("You now have:", money, "coins")

    elif hero_strenght > villain_strenght:
        print("It's a tie!")
    else:
        print("You lose")

    stop = input("")
