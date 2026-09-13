class Recipe:
    def __init__(self, recipes={
        # Weapons
        "Arrow": {
            "Bone": 1,
            "Feather": 1,
            "Sharp Stone": 1,
        },

        "Bow": {
            "Stick": 3,
            "Rope": 2,
        },

        "Spear": {
            "Stick": 2,
            "Sharp Stone": 2,
            "Rope": 1,
        },

        "Dagger": {
            "Iron Ore": 2,
            "Stick": 1,
        },

        "Iron Sword": {
            "Iron Ore": 5,
            "Wood": 2,
        },

        "Steel Sword": {
            "Steel Ingot": 4,
            "Wood": 2,
        },

        "War Hammer": {
            "Steel Ingot": 6,
            "Wood": 3,
        },

        "Dragon Slayer": {
            "Dragon Tooth": 2,
            "Steel Ingot": 10,
            "Wood": 3,
        },

        # Armour
        "Cloth Armour": {
            "Cloth": 8,
        },

        "Leather Armour": {
            "Leather": 8,
        },

        "Iron Armour": {
            "Iron Ore": 12,
        },

        "Steel Armour": {
            "Steel Ingot": 10,
        },

        "Dragon Armour": {
            "Dragon Scale": 12,
            "Steel Armour": 1,
        },

        # Consumables
        "Bandage": {
            "Cloth": 3,
        },

        "Health Potion": {
            "Herb": 3,
            "Water": 1,
        },

        "Greater Health Potion": {
            "Herb": 8,
            "Magic Crystal": 1,
        },

        "Antidote": {
            "Spider Eye": 1,
            "Herb": 2,
        },

        "Torch": {
            "Stick": 1,
            "Cloth": 1,
            "Oil": 1,
        },

        # Utility
        "Rope": {
            "Cloth": 2,
        },

        "Backpack Upgrade": {
            "Leather": 5,
            "Rope": 2,
        },

        "Campfire": {
            "Stick": 4,
            "Stone": 6,
        },

        "Lockpick": {
            "Iron Ore": 1,
        },

        # Magic
        "Magic Staff": {
            "Magic Crystal": 2,
            "Wood": 2,
        },

        "Soul Amulet": {
            "Soul Gem": 2,
            "Magic Crystal": 1,
        },

        "Infernal Blade": {
            "Infernal Core": 1,
            "Steel Ingot": 8,
            "Demon Horn": 2,
        },

        "Crystal Shield": {
            "Crystal": 6,
            "Stone Core": 2,
        },

        "Dragon Crown": {
            "Dragon Scale": 5,
            "Dragon Tooth": 2,
            "Magic Crystal": 3,
        },
    }):
        self.recipes = recipes