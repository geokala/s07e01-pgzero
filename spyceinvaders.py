WIDTH = 800
HEIGHT = 600

spyceship = Actor('cake')
spyceship.bottom = HEIGHT
spyceship.x = WIDTH/2

def draw():
    screen.clear()
    spyceship.draw()
