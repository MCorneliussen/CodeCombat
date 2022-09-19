# Help out on the front line.
# Move back to a flag if any try to sneak by.
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    if flag:
        hero.pickUpFlag(flag)
    if enemy and hero.distanceTo(enemy) < 15:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
    if enemy and hero.distanceTo(enemy) < 30:
        hero.attack(enemy)
    else:
        hero.moveXY(31, 39)
        pass

