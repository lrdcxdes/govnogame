import pygame
import random
import time
import threading

WIDTH, HEIGHT = 1280, 720
pygame.init()
pygame.font.init()


import sys
platform = sys.platform

if 'a' in platform or 'linux' in platform:
    background = pygame.image.load('sprites/background.png')
else:
    background = pygame.image.load('sprites/background.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


TT = 59

run = True
def TTMin():
    global TT
    while TT > 0:
        if not run:
            break
        time.sleep(1)
        TT -= 1

thread = threading.Thread(target=TTMin).start()


win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Squid game')

programIcon = pygame.image.load('sprites/icon.ico')
pygame.display.set_icon(programIcon)


class Fox():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.lasty = y
        self.width = width
        self.height = height

        self.win = False
    
        self.rnd = random.randint(1, 7)
        self.rnd2 = random.randint(1, 3)

        self.T = time.time()

        self.status = True

        images = pygame.image.load(image)
        self.image = pygame.transform.scale(images, (self.width, self.height))
    
    def draw(self):
        
        image = self.image
        if self.win:
            image = pygame.transform.rotate(image, 90)
        elif not self.status:
            image = pygame.transform.flip(image, True, False)
        win.blit(image, (self.x, self.y))
    
    def now(self):
        self.status = True
    
    def upd(self):
        self.status = False

fox = Fox(WIDTH - 140, round(HEIGHT/2) - 160 // 2, 140, 160, 'sprites/fox.png')



rect_dye = pygame.Rect(200, (HEIGHT // 2) - 250, 600, 200)
def fill_win():
    font = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = font.render('Нажмите ESC чтобы повторить', False, (255, 0, 0))
    textsurface2 = font.render('Вы выиграли!', False, (0, 255, 0))
    win.blit(textsurface2, (240, (HEIGHT // 2) - 170))
    win.blit(textsurface, (240, (HEIGHT // 2) - 200))
    pygame.draw.rect(win, (0, 0, 0), rect_dye, 1)
    pygame.display.update()


def fill_dye():
    font = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = font.render('Нажмите ESC чтобы повторить', False, (255, 0, 0))
    win.blit(textsurface, (240, (HEIGHT // 2) - 180))
    pygame.draw.rect(win, (0, 0, 0), rect_dye, 1)

    #pygame.draw.line(surface=win, color=(255, 0, 0), width=3, start_pos=(fox.x + fox.width // 2, fox.y + 20), end_pos=(player.x + 20, player.y + 70))

    pygame.display.update()



def draw_time():
    font = pygame.font.SysFont('Arial', 30)
    textsurface = font.render('0:'+str(TT), False, (0, 0, 255))
    win.blit(textsurface, ((WIDTH // 2) - 30, 10))





class Player():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.speed = 5

        self.win = False

        self.di = False
        #image = 1
        self.status = 'idle'
        #images = pygame.image.load(image)
        #self.image = pygame.transform.scale(images, (self.width, self.height))
    
    def draw(self):
        if self.win:
            for i in range(11):
                #win.fill((255, 255, 255))
                win.blit(background, (0, 0))
                pygame.draw.line(surface=win, color=(255, 0, 0), width=4, start_pos=(fox.x, 0), end_pos=(fox.x, HEIGHT))
                if self.x + self.width // 2 >= fox.x:
                    self.win = True
                    fox.win = True
                    if fox.y <= fox.lasty:
                        fox.y += 20
                else:
                    T = time.time()
                    if T - fox.T >= fox.rnd:
                        fox.upd()
                        if T - fox.T >= fox.rnd+fox.rnd2:
                            fox.T = time.time()
                            fox.rnd = random.randint(1, 5)
                            fox.rnd2 = random.randint(1, 3)
                            fox.now()
                fox.draw()
                images = pygame.image.load('sprites/player/kick/{}.png'.format(i))
                image = pygame.transform.scale(images, (self.width, self.height))
                win.blit(image, (self.x, self.y))
                draw_time()
                if player.win:
                    fill_win()
                elif player.di:
                    fill_dye()
                else:
                    pygame.display.update()
                time.sleep(.01)
            return
        if self.status == 'dying':
            images = pygame.image.load('sprites/player/dying/{}.png'.format(14))
            image = pygame.transform.scale(images, (self.width, self.height))
        elif self.status == 'idle':
            images = pygame.image.load('sprites/player/idle/11.png')
            image = pygame.transform.scale(images, (self.width, self.height))
        elif self.status == 'walking':
            for i in range(17):
                #win.fill((255, 255, 255))
                win.blit(background, (0, 0))
                pygame.draw.line(surface=win, color=(255, 0, 0), width=4, start_pos=(fox.x, 0), end_pos=(fox.x, HEIGHT))
                if self.x + self.width // 2 >= fox.x:
                    self.win = True
                    fox.win = True
                    if fox.y <= fox.lasty:
                        fox.y += 20
                else:
                    T = time.time()
                    if T - fox.T >= fox.rnd:
                        fox.upd()
                        if T - fox.T >= fox.rnd+fox.rnd2:
                            fox.T = time.time()
                            fox.rnd = random.randint(1, 5)
                            fox.rnd2 = random.randint(1, 3)
                            fox.now()
                fox.draw()
                images = pygame.image.load('sprites/player/walking/{}.png'.format(i))
                image = pygame.transform.scale(images, (self.width, self.height))
                win.blit(image, (self.x, self.y))
                draw_time()
                if player.win:
                    fill_win()
                elif player.di:
                    fill_dye()
                else:
                    pygame.display.update()
            return
        win.blit(image, (self.x, self.y))

    def run(self):
        self.status = 'walking'
    def idle(self):
        self.status = 'idle'
    def dye(self):
        self.di = True
        self.status = 'dying'


player = Player(100, round(HEIGHT/2) - 110 // 2, 100, 110, 'sprites/player')

def fill():
    #win.fill((255, 255, 255))
    win.blit(background, (0, 0))
    pygame.draw.line(surface=win, color=(255, 0, 0), width=4, start_pos=(fox.x, 0), end_pos=(fox.x, HEIGHT))
    if player.x + player.width // 2 >= fox.x:
        player.win = True
        fox.win = True
        if fox.y <= fox.lasty:
            fox.y += 20
    elif player.di:
        pass
    else:
        T = time.time()
        if T - fox.T >= fox.rnd:
            fox.upd()
            if T - fox.T >= fox.rnd+fox.rnd2:
                fox.T = time.time()
                fox.rnd = random.randint(1, 5)
                fox.rnd2 = random.randint(1, 3)
                fox.now()
    fox.draw()
    player.draw()

clock = pygame.time.Clock()
#run = True
while run:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            exit()
    keys = pygame.key.get_pressed()
    smouse = pygame.mouse.get_pressed(num_buttons=3)[0]
    if keys[pygame.K_SPACE] or keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_w] or smouse:
        if not player.di:
            player.x += player.speed
            player.run()
            T = time.time()
            if T - fox.T >= fox.rnd:
                player.dye()
    elif keys[pygame.K_ESCAPE]:
        player = Player(100, round(HEIGHT/2) - 110 // 2, 100, 110, 'sprites/player')
    elif not player.di:
        player.idle()
    else:
        player.dye()
    
    if TT <= 0:
        player.dye()
    
    fill()
    draw_time()
    if player.win:
        fill_win()
    elif player.di:
        fill_dye()
    else:
        pygame.display.update()