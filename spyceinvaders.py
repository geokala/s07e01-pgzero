WIDTH = 800
HEIGHT = 600

spyceship = Actor('cake')
spyceship.bottom = HEIGHT
spyceship.centerx = WIDTH/2
projectiles= list()
enemies= list()

for i in range(5):
    enemy = Actor('space-invaders')
    enemy.top = 0
    enemy.centerx = WIDTH/2 + 100*(i - 2)
    enemies.append(enemy)
    enemy.direction = "right"

def draw():
    screen.clear()
    spyceship.draw()
    for projectile in projectiles:
        projectile.draw()
    for enemy in enemies:
        enemy.draw()

def update():
    for projectile in projectiles:
        projectile.y -= 10
        i = projectile.collidelist(enemies)
        if i != -1:
            del enemies[i]
            projectiles.remove(projectile)
        elif projectile.bottom <= 0:
            projectiles.remove(projectile)
    for enemy in enemies:
        if enemy.direction == "right":
            enemy.x += 5
            if enemy.right > WIDTH:
                enemy.x -= 5
                enemy.y += 50
                enemy.direction = "left"
        elif enemy.direction == "left":
            enemy.x -= 5
            if enemy.left < 0:
                enemy.x += 5
                enemy.y += 50
                enemy.direction = "right"
            

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
    

