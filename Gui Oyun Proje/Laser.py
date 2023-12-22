import pygame

class Double_Laser1(pygame.sprite.Sprite):
    def __init__(self,pos,speed = 15):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert_alpha()
        self.rect = self.image.get_rect(center = (pos.x,pos.y+60))
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
class Double_Laser2(pygame.sprite.Sprite):
    def __init__(self,pos,speed = 15):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert_alpha()
        self.rect = self.image.get_rect(center = (pos.x,pos.y))
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed = 15):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
class LaserFourWays1(pygame.sprite.Sprite):
    def __init__(self,pos,speed = 15):
        super().__init__()
        self.image = pygame.image.load("laser.diaganel.png").convert_alpha()
        self.rect = self.image.get_rect(center = (pos.x+15,pos.y+25))
        self.speed = speed
    def update(self):
        self.rect.y += self.speed
class LaserFourWays2(pygame.sprite.Sprite):
    def __init__(self,pos,speed = 15):
        super().__init__()
        self.image = pygame.image.load("laser.diaganel.png").convert_alpha()
        self.rect = self.image.get_rect(center = (pos.x+15,pos.y+25))
        self.speed = speed
    def update(self):
        self.rect.y -= self.speed
class LaserFourWays3(pygame.sprite.Sprite):
    def __init__(self,pos,speed = 15):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert_alpha()
        self.rect = self.image.get_rect(center = (pos.x+15,pos.y+25))
        self.speed = speed
    def update(self):
        self.rect.x -= self.speed
class LaserFourWays4(pygame.sprite.Sprite):
    def __init__(self,pos,speed = 15):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert_alpha()
        self.rect = self.image.get_rect(center = (pos.x+15,pos.y+25))
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
class Laser_Const(pygame.sprite.Sprite):
    def __init__(self,pos,screen):
        super().__init__()
        self.pos = pos
        self.image = pygame.Surface((screen.get_width(),5))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(midleft = pos)
        pygame.draw.rect(screen,(255,255,255),self.rect)
    def update(self):
        self.rect.midleft = self.pos
        
        

        
        