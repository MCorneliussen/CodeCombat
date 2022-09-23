# Get the hero and the peasant to the south.

# The function move your hero down along the center line.
def moveDownCenter():
    hx = 40
    hy = hero.pos.y - 12
    hero.moveXY(hx, hy)

# The function build a fence on the right of something.
def buildRightOf(something):
    # buildXY a "fence" 20 meters to something's right.
    cx = coin.pos.x + 20
    cy = coin.pos.y
    hero.buildXY("fence", cx, cy)
    pass

# The function build a fence on the left of something.
def buildLeftOf(something):
    # buildXY a "fence" 20 meters to something's left.
   
    ox = ogre.pos.x - 20
    oy = ogre.pos.y
    hero.buildXY("fence", ox, oy)
    pass

while True:
    ogre = hero.findNearestEnemy()
    coin = hero.findNearestItem()
    if ogre:
        buildLeftOf(ogre)
    if coin:
        buildRightOf(coin)
    moveDownCenter()
