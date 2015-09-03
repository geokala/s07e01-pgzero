WIDTH = 800
HEIGHT = 600

spyceship = Actor('cake')
spyceship.bottom = HEIGHT
spyceship.centerx = WIDTH/2
projectiles= list()

def draw():
    screen.clear()
    spyceship.draw()
    for projectile in projectiles:
        projectile.draw()

def update():
    for projectile in projectiles:
        projectile.y -= 10
        if projectile.bottom <= 0:
            projectiles.remove(projectile)

def on_key_down(key):
    if key ==keys.LEFT:
        spyceship.x -= 50
    if key==keys.RIGHT:
        spyceship.x+=50
    if key==keys.SPACE:
         fire()

def fire():
    projectile=Actor('long-arrow-up')
    projectile.midbottom = spyceship.midtop
    projectiles.append(projectile)
    

