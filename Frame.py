import pygame, sys, random


class Chaser_Enemy:
    
    def __init__(self):
        self.pos = (random.randint(1,760), random.randint(1,560))
        self.color = (random.randint(200,250),random.randint(200,250),random.randint(200,250))
        self.size = (30,30)
        self.current_size = (0,0)
        self.growing = True
        self.speed = random.randint(10,30)
        return
        
    def spawn(self):
        if self.current_size > self.size:
            self.growing = False
        else:
            self.current_size = (self.current_size[0]+self.size[0]/100,self.current_size[1]+self.size[1]/100)
        gameDisplay.fill((random.randint(200,250),random.randint(200,250),random.randint(200,250)), rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])
        return
        
    def chase(self, player):
        x = self.pos[0] + (((player.x0)-self.pos[0]) * timer.get_frame_duration() *1.8 )
        y = self.pos[1] + (((player.y0)-self.pos[1]) * timer.get_frame_duration() *1.8 )
        self.pos = (x,y)
        gameDisplay.fill(self.color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])
        return
        
    def __str__(self):
        return '('+str(self.pos)+','+str(self.speed)+','+str(self.color)+','+str(self.size)+')'


class Enemy:
    def __init__(self):
        self.pos = (random.randint(1,760), random.randint(1,560))
        self.speed = (random.randint(-50,50), random.randint(-50,50))
        self.color = (random.randint(50,200),random.randint(50,200),random.randint(50,200))
        self.size = (random.randint(10,35),random.randint(10,35))
        self.current_size = (0,0)
        self.growing = True
        return
    def move(self):
        x = self.pos[0] + (self.speed[0] * timer.get_frame_duration())
        y = self.pos[1] + (self.speed[1] * timer.get_frame_duration())
        self.pos = (x, y)
        self.bounce()      
        gameDisplay.fill(self.color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])
        return
    
    def bounce(self):
        if self.pos[0] > (800-self.size[0]) or self.pos[0] < 0:
            self.speed = (self.speed[0]*-1, self.speed[1])
        if self.pos[1] > (600-self.size[1]) or self.pos[1] < 0:
            self.speed = (self.speed[0], self.speed[1]*-1)
        return
        
    def spawn(self):
        if self.current_size > self.size:
            self.growing = False
        else:
            self.current_size = (self.current_size[0]+self.size[0]/100,self.current_size[1]+self.size[1]/100)
        gameDisplay.fill(self.color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])
    def __str__(self):
        return '('+str(self.pos)+','+str(self.speed)+','+str(self.color)+','+str(self.size)+')'




   
class Character:
    
    def __init__(self,pos):
        self.x0=pos[0]
        self.y0=pos[1]
        self.size = (30,30)
       
    def is_Touching(self,pos,height,width):
        
        x=[self.x0,pos[0]] # character x,  enemy x  Anything 0 is character
        y=[self.y0,pos[1]] # character y,  enemy y  Anything 1 is enemy
        w=[self.size[0],width]
        h=[self.size[1],height]
        
        if (x[1]+w[1]>=x[0]>=x[1]) and (y[1]+h[1]>=y[0]>=y[1]):
            return True
        if (x[0]+w[0]>=x[1]>=x[0]) and (y[1]+h[1]>=y[0]>=y[1]):
            return True
        if (x[0]+w[0]>=x[1]>=x[0]) and (y[0]+h[0]>=y[1]>=y[0]):
            return True
        if (x[1]+w[1]>=x[0]>=x[1]) and (y[0]+h[0]>=y[1]>=y[0]):
            return True 
        return False
    # takes self, and position of 
    
    def set_Location(self,loc):
        self.x0=loc[0]-15
        self.y0=loc[1]-15    
            
    def render(self):
        gameDisplay.fill((0,0,0),rect=[self.x0,self.y0,self.size[1],self.size[0]])


class Clock:
    def __init__(self):
        self.frame_duration = 0.00
        self.this_frame_time = 0
        self.last_frame_time = 0
        return 
    
    def tick(self):
        self.this_frame_time = self.get_time()
        self.frame_duration = (self.this_frame_time - self.last_frame_time) / 1000.000
        self.last_frame_time = self.this_frame_time
        return
    
    def get_time(self):
        return pygame.time.get_ticks()

    def get_frame_duration(self):
        return self.frame_duration
    
    def begin(self):
        self.last_frame_time = self.get_time()
        return
    
#initializes pygame which returns tuple of successes and failures
print(pygame.init())


chaser_list = [] 
enemy_list = []
white = (255,255,255)

#set up timer
timer = Clock()
timer.begin()

tick_interval = 1.00
tick_time = 0

#parameters of first rectangle
speedx = 50
speedy = 25
posx = 100
posy = 100
delay_duration = 5

#setting up the surface, what goes inside is A TUPLE of parameters so use another parenth
gameDisplay = pygame.display.set_mode( (800,600) )

#titles the display
pygame.display.set_caption("FUck my life")

enemy = Enemy()
enemy_list.append(enemy)    
char = Character((400,300))

font=pygame.font.Font(None,50)
font2=pygame.font.Font(None,10)
col=[255,0,255]
sequence=True
gameExit=False
menuState=True
gameState=False
exitState=False

hasClick=True
mode1=False
mode2=False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True  
        if exitState and event.type == pygame.MOUSEBUTTONDOWN:
            if 780>=a[0]>=630 and 580>=a[1]>=500:
                exitState=False
                menuState=True
                print("go to menu")
            elif 170>=a[0]>=20 and 580>=a[1]>=500:
                exitState=False
                gameExit = True
        if menuState and event.type == pygame.MOUSEBUTTONDOWN:
            if 600>=a[0]>=200 and 375>=a[1]>=225:
                gameState=True
                menuState=False
                #if mode1 or mode2:
                    #hasClick=True
                    #menuState=False
                    #gameState=True
                #else:
                    #hasClick=False
                                       
            
    if menuState:
        gameDisplay.fill((0,255,255))
        gameDisplay.fill((255,255,255),rect=[200,225,400,150])
        gameDisplay.fill((0,255,255),rect=[220,245,360,110])
        
        
        text=font.render("Play Mode",1,(255,255,255))
        gameDisplay.blit(text,(310,285))
        if not hasClick:
            text=font2.render("Please select a game mode (1 or 2)",1,(0,0,0))
            gameDisplay.blit(text,(50,50))            
        #gameDisplay.fill((0,0,0))
        a=pygame.mouse.get_pos()
        
    if gameState:
        tick_time += timer.get_frame_duration()
        if tick_time > tick_interval:
            print('new_enemy!')
            tick_time = 0
            enemy = Enemy()
            enemy_list.append(enemy)
            print(len(enemy_list))  
            if len(enemy_list) / 5 == 1:
                chaser = Chaser_Enemy()
                chaser_list.append(chaser)
                print(len(chaser_list))
            
        #white clears what was behind it
        gameDisplay.fill(white)
        char.set_Location(pygame.mouse.get_pos())
        char.render()
        
        for enemy in enemy_list:
            if char.is_Touching(enemy.pos,enemy.size[0],enemy.size[1]) and not enemy.growing:
                gameState=False
                exitState=True
                pygame.draw.circle(gameDisplay,(255,0,0),(char.x0+15,char.y0+15 ),40,2)
                pygame.display.update()
                pygame.time.delay(1250)
                break
            if enemy.growing:
                enemy.spawn()
            else:
                enemy.move()          
        for chaser in chaser_list:
            if char.is_Touching(chaser.pos,chaser.size[0],chaser.size[1]) and not chaser.growing:
                gameState=False
                exitState=True
                pygame.draw.circle(gameDisplay,(255,0,0),(char.x0+15,char.y0+15 ),40,2)
                pygame.display.update()
                pygame.time.delay(1250)
                break
            if chaser.growing:
                chaser.spawn()        
            else:
                chaser.chase(char)

    if exitState:
        a=pygame.mouse.get_pos()
        if col[0]>0 and sequence: #column is list of [255,255,255] outside while loops for color manipulation
            gameDisplay.fill((col[0],col[0],col[0]))
            col[0]-=1
        if col[0]==0:
            sequence = False
            pygame.time.delay(500)
        if not sequence and col[0]<=255:
            text = font.render("Game Over",1,(col[0],col[0],col[0]))
            gameDisplay.blit(text,(300,150))
            col[0]+=1
        elif not sequence and col[1]<=255:
            gameDisplay.fill((col[1],col[1],col[1]),rect=[20,500,150,80])
            gameDisplay.fill((col[1],col[1],col[1]),rect=[630,500,150,80])  
            text=font.render("Exit",1,(0,0,0))
            text2=font.render("Menu",1,(0,0,0))
            gameDisplay.blit(text,(55,525))
            gameDisplay.blit(text2,(655,525))
            col[1]+=1     
        
    #artificial delay
    pygame.time.delay(delay_duration)
    
    pygame.display.update()
    timer.tick()
#only updates specific area mentioned, but if no parameters its like flip,update is more versatile
#pygame.display.update()




#unitializing everything
pygame.quit()

