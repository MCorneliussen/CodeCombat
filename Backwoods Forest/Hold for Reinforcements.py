# Ogres are climbing the cliffs!
# Protect the peasants long enough for the militia to assemble.
while True:
    green = hero.findFlag("green")
    black = hero.findFlag("black")
    enemy = hero.findNearestEnemy()
    
    if green:
        hero.pickUpFlag(green)
    
    elif black and hero.isReady("cleave"):
        # Else, attack!
        # Use flags to move into position, and 'cleave' if ready.
        hero.pickUpFlag(black)
        hero.cleave(enemy)

    elif enemy and hero.distanceTo(enemy) < 10:
        hero.attack(enemy)
        pass
