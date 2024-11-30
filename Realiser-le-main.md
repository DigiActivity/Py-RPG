## Prérequis


### fonction clean()

```python
import os
...

def clean():
    # on utilise la commande cls pour windows et clear pour les autres systèmes
    os.system('cls' if os.name=='nt' else 'clear')
```

## Le GUI

La fonction GUI servira à afficher des informations dans la console et servira également à récupérer des informations de l'utilisateur (faire des choix).

On devra passer dans cette fonction :
- notre héros, pour afficher ses stats (obligatoire)
- un texte à afficher, informatif, pour que le jeu soit plus vivant (optionnel)
- une liste d'actions possibles, pour que le joueur puisse choisir (optionnel)
- un monstre, pour afficher ses stats (optionnel)

> Rappel : pour créer une fonction avec des arguments optionnels, on peut leur donner des valeurs par défaut avec un `=`. Par exemple :
> ```python
> def ma_fonction(arg1, arg2 = "valeur par défaut"):
>     print(arg1, arg2)
> ```

### Étapes d'affichage

Chacunes de ces étapes sont affichées sur un seul et même écran, on ne fait pas de `clean()` entre chaque étape.

Cela afficherait par exemple quelque chose comme :

```
Stats du héros
...
------------------
Stats du monstre
------------------
Texte informatif blablabla
------------------
[attack (a), heal (h), ...] : 
```

1. On commence par nettoyer la console
2. On affiche les stats du héros
3. Si un monstre est passé en argument, on l'affiche
4. On affiche le texte informatif si il est passé en argument
5. Si aucune action n'est passée en argument, on affiche un message pour demander à l'utilisateur de presser Entrée pour continuer
6. Sinon, on affiche les actions possibles, sous forme de texte, avec les raccourcis entre parenthèses

### Gestion des actions

L'idée derrière les actions dans le GUI est de faciliter la vie du joueur. On ne veut pas qu'il ait à taper "attack" ou "heal" à chaque fois, mais plutôt qu'il puisse taper "a" ou "h".

Pour cela, on va ajouter un raccourci pour chaque action possible. Par exemple, si on a les actions "attack" et "heal", on pourra taper "a" ou "h" pour les choisir.

La fonction GUI pourrait donc s'appeller comme ça :

```python
gui(hero, text="Un monstre apparaît !", actions=[("attack", "a"), ("heal", "h")], monster=monster)
```

Ici on affiche les stats du héros, le texte "Un monstre apparaît !", les stats du monstre, et on propose deux actions : "attack" et "heal", avec les raccourcis "a" et "h".

#### Comment afficher et sélectionner ces actions

On veut pouvoir passer des actions sous forme de liste de tuples, où chaque tuple contient le nom de l'action et son raccourci.

L'idée c'est de pouvoir ensuite facilement récupérer l'action sélectionnée pour la donner au jeu.

Exemple :

```python
choix_joueur = gui(hero, actions=[("attack", "a"), ("heal", "h")])
# Si le joueur sélectionne "attack" ou "a", choix_joueur vaudra "a", si il sélectionne "heal" ou 'h', choix_joueur vaudra "h"
```

Pour cela, voici les étapes à suivre :

*Tant que le joueur n'a pas sélectionné d'actions :*

1. à partir de la liste de tuples, construire un texte qui affiche les actions possibles (avec des boucles)

```python
text_to_print = ""
for action in actions:
    print(f"{action[0]} ({action[1]})")
```

2. demander à l'utilisateur de taper une lettre

```python
user_input = input(text_to_print)
```

3. vérifier si la lettre est un raccourci d'une action possible, et si oui, retourner le raccourci, sinon demander à l'utilisateur de retaper une lettre

<details>
<summary>
BONUS : afficher l'inventaire
</summary>
Vous pouvez ajouter dans la boucle, une option pour afficher l'inventaire. L'idée est d'afficher seulement l'inventaire, puis revenir à l'écran précédent.

Pour ça, on peut déjà commencer par ajouter une action "inventory" avec le raccourci "i" dans la liste d'actions.

```python
actions_copy = actions.copy()
actions_copy.append(("inventory", "i"))
```

Ensuite, dans la boucle, on affiche cette action en plus des autres, et on vérifie si l'utilisateur a tapé "i" pour afficher l'inventaire.

Si c'est le cas, on fait un clean(), on affiche l'inventaire et on demande à l'utilisateur de presser Entrée pour continuer.

Ensuite, pour revenir rapidement à l'écran précédent, le plus simple est de rappeler la fonction GUI avec les mêmes arguments que la première fois.

```python
if user_input == "i":
    clean()
    print(hero.inventory)
    input("Press Enter to continue...")
    return gui(hero, text, actions, monster)
else:
    return user_input
```
</details>

### Code final

<details>
<summary>
Code final de la fonction GUI (Spoiler)
</summary>
    
```python
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
            for choice in final_actions: # on vérifie que l'utilisateur a tapé un raccourci valide
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
                        return choice[1] # si l'utilisateur a tapé "heal", on retourne "h"
            print("Incorrect")
```
</details>

## La boucle de jeu

On va maintenant utiliser cette fonction GUI pour créer une boucle de jeu.

Dans une fonction `play()`, on commencera par clean() et on affichera un message de bienvenue.

Ensuite, on demandera au joueur de taper son nom, puis on créera un héros avec ce nom.

Pour tester la fonction GUI, on pourra afficher les stats du héros avec la fonction GUI.

```python
...
def play():
    clean()
    print("Bienvenue dans le jeu !")
    hero_name = input("Quel est votre nom ? ")
    hero = Hero(hero_name)
    gui(hero, "Êtes-vous prêt à commencer ?") # pas d'actions, le joueur devra voir les stats et appuyer sur Entrée
```

Ensuite, on va créer une boucle infinie, qui se terminera si le héros meurt ou si le joueur décide de quitter.

Cette boucle sera en plusieurs étapes :

1. On simule un choix en proposant au joueur d'entrer dans la pièce de droite ou de gauche. (il peut aussi quitter à cette étape de la partie)

2. Déterminer aléatoirement si le joueur tombe sur un monstre ou sur une pièce vide.

### Pièce vide

Si le joueur tombe sur une pièce vide, on récupère l'inventaire de la salle avec `la_piece.inventory.drop()`

Si il n'y a rien de drop, on affiche que c'est vide. Sinon on affiche la liste des objets trouvés et on recommence la boucle

### Monstre

Si le joueur tombe sur un monstre, on crée un monstre avec `Monster()`, on affiche le monstre avec la fonction GUI, et le combat commence :

1. Tant que le héros et le monstre sont en vie, on affiche le GUI avec les actions possibles (attack, heal, ...)

2. Si le joueur choisit "a" (attack), on attaque le monstre avec `hero.attack(monster)` on doit calculer les dégâts infligés et les afficher dans le GUI :
    - Les dégâts dépendent de l'attaque du héros (`heros.inventory.get_total_damage()`) et de la défense du monstre (`monster.inventory.get_total_defense()`).Cependant on veut un minimum de dégâts, donc on utilisera `max(1, degats)`
    - On soustrait les dégâts à la vie du monstre, et on affiche en GUI les dégâts infligés
    - Si le monstre tombe à 0 ou moins, on le fixe à zéro (sinon ça fera bizarre d'avoir un monstre à -10PV) et on afiche un message de victoire. Ensuite, on récupère les items du monstre avec `monster.inventory.drop()` et on les ajoute à l'inventaire du héros avec `hero.inventory.add()`. On peut ensuite continuer avec un `continue` (et vu que le while concerne les deux combattants, ça sortira aussi de la boucle de combat).
3. Si le joueur choisis "h" (heal), on va devoir lui afficher tous ses heal disponibles et lui demander d'en choisir un. Pour cela, on peut faire `hero.inventory.list_heals()` qui renvoie le tableau des heals dans l'inventaire.
    - Si il n'y en a pas, on prévient qu'il n'y a pas de heal et on redémarre le tour avec `continue` (on ne veut pas que le joueur se prenne des dégâts si il n'avait pas de heal).
    - Si il a des heals, les afficher et construire des actions en fonction des heals disponibles. Par exemple, si il a 3 heals, on les listera :
    ```
        [Heals]
        - (0) [Item] : Apple (10 HP)
        - (1) [Item] : Heal Potion (50 HP)
    ```
    et donc comme actions disponible on devra avoir `[("Apple", "0"), ("Heal Potion", "1")]`
    On récupère le numéro d'index du heal choisi par le joueur, on récupère le bon item et ensuite on pourra l'utiliser par exemple avec `hero.hp += selected_heal.value`. On supprime ensuite l'item de l'inventaire du héros avec `hero.inventory.remove(selected_heal)`.

4. Après avoir fait une action, c'est au tour du monstre. On calcule les dégâts un peu comme pour le héros (voir 2.) et ensuite on soustrait les dégâts aux pv du héros, en affichant un message comme 'Le monstre vous a tapé'. Si le héros tombe à 0 ou moins, on le fixe à zéro, on affiche un message de défaite et on sort de la boucle de combat avec un `break`.

À la fin de la boucle de combat, si le héros n'a plus de pv, on affiche un message de défaite et on sort de la boucle de jeu.

Sinon on reprend la boucle de jeu (avec les pièces vides ou les monstres).
