import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
vos = Actor('fox')
vos.pos = 100, 100

munt = Actor('coin')
munt.pos = 200, 200

def draw():
    screen.fill('lime green')
    vos.draw()
    munt.draw()
    screen.draw.text('Score: ' + str(score), color='black', topleft=(10, 10))

    if game_over:
        screen.fill('pink')
        screen.draw.text('Eindscore: ' + str(score), topleft=(10, 10), fontsize=60)
                         
def plaats_munt():
    munt.x = randint(20, (WIDTH - 20))
    munt.y = randint(20, (HEIGHT -20))

def tijd_om():
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:
        vos.x = vos.x - 15
    elif keyboard.right:
        vos.x = vos.x + 15
    elif keyboard.up:
        vos.y = vos.y - 15
    elif keyboard.down:
        vos.y = vos.y + 15

    munt_verzameld = vos.colliderect(munt)

    if munt_verzameld:
        score = score + 10
        plaats_munt()
        
clock.schedule(tijd_om, 30.0)
plaats_munt()
pgzrun.go()
