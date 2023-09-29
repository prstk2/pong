from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, x, y, speed, img, imgx, imgy):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(img), (imgx, imgy))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and p1.rect.y > 10:
            p1.rect.y -= p1.speed
        if keys_pressed[K_s] and p1.rect.y < 390:
            p1.rect.y += p1.speed
        
        if keys_pressed[K_i] and p2.rect.y > 10:
            p2.rect.y -= p2.speed
        if keys_pressed[K_k] and p2.rect.y < 390:
            p2.rect.y += p2.speed


WINDOW_SIZE = (700, 500)
FPS = 60
window = display.set_mode(WINDOW_SIZE)
black = (10, 40, 50)

p1 = Player(10, 200, 5, "pong_p1.png", 50, 100)
p2 = Player(640, 200, 5, "pong_p1.png", 50, 100)

clock = time.Clock()
running = True

while running:
    window.fill(black)
    for e in event.get():
        if e.type == QUIT:
            running = False  
    
    p1.reset()
    p2.reset()

    p1.update()
    p1.update()

    display.update()
    clock.tick(FPS)
