def have_heal(backpack):
    available_consumables = {}
    for item in consumables:
        if item in backpack.itemdict:
            if backpack.itemdict[item] != 0:
                available_consumables[item] = backpack.itemdict[item]
    return available_consumables

def heal(player, item):
    if player.current_health + consumables[item]:
        player.current_health = player.max_health
    else:
        player.current_health += consumables[item]

consumables = {
    "Bandage": 30,
    "Health Potion": 80,
    "Greater Health Potion": 1000,
}