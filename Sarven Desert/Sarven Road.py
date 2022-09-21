# Get to the oasis. Watch out for new enemies: ogre scouts!
# Go up and right by adding to the current X and Y position.

while True:
    # If there's an enemy, attack.
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.canCast("drain-life", hero.findNearestEnemy())
        hero.cast("drain-life", enemy)
    # Else, keep moving up and to the right. 
    else:
        x = hero.pos.x + 5
        y = hero.pos.x + 5
    hero.moveXY(x, y)
    pass
    
