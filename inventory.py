from item import DamageItem, DefenseItem, HealItem
import random

player_starter_defense = DefenseItem("Leather shoes", 5)
player_starter_damage = DamageItem("Small Throwable Rock", 5)
player_starter_heal = HealItem("Apple", 10)

all_def = [
    player_starter_defense,
    DefenseItem("Composite Armor", 25),
    DefenseItem("Great Wooden Shield", 20),
    DefenseItem("Bless of Ancient Gods", 50, 0.1),
    DefenseItem("Iron Helmet", 15),
]

all_dmg = [
    player_starter_damage,
    DamageItem("Too Big Sword", 10),
    DamageItem("Dagger", 15),
    DamageItem("Dwarf Axe", 17),
    DamageItem("Legendary Cosmic Mastersword", 35, 0.1),
]

all_hp = [
    player_starter_heal,
    HealItem("Heal Potion", 50),
    HealItem("Cheesecake", 30),
    HealItem("McDonald's Triple Bacon Cheese", 30),
]


class Inventory:
    def __init__(self):
        self.items = []
    
    def generate_hero_inventory(self):
        self.items.extend([
            player_starter_defense,
            player_starter_damage,
            player_starter_heal
        ])
    
    def generate_monster_inventory(self):
        # Méthode manuelle
        random_def_index = random.randint(0, len(all_def) -1 )
        random_def = all_def[random_def_index]
        # Méthode simple
        random_dmg = random.choice(all_dmg)
        random_hp = random.choice(all_hp)

        self.items.extend([random_def, random_dmg, random_hp])
    
    def get_total_defense(self):
        sum = 0
        for item in self.items:
            if item.unit == "DEF":
                sum = sum + item.value
        return sum

    def get_total_damage(self):
        sum = 0
        for item in self.items:
            if item.unit == "DMG":
                sum = sum + item.value
        return sum
    
    def list_heals(self):
        heals = []
        for item in self.items:
            if item.unit == "HP":
                heals.append(item)
        return heals
    
    def add(self, item):
        self.items.append(item)
    
    def drop(self):
        # renvoie une liste d'items drop
        l = []
        for item in self.items:
            if item.drop_rate > random.random():
                l.append(item)
        return l
