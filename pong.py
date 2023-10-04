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


class Ball(GameSprite):
    def update(self):
        global speedx
        global speedy
        global score_1
        global score_2

        self.rect.x += speedx
        self.rect.y += speedy

        if self.rect.y <= 0 or self.rect.y >= 450:
            speedy *= -1

        if self.rect.x <= -50:
            score_2 += 1
            self.rect.x = 250
            self.rect.y = 350
        if self.rect.x >= 700:
            score_1 += 1
            self.rect.x = 250
            self.rect.y = 350
        
        if self.rect.colliderect(p1.rect):
            speedx = 7 
            speedy *= -1
        if self.rect.colliderect(p2.rect):
            speedx = -7
            speedy *= -1



WINDOW_SIZE = (700, 500)
FPS = 60
window = display.set_mode(WINDOW_SIZE)
background = (0, 153, 153)
font.init()
font = font.SysFont("Arial", 50)

p1 = Player(10, 200, 5, "pong_p1.png", 50, 100)
score_1 = 0
p2 = Player(640, 200, 5, "pong_p1.png", 50, 100)
score_2 = 0
ball = Ball(250, 300, 0, "ball.png", 50, 50)
speedx = 7
speedy = 5
clock = time.Clock()
running = True
finished = False


while running:
    for e in event.get():
        if e.type == QUIT:
            running = False  

    if finished != True:
        window.fill(background)
        p1.reset()
        p2.reset()
        ball.reset()

        p1.update()
        p1.update()
        ball.update()

        if score_1 >= 3:
            finished = True
            text1 = font.render("Player 1 wins", False, (50, 50, 50))
            window.blit(text1, (250, 200))
        if score_2 >= 3:
            finished = True
            text1 = font.render("Player 2 wins", False, (50, 50, 50))
            window.blit(text1, (250, 200))

    display.update()
    clock.tick(FPS)
