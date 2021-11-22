import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
MIDDEN_X = WIDTH / 2
MIDDEN_Y = HEIGHT / 2

beweging_lijst = []
toon_lijst = []

score = 0
huidige_beweging = 0
tel = 4
dans_lengte = 4

zeg_dans = False
toon_aftellen = True
bewegingen_voltooid = False
game_over = False

danser = Actor('dancer-start')
danser.pos = MIDDEN_X + 5, MIDDEN_Y - 40

omhoog = Actor('up')
omhoog.pos = MIDDEN_X, MIDDEN_Y + 110
rechts = Actor('right')
rechts.pos = MIDDEN_X + 60, MIDDEN_Y + 170
omlaag = Actor('down')
omlaag.pos = MIDDEN_X, MIDDEN_Y + 170
links = Actor('left')
links.pos = MIDDEN_X - 60, MIDDEN_Y + 170

def draw():
    global game_over, score, zeg_dans
    global count, toon_aftellen
    if not game_over:
        screen.clear()
        screen.blit('stage', (0, 0))
        danser.draw()
        omhoog.draw()
        omlaag.draw()
        rechts.draw()
        links.draw()
        screen.draw.text('Score: ' +
                         str(score), color='black',
                         topleft=(10, 10))
        return
    
def reset_danser():
    global game_over
    if not game_over:
        if beweging == 0:
            omhoog.image = 'up-lit'
            danser.image = 'dancer-up'
            clock.shedule(reset_danser, 0.5)
        elif beweging == 1:
            rechts.image = 'right-lit'
            danser.image = 'dancer-right'
            

def update_danser(beweging):
    pass

def toon_bewegingen():
    pass

def genereer_bewegingen():
    pass

def aftelen():
    pass

def volgonde_beweging():
    pass

def on_key_up(toets):
    pass

def update():
    pass

pgzrun.go()
