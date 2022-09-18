# Collect coins to repair the cart while staying close to the peasant!

while True:
    item = hero.findNearestItem()
    # Change the if-statement to check if the distance from the hero to the coin is less than 15.
    if item and item.type == "coin" and hero.distanceTo(item) < 15:
        hero.moveXY(item.pos.x,item.pos.y)
        # Move to the red X after collecting the coin.
        hero.moveXY(42, 45)
