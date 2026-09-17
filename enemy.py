class Enemy:
    def __init__(self, name, current_health, max_health, attack, max_attack, armour, drops):
        self.name = name
        self.current_health = current_health
        self.max_health = max_health
        self.attack = attack
        self.max_attack = max_attack
        self.armour = armour
        self.drops = drops

    def get_damaged(self, amount):
        if self.current_health - amount <= 0:
            self.current_health = 0
        else:
            self.current_health -= amount
    
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    

class Drops:
    def __init__(self, item, drop_rate, min_amount, max_amount):
        self.item = item
        self.drop_rate = drop_rate
        self.min_amount = min_amount
        self.max_amount = max_amount

rat = Enemy(
    name="Rat",
    current_health=45,
    max_health=45,
    attack=2,
    max_attack=5,
    armour=0,
    drops=[
        Drops(
            item="Fur",
            drop_rate=1,
            min_amount=1,
            max_amount=3,
        ),
        Drops(
            item="Rat Tail",
            drop_rate=0.6,
            min_amount=1,
            max_amount=2,
        ),
    ]
)

spider = Enemy(
    name="Spider",
    current_health=70,
    max_health=70,
    attack=4,
    max_attack=6,
    armour=4,
    drops=[
        Drops(
            item="Spider Eye",
            drop_rate=0.4,
            min_amount=1,
            max_amount=4,
        ),
        Drops(
            item="Spider Leg",
            drop_rate=0.8,
            min_amount=2,
            max_amount=6,
        ),
        Drops(
            item="Venom Sack",
            drop_rate=0.15,
            min_amount=1,
            max_amount=1,
        ),
    ]
)

skeleton = Enemy(
    name="Skeleton",
    current_health=100,
    max_health=100,
    attack=5,
    max_attack=10,
    armour=2,
    drops=[
        Drops(
            item="Bone",
            drop_rate=1,
            min_amount=1,
            max_amount=8,
        ),
        Drops(
            item="Arrow",
            drop_rate=0.2,
            min_amount=1,
            max_amount=2,
        ),
    ]
)

wolf = Enemy(
    name="Wolf",
    current_health=90,
    max_health=90,
    attack=6,
    max_attack=11,
    armour=3,
    drops=[
        Drops(
            item="Fur",
            drop_rate=1,
            min_amount=2,
            max_amount=5,
        ),
        Drops(
            item="Fang",
            drop_rate=0.5,
            min_amount=1,
            max_amount=3,
        ),
    ]
)

zombie = Enemy(
    name="Zombie",
    current_health=120,
    max_health=120,
    attack=6,
    max_attack=9,
    armour=5,
    drops=[
        Drops(
            item="Flesh",
            drop_rate=1,
            min_amount=2,
            max_amount=6,
        ),
        Drops(
            item="Cloth",
            drop_rate=0.7,
            min_amount=1,
            max_amount=4,
        ),
    ]
)

goblin = Enemy(
    name="Goblin",
    current_health=130,
    max_health=130,
    attack=9,
    max_attack=14,
    armour=6,
    drops=[
        Drops(
            item="Leather",
            drop_rate=0.8,
            min_amount=1,
            max_amount=3,
        ),
        Drops(
            item="Dagger",
            drop_rate=0.15,
            min_amount=1,
            max_amount=1,
        ),
    ]
)

orc = Enemy(
    name="Orc",
    current_health=170,
    max_health=170,
    attack=12,
    max_attack=17,
    armour=8,
    drops=[
        Drops(
            item="Iron Ore",
            drop_rate=0.8,
            min_amount=2,
            max_amount=5,
        ),
        Drops(
            item="Club",
            drop_rate=0.1,
            min_amount=1,
            max_amount=1,
        ),
    ]
)

bandit = Enemy(
    name="Bandit",
    current_health=140,
    max_health=140,
    attack=11,
    max_attack=15,
    armour=7,
    drops=[
        Drops(
            item="Cloth",
            drop_rate=0.8,
            min_amount=2,
            max_amount=5,
        ),
        Drops(
            item="Arrow",
            drop_rate=0.6,
            min_amount=2,
            max_amount=8,
        ),
    ]
)

giant_spider = Enemy(
    name="Giant Spider",
    current_health=150,
    max_health=150,
    attack=10,
    max_attack=16,
    armour=8,
    drops=[
        Drops(
            item="Spider Eye",
            drop_rate=0.7,
            min_amount=2,
            max_amount=6,
        ),
        Drops(
            item="Spider Leg",
            drop_rate=1,
            min_amount=4,
            max_amount=10,
        ),
        Drops(
            item="Venom Sack",
            drop_rate=0.4,
            min_amount=1,
            max_amount=2,
        ),
        Drops(
            item="Silk",
            drop_rate=0.3,
            min_amount=1,
            max_amount=3,
        ),
    ]
)

troll = Enemy(
    name="Troll",
    current_health=260,
    max_health=260,
    attack=18,
    max_attack=25,
    armour=14,
    drops=[
        Drops(
            item="Troll Hide",
            drop_rate=1,
            min_amount=1,
            max_amount=3,
        ),
        Drops(
            item="Club",
            drop_rate=0.2,
            min_amount=1,
            max_amount=1,
        ),
    ]
)

werewolf = Enemy(
    name="Werewolf",
    current_health=220,
    max_health=220,
    attack=19,
    max_attack=28,
    armour=10,
    drops=[
        Drops(
            item="Fur",
            drop_rate=1,
            min_amount=4,
            max_amount=8,
        ),
        Drops(
            item="Fang",
            drop_rate=0.8,
            min_amount=2,
            max_amount=5,
        ),
        Drops(
            item="Moon Shard",
            drop_rate=0.2,
            min_amount=1,
            max_amount=1,
        ),
    ]
)

dark_knight = Enemy(
    name="Dark Knight",
    current_health=250,
    max_health=250,
    attack=20,
    max_attack=26,
    armour=18,
    drops=[
        Drops(
            item="Steel Ingot",
            drop_rate=0.8,
            min_amount=2,
            max_amount=5,
        ),
        Drops(
            item="Knight Sword",
            drop_rate=0.1,
            min_amount=1,
            max_amount=1,
        ),
    ]
)

golem = Enemy(
    name="Golem",
    current_health=320,
    max_health=320,
    attack=16,
    max_attack=22,
    armour=22,
    drops=[
        Drops(
            item="Iron Ore",
            drop_rate=1,
            min_amount=5,
            max_amount=10,
        ),
    ]
)

dragon = Enemy(
    name="Dragon",
    current_health=550,
    max_health=550,
    attack=28,
    max_attack=38,
    armour=28,
    drops=[
        Drops(
            item="Dragon Scale",
            drop_rate=1,
            min_amount=5,
            max_amount=10,
        ),
        Drops(
            item="Dragon Tooth",
            drop_rate=0.8,
            min_amount=1,
            max_amount=3,
        ),
    ]
)

lich = Enemy(
    name="Lich",
    current_health=400,
    max_health=400,
    attack=30,
    max_attack=40,
    armour=18,
    drops=[
        Drops(
            item="Magic Crystal",
            drop_rate=0.7,
            min_amount=1,
            max_amount=3,
        ),
        Drops(
            item="Ancient Tome",
            drop_rate=0.25,
            min_amount=1,
            max_amount=1,
        ),
        Drops(
            item="Soul Gem",
            drop_rate=0.4,
            min_amount=1,
            max_amount=2,
        ),
    ]
)

ancient_golem = Enemy(
    name="Ancient Golem",
    current_health=650,
    max_health=650,
    attack=25,
    max_attack=35,
    armour=35,
    drops=[
        Drops(
            item="Steel Ingot",
            drop_rate=0.8,
            min_amount=4,
            max_amount=8,
        ),
    ]
)

demon_lord = Enemy(
    name="Demon Lord",
    current_health=500,
    max_health=500,
    attack=34,
    max_attack=44,
    armour=25,
    drops=[
        Drops(
            item="Infernal Core",
            drop_rate=0.5,
            min_amount=1,
            max_amount=2,
        ),
        Drops(
            item="Demon Horn",
            drop_rate=0.8,
            min_amount=2,
            max_amount=5,
        ),
    ]
)

low = (
    rat,
    spider,
    skeleton,
    wolf,
    zombie,
)

mid = (
    goblin,
    orc,
    bandit,
    giant_spider,
)

high = (
    troll,
    werewolf,
    dark_knight,
    golem,
)

elite = (
    dragon,
    lich,
    ancient_golem,
    demon_lord,
)