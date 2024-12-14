import os
from random import random
from entity import Monster, EmptyRoom, Hero

def clean():
    os.system('cls' if os.name=='nt' else 'clear')


def gui(hero, text = "", actions = [], monster = None):
    clean()
    print(hero)
    if (monster != None):
        print("------------------")
        print(monster)
    print("------------------")
    if (text != ""):
        print(text)
        print("------------------")
    if (len(actions) == 0):
        input("Press Enter to continue...")
        return
    else:
        # ajouter la possibilité de quitter et de regarder dans l'inventaire
        final_actions = actions.copy()
        final_actions.append(("inventory", "i"))
        final_actions.append(("quit", "q")) # on peut quitter dans tous les cas

        # construire le texte de sélection du choix [attack (a), heal (h), ...]
        action_text = ", ".join([f"{choice[0]} ({choice[1]})" for choice in final_actions])

        while(True):
            user_input = input(f"[{action_text}] : ")
            for choice in final_actions:
                if user_input in choice:
                    # gestion de l'inventaire
                    if "i" in choice:
                        # on affiche l'inventaire
                        clean()
                        print(hero.inventory)
                        print("------------------")
                        input("Press Enter to continue...")
                        # on revient à la fenètre d'avant
                        return gui(hero, text, actions, monster)
                    else :
                        return choice[1]
            print("Try again.")

def calculate_damages(attacker_inv, defenser_inv):
    minimum_damage_ratio = 0.1
    brut_damage = attacker_inv.get_total_damage() - (defenser_inv.get_total_defense() / 2)
    min_damages = attacker_inv.get_total_damage() * minimum_damage_ratio
    return max(brut_damage, min_damages)


def play():
    clean()
    name = input("Select Hero name : \n")
    hero = Hero(name)
    gui(hero, "Are you ready to enter the dungeon ?")

    wants_to_quit = False

    # selectionner équipement

    while (wants_to_quit == False and hero.hp > 0):
        # proposer d'aller dans la salle de droite ou de gauche (ou soin ou quitter)
        user_input = gui(hero, "Select a room to enter",[("left", "l"), ("right", "r")])
        
        if (user_input == "q"):
            wants_to_quit = True
            break
        # préparer la salle
        if (random() > hero.level / 10):
            # si c'est une pièce vide on gagne l'équipement et on retourne dans le couloir
            room = EmptyRoom()
            dropped_items = room.inventory.drop()
            if len(dropped_items) == 0:
                gui(hero, f"You entered : {room.name}, it is empty")
            else:
                text = f"You entered : {room.name}, here's wat you found : "
                for item in dropped_items:
                    text += f"\n - {str(item)}"
                    hero.inventory.add(item)
                gui(hero, text)
            hero.level += 1

        else:
            monster = Monster()
            gui(hero, f"Behind the door, {monster.name} was waiting for you")
            # le combat commence
            while hero.hp > 0 and monster.hp > 0:
                user_input = gui(hero, monster=monster, actions=[("attack", "a"), ("heal", "h")])

                if (user_input == "q"):
                    wants_to_quit = True
                    break
                if user_input == "a":
                    # damages = hero.inventory.calculate_damages(monster.inventory)
                    damages = calculate_damages(hero.inventory, monster.inventory)
                    monster.hp -= damages
                    if monster.hp < 0:
                        monster.hp = 0
                    gui(hero, monster=monster, text=f"You hitted the monster with {damages}DMG !")
                    if monster.hp == 0:
                        dropped_items = monster.inventory.drop()
                        if len(dropped_items) == 0:
                            gui(hero, f"You successfuly won against {monster.name} !")
                        else:
                            text = f"You successfuly won against {monster.name} ! He dropped :"
                            for item in dropped_items:
                                text += f"\n - {str(item)}"
                                hero.inventory.add(item)
                            gui(hero, text)
                        hero.level += 2
                        continue
                else:
                    #logique de heal
                    heal_items = hero.inventory.list_heals()
                    if len(heal_items) == 0:
                        gui(hero, text="You have no heals :(")
                        continue
                    heal_text = "[Heals]"
                    heal_actions = []
                    for i, item in enumerate(heal_items):
                        heal_text += f"\n - ({i}) {str(item)}"
                        heal_actions.append((item.name, str(i)))
                    
                    selected_index = gui(hero, heal_text, heal_actions)
                    selected_heal = heal_items[int(selected_index)]
                    hero.hp += selected_heal.value
                    hero.inventory.remove(selected_heal)
                    gui(hero, text=f"You used : {selected_heal.name}, adding {selected_heal.value} HP")
                
                # au tour du monstre
                damages = calculate_damages(monster.inventory, hero.inventory)
                hero.hp -= damages
                if hero.hp < 0:
                        hero.hp = 0

                gui(hero, monster=monster, text=f"{monster.name} hitted you with {damages}DMG ! {hero.hp} left")
    if (wants_to_quit):
        print("Bye ! 👋")
        return
    else:
        user_input = gui(hero, "You died, do you want to try again ?", [("yes", "y"), ("no", "n")])
        if user_input == "y":
            return play()

play()