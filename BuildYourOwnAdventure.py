"""This is a text-based choose your own adventure game. The player selects attributes and goes on a quest. You make
decisions on where to go, fight monsters and solve riddles."""

import time
import random


class Hero:
    def __init__(self, name, class_type, race, weapon, spell):
        self.name = name
        self.class_type = class_type
        self.race = race
        self.weapon = weapon
        self.spell = spell


player_hero = Hero(input("What is your name? "), input("What is your class? "), input("What is your race? "),
                   input("What weapon shall you wield? "), input("You can choose one spell. What is it? "))

article_1 = ""
article_2 = ""

if player_hero.class_type[0].lower() in ['a', 'e', 'i', 'o', 'u']:
    article_1 = "an"
else:
    article_1 = "a"
if player_hero.weapon[0].lower() in ['a', 'e', 'i', 'o', 'u']:
    article_2 = "an"
else:
    article_2 = "a"

print(f"You are {player_hero.name}, {article_1} {player_hero.class_type}, who is a member of the {player_hero.race} race. "
      f"You wield {article_2} {player_hero.weapon}, and you can cast the spell '{player_hero.spell}.'")


def choose_direction():
    while True:
        direction = input("\nShall you go to the East, the West, the South or the North? ").capitalize()
        if direction not in ["East", "West", "North", "South"]:
            print("Damn fool! Follow instructions properly")
            continue
        else:
            print(f"{direction} it is, then!")
            return direction


def eastern_encounter():
    print("A goblin appears! It advances menacingly. You must fight it off!")
    options = [1, 2, 3]
    player_score = 0
    computer_score = 0
    num_dict = {1: "lunge",
                2: "strike",
                3: "guard"}

    while True:
        if computer_score == 3 or player_score == 3:
            break
        try:
            player_guess = int(input("Fight the beast! You can lunge (1), strike swiftly (2), or guard (3): "))
        except ValueError:
            print("Damn fool! Follow instructions properly")
            continue
        if player_guess not in options:
            print("Damn fool! Follow instructions properly")
            continue
        else:
            print(f"You decided to {num_dict.get(player_guess)} with your {player_hero.weapon}.")
        computer_guess = random.randint(1, 3)
        print(f"The goblin decided to {num_dict.get(computer_guess)}.")
        if player_guess == computer_guess:
            print("Neither party could damage the other!")
        elif (player_guess == 1 and computer_guess == 3) or (player_guess == 2 and computer_guess == 1) or (
                player_guess == 3 and computer_guess == 2):
            player_score += 1
            print(f"Good job, the {num_dict.get(player_guess)} was successful!")
        elif (computer_guess == 1 and player_guess == 3) or (computer_guess == 2 and player_guess == 1) or (
                computer_guess == 3 and player_guess == 2):
            computer_score += 1
            print("Argghh! You take a blow from the creature!")
    if computer_score == 3:
        print("You have been felled by the creature.")
    if player_score == 3:
        print(f"You bested the beast with your {player_hero.weapon}! You continue with your adventure.")
    return computer_score, player_score


def western_encounter():
    print("You peer over a cliff and gaze upon a vast ocean. Suddenly, a creature begins to emerge from the depths!")
    while True:
        try:
            choice = int(input("Will you stand your ground (1), or will you retreat (2)? "))
        except ValueError:
            print("Damn fool! Follow instructions properly")
            continue
        if choice not in [1, 2]:
            print("Damn fool! Follow instructions properly")
            continue
        elif choice == 2:
            print("You run away, deciding it better to be safe than sorry.")
        else:
            print(
                f"A large, pale fish-thing rises, water cascading off its body. It looks at you with crystalline eyes "
                f"and speaks into your mind. \nIt says 'Give me your {player_hero.weapon}.'")
            time.sleep(1)
            print("You refuse!")
            time.sleep(1)
            print("It kills you instantly with its mind.")
        return choice


def northern_encounter():
    print(
        "You walk into a dense forest, an ominous croaking and chittering faintly heard in the undergrowth. "
        "\nSuddenly, a massive, spiny boar rushes at you!")
    while True:
        try:
            action_1 = int(input(f"What will you do? \n(1) Run away; "
                             f"\n(2) Stand your ground and attack with your {player_hero.weapon}; "
                             f"\n(3) Stand your ground and attack with your {player_hero.spell}; "
                             f"\n(4) Dodge to the side and attack with your {player_hero.spell}; "
                             f"\n(5) Dodge to the side and attack with your {player_hero.weapon}\n"))
        except ValueError:
            print("Damn fool! Follow instructions properly")
            continue
        if action_1 not in [1, 2, 3, 4, 5]:
            print("Damn fool! Follow instructions properly")
            continue
        else:
            if action_1 == 1:
                print("You sprint in the opposite direction, leaving the forest. The beast halts at the edge of the "
                      "forest and goes no further. \nYou return to the main road.")
            elif action_1 == 2:
                print("Your attack glances off the boar's formidable brow ridge and you are trampled.")
            elif action_1 == 3:
                print("Your spell is effective, and the beast is slain! \nHowever, it's momentum was so great, you are "
                      "trampled nonetheless.")
            elif action_1 == 4:
                print(
                    f"You evade the charge and attack with your spell '{player_hero.spell}' on its flank. "
                    f"\nThe beast is felled! You continue on your journey.")
            else:
                print(
                    f"You evade the charge and strike with your {player_hero.weapon}. "
                    f"\nThe beast is injured immensely, but still alive and even more wrathful!")
                try:
                    action_2 = int(input("Will you strike it again (1), or take the chance to run away (2)? "))
                except ValueError:
                    print("Damn fool! Follow instructions properly")
                    continue
                if action_2 not in [1, 2]:
                    print("Damn fool! Follow instructions properly")
                    continue
                else:
                    if action_2 == 1:
                        print("The beast is slain! Exhausted, but triumphant, you continue on your quest.")
                    else:
                        print(
                            "As you turn to run, the beast opens its mouth and breathes fire upon you! "
                            "\nYour smoldering carcass lands heavily upon the dirt.")
                        return action_1, action_2
        return action_1


def southern_encounter():
    print("You peer through the dense foliage and see a hut. You approach with trepidation. \nYou see a Shaman!")
    print(
        "'Brave wanderer,' croaks the wizened shaman. 'You have trespassed upon my domain. "
        "\nIf you do not answer my riddle I shall take your soul!")
    name = "SmeefusMcGeefus"
    guess = ""
    guess_count = 0
    out_of_guesses = False

    while guess != name and not out_of_guesses:
        if guess_count == 0:
            guess = input("You have three attempts to guess my name! What is it? ")
            guess_count += 1
        elif guess_count == 1:
            guess = input("Ooh hoo hoo, not quite! Guess again! ")
            guess_count += 1
        elif guess_count == 2:
            guess = input("Ee hee hee! Almost done! One more wrong guess and your soul is mine! ")
            guess_count += 1
        else:
            out_of_guesses = True
    if out_of_guesses:
        print("You LOSE! I will take your soul! Muahahaha!")
    else:
        print(
            "'AAAHHHH!!! You have bested meee!!!' \nThe shaman shrivels up and turns into a clay totem, it's power "
            "spent.\nYou continue on your journey.")


def ending():
    time.sleep(2)
    print("After a long day of travel, you reach a tavern on the side of the road, ready to rest your weary legs. \n"
          "You drink your mead and slip into a slumber, to prepare for another day on the road tomorrow, and hopefully "
          "thereafter...")


def are_dead():
    time.sleep(2)
    print(
        "You have fallen, a product of fate, your hubris, or who knows what else. Better luck in your next life...")


dead = False
number_of_encounters = 0  # each encounter makes counter go up by 1; when 4, end adventure
print("You now begin your quest for glory and riches and power. It is time to choose where you go.")

while True:
    if dead:
        are_dead()
        break

    if number_of_encounters == 4:
        ending()
        break

    direction = choose_direction()

    if direction == "East":
        number_of_encounters += 1
        player_score, computer_score = eastern_encounter()
        if player_score == 3:
            dead = True
        if computer_score == 3:
            continue

    elif direction == "West":
        number_of_encounters += 1
        choice = western_encounter()
        if choice not in [1, 2]:
            continue
        if choice == 1:
            dead = True
        elif choice == 1:
            continue

    elif direction == "North":
        number_of_encounters += 1
        try:
            action_1, action_2 = northern_encounter()
        except TypeError:
            continue
        if action_1 in [1, 4]:
            continue
        elif action_1 in [2, 3]:
            dead = True
        elif action_1 == 5:
            if action_2 == 1:
                continue
            else:
                dead = True

    else:
        number_of_encounters += 1
        southern_encounter()
        time.sleep(1)
        continue

