# Get to the Oasis by moving down 10m at a time.
# Build fences 20m to the left of each ogre.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # buildXY a "fence" 20 meters to enemy's left.
        ex = enemy.pos.x - 20
        ey = enemy.pos.y
        hero.buildXY("fence", ex, ey)
        pass
    else:
        # moveXY down 10 meters.
        hx = hero.pos.x
        hy = hero.pos.y - 10
        hero.moveXY(hx, hy)
        pass
