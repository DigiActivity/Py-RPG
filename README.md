# Projet RPG

## Introduction

Dans ce projet, nous allons créer un jeu de rôle (RPG) en utilisant la programmation orientée objet (POO) en Python. Le jeu se déroule dans un monde fantastique où le joueur incarne un héros qui doit explorer des donjons, combattre des monstres et collecter des trésors. Le but du jeu est de survivre aux dangers du donjon le plus longtemps possible en parcourant les salles.

Le but ici est de s'entraîner aux classes et de les faire intéragir entre elles. Le jeu est très simplifié et ne contient pas de graphismes, il est basé sur des textes et des interactions en console. D'ailleurs, toute la partie GUI et gameplay sera fournie, il vous suffira de correctement concevoir les classes et méthodes demandées et de vérifier que tout fonctionne correctement.

## Étapes du projet

1. [Items](#exercice-1-items) : Créer des items de soin, de dégâts et de défense.

2. [Inventaire](#exercice-2-inventaire) : Gérer l'inventaire du joueur pour stocker et utiliser des items.

3. [Entités](#exercice-3-entités) : Créer des entités (joueur, monstre et salle vide) pour explorer et combattre dans le donjon.

4. [Fichier principal](#fichier-principal) : Créer le fichier principal du jeu pour initialiser les entités, gérer la boucle de jeu et afficher les informations.

## Exercice 1. Items

Les items sont des objets que les entités peuvent posséder et utiliser. Ils sont essentiels pour le gameplay car ils permettent aux entités d'augmenter leurs capacités de combat et de survie. Il existe plusieurs types d'items dans le jeu :

### Classe `Item`

La classe `Item` est la classe de base pour tous les items. Elle contient les propriétés et méthodes communes à tous les types d'items.

- **Propriétés :**
  - `name` : Le nom de l'item.
  - `drop_rate` : Le taux de drop de l'item (probabilité d'être trouvé).
  - `value` : La valeur de l'item (quantité de soin, de dégâts ou de défense qu'il apporte).
  - `unit` : L'unité de la valeur (HP, DMG, DEF).

- **Méthodes :**
  - `__init__(self, name, drop_rate)` : Initialise un item avec un nom et un taux de drop.
  - `__str__(self)` : Retourne une représentation en chaîne de caractères de l'item.

### Classe `HealItem`

La classe `HealItem` hérite de la classe `Item` et représente les items de soin.

- **Propriétés :**
  - `value` : La quantité de points de vie (HP) que l'item restaure.
  - `unit` : Fixée à "HP".

- **Méthodes :**
  - `__init__(self, name, hp, drop_rate=0.5)` : Initialise un item de soin avec un nom, une valeur de soin et un taux de drop par défaut de 0.5.

### Classe `DamageItem`

La classe `DamageItem` hérite de la classe `Item` et représente les items de dégâts.

- **Propriétés :**
  - `value` : La quantité de dégâts (DMG) que l'item inflige.
  - `unit` : Fixée à "DMG".

- **Méthodes :**
  - `__init__(self, name, dmg, drop_rate=0.5)` : Initialise un item de dégâts avec un nom, une valeur de dégâts et un taux de drop par défaut de 0.5.

### Classe `DefenseItem`

La classe `DefenseItem` hérite de la classe `Item` et représente les items de défense.

- **Propriétés :**
  - `value` : La quantité de défense (DEF) que l'item apporte.
  - `unit` : Fixée à "DEF".

- **Méthodes :**
  - `__init__(self, name, df, drop_rate=0.5)` : Initialise un item de défense avec un nom, une valeur de défense et un taux de drop par défaut de 0.5.

Ces classes permettent de créer différents types d'items avec des propriétés spécifiques, tout en partageant des fonctionnalités communes définies dans la classe de base `Item`.

## Exercice 2. Inventaire

L'inventaire est une collection d'items que les entités peuvent posséder. Il permet de gérer les items de manière organisée et de les utiliser en fonction des besoins. L'inventaire joue un rôle central dans le jeu car il détermine les capacités de combat et de survie des entités.

### Listes d'Items de Départ

Pour faciliter la création des inventaires, voici des listes d'items de départ pour les entités :

- **Items de Défense :**
  - `player_starter_defense` : `DefenseItem("Leather shoes", 5)`
  - `DefenseItem("Composite Armor", 25)`
  - `DefenseItem("Great Wooden Shield", 20)`
  - `DefenseItem("Bless of Ancient Gods", 50, 0.1)`
  - `DefenseItem("Iron Helmet", 15)`

- **Items de Dégâts :**
  - `player_starter_damage` : `DamageItem("Small Throwable Rock", 5)`
  - `DamageItem("Too Big Sword", 10)`
  - `DamageItem("Dagger", 15)`
  - `DamageItem("Dwarf Axe", 17)`
  - `DamageItem("Legendary Cosmic Mastersword", 35, 0.1)`

- **Items de Soin :**
  - `player_starter_heal` : `HealItem("Apple", 10)`
  - `HealItem("Heal Potion", 50)`
  - `HealItem("Cheesecake", 30)`
  - `HealItem("McDonald's Triple Bacon Cheese", 30)`

Ces listes permettent de créer des inventaires variés et équilibrés pour les héros et les monstres, en incluant des items de différents types et valeurs.
Évidemment si vous souhaitez ajouter des items supplémentaires ou différents, vous êtes libres de le faire.

### Classe `Inventory`

La classe `Inventory` gère la collection d'items pour une entité.

- **Propriétés :**
  - `items` : Une liste d'items que l'inventaire contient.

- **Méthodes :**
  - `generate_hero_inventory(self)` : Génère l'inventaire initial du héros avec des items de départ.
  - `generate_monster_inventory(self)` : Génère un inventaire aléatoire pour les monstres.
  - `get_total_defense(self)` : Calcule la somme des valeurs de tous les items de défense dans l'inventaire.
  - `get_total_damage(self)` : Calcule la somme des valeurs de tous les items de dégâts dans l'inventaire.
  - `list_heals(self)` : Renvoie la liste des items de soin disponibles dans l'inventaire.
  - `add(self, item)` : Ajoute un item à l'inventaire.

#### Détails des Méthodes

- **`generate_hero_inventory(self)`**
  - Ajoute des items de départ spécifiques à l'inventaire du héros.

- **`generate_monster_inventory(self)`**
  - Ajoute un item aléatoire de chaque type (défense, dégâts, soin) à l'inventaire du monstre.

- **`get_total_defense(self)`**
  - Parcourt tous les items de l'inventaire et additionne les valeurs des items de défense (`unit` égale à "DEF").
  - Retourne la valeur totale de défense.

- **`get_total_damage(self)`**
  - Parcourt tous les items de l'inventaire et additionne les valeurs des items de dégâts (`unit` égale à "DMG").
  - Retourne la valeur totale de dégâts.

- **`list_heals(self)`**
  - Parcourt tous les items de l'inventaire et crée une liste des items de soin (`unit` égale à "HP").
  - Retourne la liste des items de soin.

- **`add(self, item)`**
  - Ajoute un item à la liste des items de l'inventaire.


## Exercice 3. Entités

Les entités sont les personnages et les objets interactifs du jeu. Elles peuvent posséder et utiliser des items, et interagir avec d'autres entités. Les principales entités du jeu sont :

### Classe `Entity`

La classe `Entity` est la classe de base pour toutes les entités du jeu. Elle contient les propriétés et méthodes communes à toutes les entités.

- **Propriétés :**
  - `name` : Le nom de l'entité.
  - `hp` : Les points de vie (HP) de l'entité.
  - `inventory` : L'inventaire de l'entité, qui est une instance de la classe `Inventory`.
  - `type` : Le type de l'entité (par défaut "GenericEntity").
  - `level` : Le niveau de l'entité (par défaut 1).

- **Méthodes :**
  - `__init__(self, name, hp)` : Initialise une entité avec un nom et des points de vie.
  - `__str__(self)` : Retourne une représentation en chaîne de caractères de l'entité.

#### Détails des Méthodes

- **`__init__(self, name, hp)`**
  - Initialise une entité avec un nom, des points de vie, un inventaire vide, un type par défaut et un niveau par défaut.

- **`__str__(self)`**
  - Retourne une représentation en chaîne de caractères de l'entité, incluant son type, son nom, son niveau, ses points de vie, ses dégâts totaux et sa défense totale.

### Sous-classes d'Entités

#### Classe `Monster`

La classe `Monster` hérite de la classe `Entity` et représente les monstres que le héros rencontre dans le jeu.

- **Propriétés :**
  - `level` : Le niveau du monstre (par défaut 1).
  - `hp` : Les points de vie du monstre (par défaut 20).

- **Méthodes :**
  - `__init__(self, level=1, hp=20)` : Initialise un monstre avec un niveau et des points de vie par défaut. Génère un inventaire aléatoire pour le monstre.

#### Classe `Hero`

La classe `Hero` hérite de la classe `Entity` et représente le héros contrôlé par le joueur.

- **Propriétés :**
  - `name` : Le nom du héros.
  - `hp` : Les points de vie du héros (par défaut 40).

- **Méthodes :**
  - `__init__(self, name, hp=40)` : Initialise un héros avec un nom et des points de vie par défaut. Génère l'inventaire initial du héros.

#### Classe `EmptyRoom`

La classe `EmptyRoom` hérite de la classe `Entity` et représente une salle vide dans le jeu.

- **Propriétés :**
  - `name` : Le nom de la salle.
  - `hp` : Les points de vie de la salle (fixé à 0).

- **Méthodes :**
  - `__init__(self, name)` : Initialise une salle vide avec un nom. Génère un inventaire aléatoire pour la salle.

Ces sous-classes permettent de créer différents types d'entités avec des propriétés et des comportements spécifiques, tout en partageant des fonctionnalités communes définies dans la classe de base `Entity`.

## Fichier principal

Le fichier principal `main.py` contient le code principal du jeu, y compris la création des entités, l'initialisation du jeu, la boucle de jeu et l'affichage des informations. Il utilise les classes et méthodes définies dans les exercices précédents pour gérer les interactions entre les entités et les items.

> Pour plus de challenge je vous invite à ne pas regarder la suite du README et à essayer vous-même de concevoir le GUI et la boucle de gameplay. Toutefois si vous l'ouvrez, ne vous laissez pas impressionner par la longueur du code. Les mécaniques restent simples, ormis les fonctions de GUI qui sont un peu plus complexes, mais quasiment équivalentes à ce qu'on a déjà pu faire.

> Vous pouvez également trouver un énoncé détaillé sur la façon de réaliser le projet ici : [Projet RPG - Enoncé](Realiser-le-main.md)

<details>
  <summary>Spoiler warning</summary>
  
  ```python
import os
from random import random
from classes.entities import Hero, EmptyRoom, Monster
from classes.inventory import Inventory

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
            room = EmptyRoom("Left Room" if user_input == "l" else "Right Room")
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
                    damages = Inventory.calculate_damages(hero.inventory, monster.inventory)
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
                damages = Inventory.calculate_damages(monster.inventory, hero.inventory)
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
  ```
  
</details>