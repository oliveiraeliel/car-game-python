from ursina import *
from ursina import texture
from ursina import text
import random

app = Ursina()
camera.orthographic = True
camera.fov = 20

car = Entity(
    model='quad',
    texture='assets\car2',
    collider='box',
    scale=(4, 2),
    rotation_z=-90
)

road1 = Entity(
    model='quad',
    texture='assets\\road2',
    scale=25,
    z=1,
    rotation_z=-90
)

road2 = duplicate(road1, y=15)
pair = [road1, road2]

enemies = []


def newEnemy():
    val = random.uniform(-5, 5)
    new = duplicate(
        car,
        texture='assets\enemy',
        x=2*val,
        y=15,
        color=color.random_color(),
        rotation_z= -90 if val > 0
        else 90
    )
    enemies.append(new)
    invoke(newEnemy, delay=0.5)


newEnemy()


def update():
    car.x += held_keys['d']*10*time.dt
    car.x -= held_keys['a']*10*time.dt
    for road in pair:
        road.y -= 10*time.dt
        if road.y < -15:
            road.y += 30
    for enemy in enemies:
        if enemy.x < 0:
            enemy.y -= 25*time.dt
        else:
            enemy.y -= 15*time.dt
        if enemy.y < -15:
            enemies.remove(enemy)
            destroy(enemy)
        if car.intersects().hit:
            car.shake()
app.run()
