import random

class Drops():
    def __init__(self, item, drop_rate, min_amount, max_amount):
        self.item = item
        self.drop_rate = drop_rate
        self.min_amount = min_amount
        self.max_amount = max_amount

def gather(area, backpack):
    for drop in gather_area[area]:
        chance = random.random()
        if chance <= drop.drop_rate:
            amount = random.randint(drop.min_amount, drop.max_amount)
            backpack.pick_item(drop.item, amount)
            print(f"You found and gathered {amount}x {drop.item}")

gather_area = {
    '1': (Drops(item='Water', drop_rate=1, min_amount=1, max_amount=3),
            Drops(item='Sharp Stone', drop_rate=0.7, min_amount=1, max_amount=3),
            Drops(item='Feather', drop_rate=0.7, min_amount=1, max_amount=3)
            ),
    '2': (Drops(item='Herb', drop_rate=1, min_amount=2, max_amount=4),
            Drops(item='Feather', drop_rate=0.7, min_amount=1, max_amount=4),
            Drops(item='Sharp Stone', drop_rate=0.7, min_amount=1, max_amount=3)
            )
}
