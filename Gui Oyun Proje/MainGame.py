import pygame,sys,random,math    
from Laser import *
from explosion import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
DIFFUCULTY = [400,4000]
laser_types_list = ["Single","Double","FourWay","Const"]
SCORE = 0

#Objects
class Enemy(pygame.sprite.Sprite):
    def __init__(self,min_speed,max_speed):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.image = pygame.transform.rotate(self.image,(random.randint(-270,270)))
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH+200,random.randint(10,SCREEN_HEIGHT-100)))
        self.min_speed = min_speed
        self.max_speed = max_speed
    def killit(self):
        if self.rect.x <= -100:
            self.kill()
    def update(self) :
        self.rect.x -= random.randint(self.min_speed,self.max_speed)
        self.killit()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Main Ship - Base - Full health.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.image = pygame.transform.rotate(self.image,-90)
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        self.movement_speed = 4
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 250
        self.lasers = pygame.sprite.Group()
        self.lasers_const = pygame.sprite.GroupSingle()
        self.laser_type = None
        self.types = "Double"
        self.has_power_up = False
        self.power_up_blast_time = 0
        self.power_up_cooldown = 3500
    def collison(self):
        if pygame.sprite.spritecollide(player.sprite,laser_types1,True):
            self.types = "Single"
        if pygame.sprite.spritecollide(player.sprite,laser_types2,True):
            self.types = "Double"
            self.has_power_up = True
            self.power_up_blast_time = pygame.time.get_ticks()
        if pygame.sprite.spritecollide(player.sprite,laser_types3,True):
            self.types = "FourWay"
            self.has_power_up = True 
            self.power_up_blast_time = pygame.time.get_ticks()
        if pygame.sprite.spritecollide(player.sprite,laser_types4,True):
            self.types = "Const"
            self.has_power_up = True 
            self.power_up_blast_time = pygame.time.get_ticks()
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center))
    def shoot_double_laser(self):   
        self.lasers.add(Double_Laser1(self.rect))
        self.lasers.add(Double_Laser2(self.rect))         
    def shoot_four_laser(self):
        self.lasers.add(LaserFourWays1(self.rect))
        self.lasers.add(LaserFourWays2(self.rect))
        self.lasers.add(LaserFourWays3(self.rect))
        self.lasers.add(LaserFourWays4(self.rect))
    def shoot_constant(self):
        self.lasers_const.add(Laser_Const(self.rect.center,screen))

        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.movement_speed
        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.movement_speed
        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.movement_speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.movement_speed
        if keys[pygame.K_SPACE] and self.ready == True and self.types == "Single":
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            laser_shoot_Sound.play()
        if keys[pygame.K_SPACE] and self.ready == True and self.types == "Double":
            self.shoot_double_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            laser_shoot_Sound.play()
            laser_shoot_Sound.play()
        if keys[pygame.K_SPACE] and self.ready == True and self.types == "FourWay":
            self.shoot_four_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            laser_shoot_Sound.play()
            laser_shoot_Sound.play()            
            laser_shoot_Sound.play()
            laser_shoot_Sound.play()
        if keys[pygame.K_SPACE]  and self.types == "Const":
            self.shoot_constant()
            self.laser_time = pygame.time.get_ticks()
        else:
            self.lasers_const.empty()
    def reset_power_up(self):
        if self.has_power_up:
            reset_current_time = pygame.time.get_ticks()
            if reset_current_time - self.power_up_blast_time  >= self.power_up_cooldown:
                self.has_power_up = False
                self.lasers.remove()
                
        elif self.has_power_up == False:
            self.types = "Single"
            self.lasers_const.empty()
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True
                
    def update(self):
        self.player_input()
        self.lasers.update()
        self.lasers_const.update()
        self.recharge()
        self.collison()
        self.reset_power_up()
class LaserType1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("single_laser.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH+200,random.randint(10,SCREEN_HEIGHT-100)))
    def update(self) :
        self.rect.x -= 5
class LaserType2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("double_laser.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH+200,random.randint(10,SCREEN_HEIGHT-100)))
    def update(self) :
        self.rect.x -= 5      
class LaserType3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("4 Four Way.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH+200,random.randint(10,SCREEN_HEIGHT-100)))
    def update(self):
        self.rect.x -= 5
class LaserType4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("const_laser.png").convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH+200,random.randint(10,SCREEN_HEIGHT-100)))
    def update(self):
        self.rect.x -= 5

pygame.init()

obstacle_timer = pygame.USEREVENT + 1
obstacle_timer2 = pygame.USEREVENT + 2

DIFFUCULTY[0] = 400
DIFFUCULTY[1] = 4000
pygame.time.set_timer(obstacle_timer,DIFFUCULTY[0])
pygame.time.set_timer(obstacle_timer2,DIFFUCULTY[1])  
DIF_TEXT = "MEDIUM"
min_speed = 5
max_speed = 17
playing = True
game_active = True
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Gui_Proje")

#sound
laser_shoot_Sound = pygame.mixer.Sound("shoot.wav")
enemy_death_Sound = pygame.mixer.Sound("invaderkilled.wav")
pygame.mixer.music.load("VELDA - 8 bit Win (A Nice Final Boss) (Royalty Free Music).wav")

pygame.mixer.Sound.set_volume(laser_shoot_Sound,0.1)
pygame.mixer.Sound.set_volume(enemy_death_Sound,0.1)
pygame.mixer.music.set_volume(0.5)

#background menu
bg_menu = pygame.image.load("Space_Stars6.png").convert()
bg_menu = pygame.transform.scale(bg_menu,(SCREEN_WIDTH,SCREEN_HEIGHT))

#background_game
bg = pygame.image.load("space2_4-frames.png").convert()
bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
bg_width = bg.get_width()
bg_rect = bg.get_rect()
scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1

clock = pygame.time.Clock()
font = pygame.font.Font("PublicPixel-z84yD.ttf",25)
font_menu = pygame.font.Font("PublicPixel-z84yD.ttf",40)
font_menu_dif = pygame.font.Font("PublicPixel-z84yD.ttf",30)

#Player Object
player = pygame.sprite.GroupSingle()
player.add(Player())

#Enemy Object
enemy = pygame.sprite.Group()
enemy.add(Enemy(5,max_speed))

#Laser Objects
laser_types1 = pygame.sprite.Group()
laser_types1.add(LaserType1())
laser_types2 = pygame.sprite.Group()
laser_types3 = pygame.sprite.Group()
laser_types4 = pygame.sprite.Group()

explosion = pygame.sprite.Group()

def play_again():
    global SCORE,playing
    Score_Title_Text = font_menu.render("SCORE",0,"white")
    Score_Title_Rect = Score_Title_Text.get_rect(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//9))
    Score_Text = font_menu.render("YOUR SCORE:" + str(SCORE),0,"white")
    Score_Rect = Score_Text.get_rect(center = (SCREEN_WIDTH//4,SCREEN_HEIGHT//2))
    Play_again_Text = font_menu.render("PLAY AGAIN?",0,"white")
    Play_again_Rect = Play_again_Text.get_rect(center = (SCREEN_WIDTH//1.35,SCREEN_HEIGHT//2))
    Quit_Text = font_menu.render("QUIT",0,"white")
    Quit_Rect = Quit_Text.get_rect(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//1.25 ))
    screen.fill((0,0,0))
    screen.blit(Score_Title_Text,Score_Title_Rect)
    screen.blit(Score_Text,Score_Rect)
    screen.blit(Play_again_Text,Play_again_Rect)
    screen.blit(Quit_Text,Quit_Rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Quit_Rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                if Play_again_Rect.collidepoint(event.pos):
                    playing = True
                    menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        pygame.display.update()
        clock.tick(60)

def collisons():
    global playing,game_active,SCORE
    if pygame.sprite.spritecollide(player.sprite,enemy,False):
        playing = False
       
    if player.sprite.lasers: 
        for laser in player.sprite.lasers:
            if pygame.sprite.spritecollide(laser,enemy,True):
                    explosion.add(Explosion(laser.rect.x,laser.rect.y))
                    laser.kill()
                    SCORE += 1
                    enemy_death_Sound.play()
    if player.sprite.lasers_const:
        for laser in player.sprite.lasers_const:
            if pygame.sprite.spritecollide(laser,enemy,True):
                    explosion.add(Explosion(laser.rect.centerx,laser.rect.centery))
                    SCORE += 1
                    enemy_death_Sound.play()

def draw_score():
    score_text = str(SCORE)
    score_surface = font.render(score_text,False,(255,255,255))
    screen.blit(score_surface,(30,20))

def play():
    pygame.mixer.music.play()
    global scroll,max_speed,SCORE,playing
    SCORE = 0
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == obstacle_timer:
                    enemy.add(Enemy(5,max_speed))   
                if event.type == obstacle_timer2:
                    laser_choice = random.choice(laser_types_list)
                    if laser_choice == "Double":
                        laser_types2.add(LaserType2())
                        
                    elif laser_choice == "FourWay":
                        laser_types3.add(LaserType3())
                        
                    elif laser_choice == "Single":
                        laser_types1.add(LaserType1())
                    
                    elif laser_choice == "Const":
                        laser_types4.add(LaserType4())

        for i in range(0, tiles):
                screen.blit(bg, (i * bg_width + scroll, 0))
                bg_rect.x = i * bg_width + scroll
                
        scroll -= 5
        if abs(scroll) > bg_width:
            scroll = 0
        if playing:
            player.sprite.lasers.draw(screen) 
            player.sprite.lasers_const.draw(screen) 
            laser_types1.draw(screen)
            laser_types1.update()    
            laser_types2.draw(screen)    
            laser_types2.update()    
            laser_types3.draw(screen)    
            laser_types3.update()
            laser_types4.draw(screen)    
            laser_types4.update()  
            enemy.draw(screen)    
            enemy.update()    
            explosion.draw(screen)    
            explosion.update()
            player.draw(screen)
            player.update()
            collisons()    
            draw_score()    
        else:
            enemy.empty()
            player.sprite.lasers.empty()
            laser_types1.empty()
            laser_types2.empty()
            laser_types3.empty()
            explosion.empty()
            player.sprite.rect.x = SCREEN_WIDTH/2
            player.sprite.rect.y = SCREEN_HEIGHT/2
            play_again()
        pygame.display.update()
        clock.tick(60)

def settings():
    global DIFFUCULTY,SCREEN_WIDTH,SCREEN_HEIGHT,screen,bg_menu,bg,bg_width,bg_rect,scroll,tiles,DIF_TEXT,max_speed
    
    while True:
        screen.blit(bg_menu,(0,0))
        Settings_Text = font_menu.render("SETTINGS:",0,"white")
        Settings_Rect = Settings_Text.get_rect(center = (SCREEN_WIDTH//7,SCREEN_HEIGHT//15))
        #Res
        Resolution_Text = font_menu.render("RESOLUTION",0,"white")
        Resolution_Rect = Resolution_Text.get_rect(center = (SCREEN_WIDTH//6.25,SCREEN_HEIGHT//4.5))
        
        Resolution_Text1 = font_menu.render("1280x720",0,"white")
        Resolution_Rect1 = Resolution_Text1.get_rect(center = ((SCREEN_WIDTH//2,SCREEN_HEIGHT//4.5)))
        
        Resolution_Text2 = font_menu.render("1920x1080",0,"white")
        Resolution_Rect2 = Resolution_Text1.get_rect(center = ((SCREEN_WIDTH//1.2,SCREEN_HEIGHT//4.5)))
        
        #Dif
        Diffuculty_text = font_menu_dif.render("DIFFUCULTY",0,"white")
        Diffuculty_rect = Diffuculty_text.get_rect(center =(SCREEN_WIDTH//7,SCREEN_HEIGHT//2))
        
        Diffuculty_text1 = font_menu_dif.render("EASY",0,"white")
        Diffuculty_rect1 = Diffuculty_text1.get_rect(center =(SCREEN_WIDTH//2.35,SCREEN_HEIGHT//2))
        
        Diffuculty_text2 = font_menu_dif.render("MEDIUM",0,"white")
        Diffuculty_rect2 = Diffuculty_text2.get_rect(center =(SCREEN_WIDTH//1.75,SCREEN_HEIGHT//2))

        Diffuculty_text3 = font_menu_dif.render("HARD",0,"white")
        Diffuculty_rect3 = Diffuculty_text3.get_rect(center =(SCREEN_WIDTH//1.35,SCREEN_HEIGHT//2))

        Diffuculty_text4 = font_menu_dif.render("EXTREME",0,"white")
        Diffuculty_rect4 = Diffuculty_text4.get_rect(center =(SCREEN_WIDTH//1.1,SCREEN_HEIGHT//2))

        Back_text = font_menu.render("BACK",0,"white")
        Back_rect = Back_text.get_rect(center =(SCREEN_WIDTH//6.25,SCREEN_HEIGHT//1.25))
        
        Diffuculty_Shower_Text = font_menu.render("DIFFUCULTY:" + DIF_TEXT,0,"white")
        Diffuculty_Shower_rect = Diffuculty_Shower_Text.get_rect(center = (SCREEN_WIDTH//1.5,SCREEN_HEIGHT//1.25))
        
        screen.blit(Settings_Text,Settings_Rect)

        screen.blit(Resolution_Text,Resolution_Rect)
        screen.blit(Resolution_Text1,Resolution_Rect1)
        screen.blit(Resolution_Text2,Resolution_Rect2)

        screen.blit(Diffuculty_text,Diffuculty_rect)
        screen.blit(Diffuculty_text1,Diffuculty_rect1)
        screen.blit(Diffuculty_text2,Diffuculty_rect2)
        screen.blit(Diffuculty_text3,Diffuculty_rect3)
        screen.blit(Diffuculty_text4,Diffuculty_rect4)

        
        screen.blit(Back_text,Back_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if Resolution_Rect1.collidepoint(event.pos):
                    SCREEN_WIDTH = 1280
                    SCREEN_HEIGHT = 720
                    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
                    bg_menu = pygame.transform.scale(bg_menu,(SCREEN_WIDTH,SCREEN_HEIGHT))
                    bg = pygame.image.load("space2_4-frames.png").convert()
                    bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
                    bg_width = bg.get_width()
                    bg_rect = bg.get_rect()
                    scroll = 0
                    tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1
                    
                if Resolution_Rect2.collidepoint(event.pos):
                    SCREEN_WIDTH = 1920
                    SCREEN_HEIGHT = 1080
                    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
                    bg_menu = pygame.transform.scale(bg_menu,(SCREEN_WIDTH,SCREEN_HEIGHT))
                    bg = pygame.image.load("space2_4-frames.png").convert()
                    bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
                    bg_width = bg.get_width()
                    bg_rect = bg.get_rect()
                    scroll = 0
                    tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1

                if Back_rect.collidepoint(event.pos):
                    menu()
                
                if Diffuculty_rect1.collidepoint(event.pos):
                        DIFFUCULTY[0] = 600
                        DIFFUCULTY[1] = 2000
                        pygame.time.set_timer(obstacle_timer,DIFFUCULTY[0])
                        pygame.time.set_timer(obstacle_timer2,DIFFUCULTY[1])
                        DIF_TEXT = "EASY"
                        max_speed = 10
                        
                elif Diffuculty_rect2.collidepoint(event.pos):
                        DIFFUCULTY[0] = 400
                        DIFFUCULTY[1] = 4000
                        pygame.time.set_timer(obstacle_timer,DIFFUCULTY[0])
                        pygame.time.set_timer(obstacle_timer2,DIFFUCULTY[1])  
                        DIF_TEXT = "MEDIUM"
                        max_speed = 17
                        
                                 
                elif Diffuculty_rect3.collidepoint(event.pos):
                        DIFFUCULTY[0] = 200
                        DIFFUCULTY[1] = 8000
                        pygame.time.set_timer(obstacle_timer,DIFFUCULTY[0])
                        pygame.time.set_timer(obstacle_timer2,DIFFUCULTY[1])
                        DIF_TEXT = "HARD"
                        max_speed = 20
                               
                elif Diffuculty_rect4.collidepoint(event.pos):
                        DIFFUCULTY[0] = 100
                        DIFFUCULTY[1] = 10000
                        pygame.time.set_timer(obstacle_timer,DIFFUCULTY[0])
                        pygame.time.set_timer(obstacle_timer2,DIFFUCULTY[1])
                        DIF_TEXT = "EXTREME"
                        max_speed = 25

        screen.blit(Diffuculty_Shower_Text,Diffuculty_Shower_rect)
                                     
        pygame.display.update()
        clock.tick(60)
        
def menu():
    global playing
    while True:
        
        screen.blit(bg_menu,(0,0))

        Menu_Text = font_menu.render("MAIN MENU",True,"white")
        Menu_Rect = Menu_Text.get_rect(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//8))

        Play_Text = font_menu.render("PLAY",True,"white")
        Play_Rect = Play_Text.get_rect(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2.75))

        Settings_Text = font_menu.render("SETTINGS",True,"white")
        Settings_Rect = Settings_Text.get_rect(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//1.75))

        Quit_Text = font_menu.render("QUIT",True,"white")
        Quit_Rect = Quit_Text.get_rect(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//1.25))

        screen.blit(Menu_Text,Menu_Rect)
        screen.blit(Play_Text,Play_Rect)
        screen.blit(Settings_Text,Settings_Rect)
        screen.blit(Quit_Text,Quit_Rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Play_Rect.collidepoint(event.pos):
                        play()
                        
                if Settings_Rect.collidepoint(event.pos):
                    settings()
                if Quit_Rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            
        pygame.display.update()
        clock.tick(60)

menu()


