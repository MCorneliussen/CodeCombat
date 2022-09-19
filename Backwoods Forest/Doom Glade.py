# An ogre army approaches. Use flags to win the battle!
while True:
    green = hero.findFlag("green")
    black = hero.findFlag("black")
    enemy = hero.findNearestEnemy()
    if black and hero.canCast("invisibility"):
        hero.cast("invisibility", hero)
        hero.pickUpFlag(black)
    if green:
        hero.pickUpFlag(green)
        distance = hero.distanceTo(enemy)
        if hero.isReady("cleave") and distance < 5:
            hero.cleave(enemy)
    elif enemy and hero.isReady("bash"):
        hero.attack(enemy)
    elif enemy:
        hero.attack(enemy)

#gear check level, the ring "The Precious" is what i used.
