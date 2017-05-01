import pygame, sys
from pygame.locals import *

import time
from random import randint
class Pingvin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("pingvin1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.right = True
    def höger(self):
        if self.rect.x + self.rect.width < 700:
            self.rect.x += self.rect.width
    def vänster(self):
        if self.rect.x > 0:
            self.rect.x -= self.rect.width
class Kniv(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("kniv.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
       
           

pygame.init()
pygame.display.set_caption("Spring från knivarna!")
WHITE = (255,255,255)
screen = pygame.display.set_mode([700,500])
player = Pingvin(0,335)
kniv = Kniv(randint(0,700),0)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
all_sprites_list.add(kniv)
kniv_list = pygame.sprite.Group()
kniv_list.add(kniv)


pygame.time.set_timer(USEREVENT + 1, 1000)
score = 0

pygame.mixer.music.load('Kevin MacLeod - There It Is.mp3')
pygame.mixer.music.play(-1)

more = True
while more:
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    if kniv.rect.y < 500:
        kniv.rect.y += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            more = False
        elif event.type == USEREVENT + 1:
            kniv = Kniv(randint(0,700),0)
            all_sprites_list.add(kniv)
            kniv_list.add(kniv)
            score = score + 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if not player.right:
                    player.image = pygame.transform.flip(player.image, True, False)
                    player.right = True
                player.höger()
            elif event.key == pygame.K_LEFT:
                if player.right:
                    player.image = pygame.transform.flip(player.image, True, False)
                    player.right = False
                player.vänster()

    krock_list = pygame.sprite.spritecollide(player,kniv_list,True)
    for krock in krock_list:
        pygame.mixer.music.stop()
        player.image = pygame.transform.flip(player.image, False, True)
        more = False
        screen.fill(WHITE)
        all_sprites_list.draw(screen)
        f = pygame.font.Font("arial.ttf", 32)
        surf = f.render("GAME OVER :(",1,(0,0,0))
        screen.blit(surf, [350,250])
        surf = f.render("Du fick " + str(score) + " poäng",1,(0,0,0))
        screen.blit(surf,[345,275])
        pygame.display.flip()
        
               


