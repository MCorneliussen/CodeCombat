# Be the first to 100 gold!
# If you are defeated, you will respawn at 67% gold.

while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 15 and hero.canCast("drain-life"):
        hero.cast("drain-life", enemy)
    else:
        item = hero.findNearestItem()
        if item.type == "coin":
            hero.moveXY(item.pos.x, item.pos.y)
            pass
