import pgzrun
from random import randint
appel = Actor('apple')

WIDTH = 500
HEIGHT = 300

def draw():
    screen.clear()
    appel.draw()
    
def plaats_appel():
    appel.x = randint(10, 800)
    appel.y = randint(10, 600)
    appel.x = 300
    appel.y = 200
    
def on_mouse_down(pos):
    if appel.collidepoint(pos):
      print('Goed shot!')
      plaats_appel()
    else:
      print('Je hebt gemist!')
      exit()
      plaats_appel()
pgzrun.go()

