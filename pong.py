from pygame import *


WINDOW_SIZE = (700, 500)
FPS = 60
window = display.set_mode(WINDOW_SIZE)


clock = time.Clock()
running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False  

    display.update()
    clock.tick(FPS)