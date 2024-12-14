from inventory import Inventory

class Entity:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.inventory = Inventory()
        self.type = "GenericEntity"
        self.level = 1

    def __str__(self):
        details = f"[{self.type}] "
        if self.name != "":
            details += self.name

        details += f"""
- HP : {self.hp}
- Damages : {self.inventory.get_total_damage()}
- Defense : {self.inventory.get_total_defense()}
"""
        return details


class Monster(Entity):
    def __init__(self, hp=20):
        name = "Gros monstre"
        super().__init__(name, hp)
        self.inventory.generate_monster_inventory()

class Hero(Entity):
    def __init__(self, name, hp=40):
        super().__init__(name, hp)
        self.inventory.generate_hero_inventory()

class EmptyRoom(Entity):
    def __init__(self):
        name = ""
        super().__init__(name, 0)
        self.inventory.generate_monster_inventory()
