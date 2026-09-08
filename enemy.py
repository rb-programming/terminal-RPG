class Enemy:
    def __init__(self, name, current_health, attack, max_attack, armour, drops):
        self.name = name
        self.current_health = current_health
        self.attack = attack
        self.max_attack = max_attack
        self.armour = armour
        self.drops = drops

    def get_damaged(self, amount):
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


skeleton = Enemy(
    name="Skeleton",
    current_health=100,
    attack=5, 
    max_attack=10, 
    armour=2,
    drops=[Drops(
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
        Drops(
            item="Coin",
            drop_rate=0.4,
            min_amount=10,
            max_amount=20,
        )
        ]
)

spider = Enemy(
    name="Spider",
    current_health=100,
    attack=4,
    max_attack=6,
    armour=4,
    drops=[Drops(
        item="Spider eye",
        drop_rate=0.4,
        min_amount=1,
        max_amount=8,
    ),
    Drops(
        item="Spider leg",
        drop_rate=0.8,
        min_amount=1,
        max_amount=8,
        )
    ]
)

low = (skeleton, spider)
mid = (skeleton, spider)
high = (skeleton, spider)
elite = (skeleton, spider)