from typing import Any
import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y) :
        super().__init__()
        self.frame_1 = pygame.image.load("Circle_explosion\\Circle_explosion1.png")
        self.frame_2 = pygame.image.load("Circle_explosion\\Circle_explosion2.png")
        self.frame_3 = pygame.image.load("Circle_explosion\\Circle_explosion3.png")
        self.frame_4 = pygame.image.load("Circle_explosion\\Circle_explosion4.png")
        self.frame_5 = pygame.image.load("Circle_explosion\\Circle_explosion5.png")
        self.frame_6 = pygame.image.load("Circle_explosion\\Circle_explosion6.png")
        self.frame_7 = pygame.image.load("Circle_explosion\\Circle_explosion7.png")
        self.frame_8 = pygame.image.load("Circle_explosion\\Circle_explosion8.png")
        self.frame_9 = pygame.image.load("Circle_explosion\\Circle_explosion9.png")
        self.frame_10 = pygame.image.load("Circle_explosion\\Circle_explosion10.png")
        self.frames = [self.frame_1,self.frame_2,self.frame_3,self.frame_4,self.frame_5,
                       self.frame_6,self.frame_7,self.frame_8,self.frame_9,self.frame_10]
        
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x,pos_y)
    def update(self):
        self.rect.x -= 10
        self.current_frame += 0.5
        if self.current_frame >= len(self.frames):
            self.kill()
            self.current_frame = 0
        self.image = self.frames[int(self.current_frame)]