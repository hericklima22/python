import pyxel as px
from math import sqrt

x, y = 90, 60
radius = 5
velocity = 1

def update():
    global y, velocity
    
    if px.btnp(px.MOUSE_BUTTON_LEFT):
        dx =px.mouse_x - x
        dy = px.mouse_y - y
        if sqrt(dx ** 2 + dy ** 2) < radius:
            velocity = 0
    y += velocity


def draw():
    px.cls(px.COLOR_BLACK)
    color = px.COLOR_WHITE
    if velocity == 0:
        color = px.COLOR_RED
    px.circ(x, y, radius, color)

    if velocity == 0:
        px.text(70, 10, "Parabens", px.COLOR_WHITE)

px.init(180, 120, "Game")
px.mouse(True)
px.run(update, draw)