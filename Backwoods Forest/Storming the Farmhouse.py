# Soldiers will slowly arrive, but the ogres will overwhelm them.
# A basic attack loop isn't going to be enough to keep you alive.
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    
    if flag:
        hero.pickUpFlag(flag)
    else:
        if enemy:
            hero.attack(enemy)
            pass
