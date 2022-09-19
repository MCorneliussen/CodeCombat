# Help your friends beat the minions that Thoktar sends against you.
# You'll need great equipment and strategy to win.
# Flags might help, but it's up to you–be creative!
# There is a doctor behind the fence. Move to the X to get healed!

while True:
    green = hero.findFlag("green")
    black = hero.findFlag("black")
    enemy = hero.findNearestEnemy()
    if black and hero.canCast("invisibility"):
        hero.cast("invisibility", hero)
        hero.pickUpFlag(black)
    if green:
        hero.pickUpFlag(green)
    elif enemy and hero.isReady("bash"):
        hero.attack(enemy)
    elif enemy:
        hero.attack(enemy)
    pass
