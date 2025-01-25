import pygame
import sys
from pygame.locals import *
import numpy as np  
from numpy import random as rand

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Russian Roulette")

p1_alive = pygame.transform.scale(pygame.image.load('/Users/Turnip/Documents/random python stuff/russian_roulette/p1_alive.jpg'), (200, 200))
p1_dead = pygame.transform.scale(pygame.image.load('/Users/Turnip/Documents/random python stuff/russian_roulette/p1_dead.png'), (200, 200))
p2_alive = pygame.transform.scale(pygame.image.load('/Users/Turnip/Documents/random python stuff/russian_roulette/p2_alive.png'), (200, 200))
p2_dead = pygame.transform.scale(pygame.image.load('/Users/Turnip/Documents/random python stuff/russian_roulette/p2_dead.png'), (200, 200))

idle_gun_left = pygame.transform.scale(pygame.image.load('/Users/Turnip/Documents/random python stuff/russian_roulette/idle_gun.png'), (200, 200))
idle_gun_right = pygame.transform.flip(idle_gun_left, True, False)
fail_gun_left = pygame.transform.scale(pygame.image.load('/Users/Turnip/Documents/random python stuff/russian_roulette/failure-2.gif'), (200, 200))
fail_gun_right = pygame.transform.flip(fail_gun_left, True, False)
shoot_gun_left = pygame.transform.scale(pygame.image.load('/Users/Turnip/Documents/random python stuff/russian_roulette/shoot.gif'), (200, 200))
shoot_gun_right = pygame.transform.flip(shoot_gun_left, True, False)

shoot_audi = pygame.mixer.Sound('/Users/Turnip/Documents/random python stuff/russian_roulette/shoot.mp3')
blank_audi = pygame.mixer.Sound('/Users/Turnip/Documents/random python stuff/russian_roulette/blank.mp3')

game_over = False

turn = 1

running = True

colour = (100,100,100) 
smallfont = pygame.font.SysFont('Ariel',35)
subtext = smallfont.render('RESTART', True, colour) 

while running:
    mouse = pygame.mouse.get_pos()

    screen.fill((255, 255, 255)) 

    screen.blit(p1_alive if not game_over or turn == 2 else p1_dead, p1_alive.get_rect(midleft=(100, height // 2)))
    screen.blit(p2_alive if not game_over or turn == 1 else p2_dead, p2_alive.get_rect(midright=(width - 100, height // 2)))
    gun = idle_gun_left if turn == 1 else idle_gun_right
    screen.blit(gun, gun.get_rect(center=(width // 2, height // 2)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x = rand.randint(5)  
            if x == 0:  
                if turn == 1: 
                    screen.blit(shoot_gun_left, shoot_gun_left.get_rect(center=(width // 2, height // 2)))
                    screen.blit(p1_dead, p1_dead.get_rect(midleft=(100, height // 2)))
                    shoot_audi.play()
                    game_over = True
                else:  
                    screen.blit(shoot_gun_right, shoot_gun_right.get_rect(center=(width // 2, height // 2)))
                    screen.blit(p2_dead, p2_dead.get_rect(midright=(width - 100, height // 2)))
                    shoot_audi.play()
                    game_over = True
            else:  
                blank_audi.play()
                turn = 2 if turn == 1 else 1  

    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, text.get_rect(center=(width // 2, 100)))
        screen.blit(subtext , (width//2,height/2 + 10)) 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                game_over = False
        

    pygame.display.update()
    clock.tick(30)

pygame.quit()