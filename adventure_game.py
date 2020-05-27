import random

import time

enemy = ["pirate", "dragon", "wizard", "were wolf", "vampire"]
villan = random.choice(enemy)


def print_pause(message):
    print(message)
    time.sleep(2)


def start_game():
    intro()
    inventory = []
    choose_path(villan, inventory)


def intro():
    print_pause("You find yourself standing in an open field")
    print_pause("with grass and yellow wild flowers")
    print_pause("You come to crossroad, one path leads to a house")
    print_pause("and other leads to a dark cave")
    print_pause(f"Rumour has it that a wicked {villan} around here")
    print_pause("and has been terrifying the near by village ")
    print()


def choose_path(villan, inventory):
    path = " "
    while path != '1' and path != '2':
        path = input("where would you like to go?\n1. House \n2. Cave\n")
    if path == '1':
        house(villan, inventory)
    else:
        cave(villan, inventory)


def attack_choice():
    choice = ""
    while choice != '1' and choice != '2':
        choice = input("Would you like to (1) Run away or (2) Fight ?\n")
    return choice


def attacking_without_sword(villan, inventory):
    print_pause("You feel a bit underprepared for this.")
    print_pause("What with only having a tiny dagger")
    y = attack_choice()
    if y == '1':
        print_pause("You run to cross road\n")
        choose_path(villan, inventory)
    else:
        print_pause("You do your best.....")
        print_pause("But your dagger is no much for everything")
        print_pause("You have been defeated !")


def attacking_with_sword(villan, inventory):
    x = attack_choice()
    if x == '1':
        print_pause("You run back to crossroad.")
        print_pause(" Luckily you don't seem to have been followed")
        print()
        choose_path(villan, inventory)

    else:
        print_pause(f"As the {villan} moves to attack.You unsheath your sword")
        print_pause("The sword of Alexander shines brightly in your hand")
        print_pause("You both have immense fight")

        my_health = random.randint(1, 5)
        enemy_health = random.randint(1, 5)

        if my_health >= enemy_health:
            print_pause(f"Great! you defeated the wicked {villan}")
            print_pause(f"You have rid the town of {villan}")
            print_pause("You are victorious !")
        else:
            print_pause("You try your best....")
            print_pause("But you have been defeated !")
            print_pause("Please try again !")


def ask_playagain():
    decission = " "
    while decission != 'yes' and decission != 'no':
        decission = input("Would you like to play again?(yes or no)\n").lower()
    if decission == 'yes':
        print_pause("Excellent restarting game !")
        print()
        start_game()
    else:
        print_pause("Thanks for playing , see you next time")


def cave(villan, inventory):
    print_pause("\nYou peer cautiously into cave")
    if "sword" in inventory:
        print_pause("You have been here before"" and gotten all good stuff")
        print_pause("Its just an empty cave now.")

    else:
        print_pause("It turns out to be only a very small cave")
        print_pause("Your eye catches a glint of metal behind a rock.\n")
        print_pause("You have found magical sword of Alexander!")
        print_pause("You discard your old dagger and take the sword with you.")
        inventory.append("sword")

    print_pause("You walk back out to crossroad\n")
    choose_path(villan, inventory)


def house(villan, inventory):

    print_pause("\nYou approach the door of house.")
    print_pause("You are about to knock,")
    print_pause(f"when the door opens and steps out a {villan}")
    print_pause(f"Eep! This is the {villan}'s house !")
    print_pause(f"The {villan} attacks you !")

    if "sword" in inventory:
        attacking_with_sword(villan, inventory)

    else:
        attacking_without_sword(villan, inventory)
    print()

    ask_playagain()


start_game()
