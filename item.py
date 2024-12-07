class Item:
    def __init__(self, name, drop_rate):
        self.name = name
        self.drop_rate = drop_rate
        self.unit = None
        self.value = None
    
    def __str__(self):
        return f"[Item] {self.name} ({self.value} {self.unit})"

class HealItem(Item):
    def __init__(self, name, hp, drop_rate=0.5):
        # Init du parent
        super().__init__(name, drop_rate)
        # Init de HealItem
        self.unit = "HP"
        self.value = hp

class DamageItem(Item):
    def __init__(self, name, damage, drop_rate=0.5):
        super().__init__(name, drop_rate)
        self.unit = "DMG"
        self.value = damage

class DefenseItem(Item):
    def __init__(self, name, defense, drop_rate=0.5):
        super().__init__(name, drop_rate)
        self.unit = "DEF"
        self.value = defense

