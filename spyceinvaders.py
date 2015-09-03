WIDTH = 800
HEIGHT = 600

spyceship = Actor('cake')
spyceship.bottom = HEIGHT
spyceship.centerx = WIDTH/2

def draw():
    screen.clear()
    spyceship.draw()

def on_key_down(key):
    if key ==keys.LEFT:
        spyceship.x -= 50
    if key==keys.RIGHT:
        spyceship.x+=50

