## -------------------------------------------------------------------- IMPORTS

import pygame, sys, random


## -------------------------------------------------------------------- CLASSES
## --------- BASIC ---------
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

## --------- MODE 1 ---------
class Box_Laser:
    def __init__(self):
        self.size = (40,40)
        possible_pos = [(380,280),(100,100),(100,460),(660,100),(660,460)]
        self.pos = possible_pos[random.randint(0,4)]
        self.color = (175,1,1)
        self.current_color = [5,1,1]
        self.current_size = (0,0)
        self.growing = True 
        self.charging = False
        self.count = 0
        self.gone = False
        self.lasers = False
        self.new_pos = (0,0)
        return
    
    def spawn(self):
        if self.current_size > self.size:
            self.growing = False
        else:
            self.current_size = (self.current_size[0]+self.size[0]/300,self.current_size[1]+self.size[1]/300)
        gameDisplay.fill((5,1,1), rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])  
        
        gameDisplay.fill((5,1,1), rect=[self.pos[0]+10,self.pos[1]-20,self.current_size[0]/2,self.current_size[1]/2]) 
              
        gameDisplay.fill((5,1,1), rect=[self.pos[0]-20,self.pos[1]+10,self.current_size[0]/2,self.current_size[1]/2]) 
       
        gameDisplay.fill((5,1,1), rect=[self.pos[0]+40,self.pos[1]+10,self.current_size[0]/2,self.current_size[1]/2])    
           
        gameDisplay.fill((5,1,1), rect=[self.pos[0]+10,self.pos[1]+40,self.current_size[0]/2,self.current_size[1]/2])      
        return    
    
    def charge(self):
        if self.current_color[0] < 255:
            self.charging = True
            self.current_color[0] += 1
            self.new_pos=self.pos
            gameDisplay.fill(self.current_color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])         
            gameDisplay.fill((5,1,1), rect=[self.pos[0]+10,self.pos[1]-20,self.current_size[0]/2,self.current_size[1]/2])
            gameDisplay.fill((5,1,1), rect=[self.pos[0]-20,self.pos[1]+10,self.current_size[0]/2,self.current_size[1]/2])
            gameDisplay.fill((5,1,1), rect=[self.pos[0]+40,self.pos[1]+10,self.current_size[0]/2,self.current_size[1]/2])        
            gameDisplay.fill((5,1,1), rect=[self.pos[0]+10,self.pos[1]+40,self.current_size[0]/2,self.current_size[1]/2])
        elif self.count == 250 and not self.gone:      
            self.color = (self.color[0]+(255-self.color[0])/10,self.color[1]+(255-self.color[1])/10,self.color[2]+(255-self.color[2])/10)
            gameDisplay.fill(self.color, rect=[self.pos[0]+10,0,20,1000])
            gameDisplay.fill(self.color, rect=[0,self.pos[1]+10,1000,20])
            #gameDisplay.fill(self.color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])
        else:      
            self.charging = False
            self.lasers = True
            gameDisplay.fill(self.color, rect=[self.pos[0]+10,0,20,1000])
            gameDisplay.fill(self.color, rect=[0,self.pos[1]+10,1000,20])
            #gameDisplay.fill(self.color, rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]]) 
            self.count += 1 
        if self.color[1] > 245:
            self.gone = True
            self.lasers = False
        return


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

## --------- MODE 2 ---------
class Coll:
    def __init__(self):
        self.pos = (random.randint(1,w_board-35), random.randint(1,h_board-35))
        self.color = ( reds[random.randint(0,len(reds)-1)],0,0)
        self.size = (20,20)
        self.current_size = (0,0)
        self.growing = True
        return
    def spawn(self):
        if self.current_size > self.size:
            self.growing = False
        else:
            self.current_size = (self.current_size[0]+self.size[0]/100,self.current_size[1]+self.size[1]/100)
        gameDisplay.fill( (random.randint(c_minred,c_maxred),0,0), \
            rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])        
    def deactivate(self):
        gameDisplay.fill( (224,224,224), \
            rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]])         
    def emphasis(self,i):
        ##outside
        out_rect = [self.pos[0]-i,self.pos[1]-i,self.current_size[0]+2*i,self.current_size[1]+2*i]
        gameDisplay.fill( (grays[i],grays[i],grays[i]), \
            rect=out_rect )         
    def render(self,i): 
        ##main
        gameDisplay.fill( (reds[i],0,0), \
            rect=[self.pos[0],self.pos[1],self.current_size[0],self.current_size[1]] )
        
    def __str__(self):
        return '('+str(self.pos)+','+str(self.speed)+','+str(self.color)+','+str(self.size)+')' 

## ------ MISC FUNCTIONS ------
def circle_freeze():
    pygame.draw.circle(gameDisplay,(255,0,0),(char.x0+15,char.y0+15 ),40,2)
    pygame.display.update()
    pygame.time.delay(1250)

## ---------------------------------------------------------------- PYGAME.INIT
print(pygame.init())


## -------------------------------------------------------------------- GLOBALS
## COLORS
black,white,red = (0,0,0),(255,255,255),(255,0,0)
col=[255,0]

## bright red to maroony red
c_minred = 150
c_maxred = 235
reds = list(range(c_minred,c_maxred,3))+[c_maxred]+list(range(c_maxred,c_minred,-3))
c_maxgray = 254
c_mingray = c_maxgray-(len(reds)-1)//2
grays = list(range(c_maxgray,c_mingray,-1))+[c_mingray]+list(range(c_mingray,c_maxgray,1))

## FONTS
font=pygame.font.Font(None,50)
font2=pygame.font.Font(None,35)


## --------------------------------------------------------------- INITIALIZING

## OBJECT LISTS (keep track of which objects are present in the board)
box_laser_list = []
chaser_list = [] 
enemy_list = []
coll_list = []

## TIMER SETUP
timer = Clock()
timer.begin()

tick_interval = 1.00
tick_time = 0

delay_duration = 5

## SURFACE SETUP (what goes inside is tuple of parameters, don't forget double parenthesis)
w_board = 800 ## board width
h_board = 600 ## board height
gameDisplay = pygame.display.set_mode( (w_board,h_board) )


## DISPLAY SETUP
pygame.display.set_caption("FUck my life")     ## window title

## ENEMY SETUP
enemy = Enemy()
enemy_list.append(enemy)

## CHARACTER SETUP
char = Character((400,300))

## COLL SETUP
ct_collected = 0     ## number of collected coll in mode 2
rd = 0              ## counts how many enemy spawns since last collectible
every_rd = 3        ## new collectible every 3 enemy spawn
red_ind = 0 ## counts index of reds list (color of colls)
red_interval = 2 ## how many cycles before red color increases
round_ct = 0 ## counts cycles since last red change

## LOGIC
sequence=True
gameExit=False
menuState=True
gameState=False
exitState=False

hasClick=True
mode1=False
mode2=False


## --------------------------------------------------------------- GAME LOOP

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True  
        if exitState and event.type == pygame.MOUSEBUTTONDOWN:
            if 780>=a[0]>=630 and 580>=a[1]>=500:
                exitState=False
                menuState=True
                mode1=False
                mode2=False   #Reseting everything when menu is clicked
                sequence=True
                enemy_list = []
                box_laser = Box_Laser()
                chaser_list = [] 
                enemy_list = []                
                col=[255,0,255]
            elif 170>=a[0]>=20 and 580>=a[1]>=500:
                exitState=False  #if exit, then leaves the loop
                gameExit = True
        if menuState and event.type == pygame.MOUSEBUTTONDOWN: 
            if 170>=a[0]>=20 and 100>=a[1]>=20: #at the menu, sets gamemode
                mode1=True #Original version
                mode2=False
            if 780>=a[0]>=630 and 100>=a[1]>=20:
                mode2=True #Second Version
                mode1=False
            if 600>=a[0]>=200 and 375>=a[1]>=225:
                if mode1 or mode2: #Only leaves the menu state when a mode is pressed
                    hasClick=True
                    menuState=False
                    gameState=True
                else:
                    hasClick=False #if no mode, then passes boolean to menustate if statement
                                       
            
    if menuState: ## --------------------------------------------- menuState --
        gameDisplay.fill((0,255,255)) #blue background
        if mode1:
            gameDisplay.fill((70,220,255),rect=[5,7,180,105])
        if mode2:
            gameDisplay.fill((70,220,255),rect=[615,7,180,105])
            
        gameDisplay.fill((255,255,255),rect=[200,225,400,150])
        gameDisplay.fill((0,255,255),rect=[220,245,360,110]) #white boxes
        gameDisplay.fill((255,255,255),rect=[20,20,150,80])
        gameDisplay.fill((255,255,255),rect=[630,20,150,80])        
        text=font.render("Play Mode",1,(255,255,255))   #text
        text2=font.render("Mode 1",1,(0,255,255))
        gameDisplay.blit(text2,(34,44))
        text2=font.render("Mode 2",1,(0,255,255)) 
        gameDisplay.blit(text2,(643,44))
        gameDisplay.blit(text,(310,285))
        

        if not hasClick: #This part sends a message to user that they need to pick
            text=font2.render("Please select a game mode (1 or 2)",1,(255,255,255))
            gameDisplay.blit(text,(200,380))           
        #gameDisplay.fill((0,0,0))
        a=pygame.mouse.get_pos()
        if 170>=a[0]>=20 and 100>=a[1]>=20: #mouseover instructions
            text=font2.render("Play Runaway mode: Dodge enemies for as long as you can!",1,(255,255,255))
            gameDisplay.blit(text,(45,500))
        if 780>=a[0]>=630 and 100>=a[1]>=20:
            text=font2.render("Play Collector's mode: Dodge enemies and collect pulsing boxes!",1,(255,255,255))
            gameDisplay.blit(text,(15,500))            
        
    if gameState: ## --------------------------------------------  gameState --
        ## ----------------------------------------------- mode1 --------------
        if mode1:
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
                if len(enemy_list) % 15 == 0:
                    box_laser = Box_Laser()
                    box_laser_list.append(box_laser)
            
                    
            ## DISPLAYING EVERYTHING
            gameDisplay.fill(white)   #white clears what was behind it
    
            ## Char location
            char.set_Location(pygame.mouse.get_pos())
            char.render()
            
            ## Box lasers
            for box_laser in box_laser_list:
                if box_laser.growing:
                    box_laser.spawn()
                elif not box_laser.gone:
                    box_laser.charge()
                ## if box_laser is charging or growing and char.is_touching box or lasers  
                if (box_laser.charging or box_laser.growing) and ( \
                    char.is_Touching(box_laser.pos,40,40) or \
                    char.is_Touching((box_laser.pos[0]-20,box_laser.pos[1]+10),20,20) or \
                    char.is_Touching((box_laser.pos[0]+10,box_laser.pos[1]-20),20,20) or \
                    char.is_Touching((box_laser.pos[0]+40,box_laser.pos[1]+10),20,20) or \
                    char.is_Touching((box_laser.pos[0]+10,box_laser.pos[1]+40),20,20) \
                    ): 
                    print('here') ##remove later
                    ## gamestate to exitstate
                    gameState=False
                    exitState=True
                    ## circle around frozen gameplay
                    circle_freeze()
                    break
                
                ## if box_laser is grown and on screen and char.is_touching box or lasers
                if box_laser.lasers and (not box_laser.gone) and (\
                    char.is_Touching((0,box_laser.pos[1]+10),20,1000) or \
                    char.is_Touching((box_laser.pos[0]+10,0),1000,20) \
                    ):
                    print('there') ##remove later
                    ## gamestate to exitstate
                    gameState=False
                    exitState=True
                    ## circle around frozen gameplay
                    circle_freeze()
                    break  
            
            ## Enemies
            for enemy in enemy_list:
                ## if character is touching enemy and enemy isn't growing, game over
                if char.is_Touching(enemy.pos,enemy.size[0],enemy.size[1]) and not enemy.growing:
                    ## gamestate to exitstate
                    gameState=False
                    exitState=True
                    ## circle around frozen gameplay
                    circle_freeze()
                    break
                ## if enemy is growing, no game over if char.is_touching enemy
                if enemy.growing:
                    enemy.spawn()
                else:
                    enemy.move()
            
            ## Chasers
            for chaser in chaser_list:
                ## if character is touching chaser and enemy isn't growing, game over
                if char.is_Touching(chaser.pos,chaser.size[0],chaser.size[1]) and not chaser.growing:
                    ## gamestate to exitstate
                    gameState=False
                    exitState=True
                    ## circle around frozen gameplay
                    circle_freeze()
                    break
                ## if chaser is growing, no game over if char.is_touching chaser
                if chaser.growing:
                    chaser.spawn()        
                else:
                    chaser.chase(char)
        
        ## ----------------------------------------------- mode2 --------------
        if mode2:
            tick_time += timer.get_frame_duration()
            
            round_ct +=1 ## counts cycles since last red color change
            ## changes red color for pulsing col
            if round_ct>red_interval:
                round_ct = 0
                red_ind += 1
                if red_ind >= len(reds):
                    red_ind = 0  
                    
            ## spawns ENEMIES
            if tick_time > tick_interval:
                print('new_enemy!')
                tick_time = 0
                enemy = Enemy()
                enemy_list.append(enemy)
                print(len(enemy_list)) 
                
                rd +=1 ## rounds since last coll spawn    
            
            ## spawns COL 
            if rd > every_rd:
                print('--new_col--')
                coll = Coll()
                coll_list.append(coll)
                rd = 0            

            ## DISPLAYING EVERYTHING
            gameDisplay.fill(white)   #white clears what was behind it
            
            ## Coll emplasis (behind everything else)
            for coll in coll_list:
                if not coll.growing:
                    coll.emphasis(red_ind)            
    
            ## Char location
            char.set_Location(pygame.mouse.get_pos())
            char.render()
            
            ## Coll
            for coll in coll_list:
                ## setting color for uniform flicker
                coll.color = (reds[red_ind],0,0)
                ## if char.is_touching coll, collect item, even if growing
                if char.is_Touching(coll.pos,30,30):
                    print("COLLECTED")
                    coll.deactivate()
                    ct_collected +=1
                    coll_list.pop(coll_list.index(coll))
                ## if not char.is_touching coll, coll is growing continue growing
                elif coll.growing:
                    coll.spawn()
                else:
                    coll.render(red_ind)            
             
            ## Enemies
            for enemy in enemy_list:
                ## if character is touching enemy and enemy isn't growing, game over
                if char.is_Touching(enemy.pos,enemy.size[0],enemy.size[1]) and not enemy.growing:
                    ## gamestate to exitstate
                    gameState=False
                    exitState=True
                    ## circle around frozen gameplay
                    circle_freeze()
                    break
                ## if enemy is growing, no game over if char.is_touching enemy
                if enemy.growing:
                    enemy.spawn()
                else:
                    enemy.move()
            

    if exitState: ## --------------------------------------------- exitState --
        a=pygame.mouse.get_pos()
        if col[0]>0 and sequence: ##column is list of [255,255,255] outside while loops for color manipulation
            gameDisplay.fill((col[0],col[0],col[0])) 
            col[0]-=1
        if col[0]==0: ## delaying for fade effect
            sequence = False
            pygame.time.delay(500)
        if not sequence and col[0]<=255: ##fading in game over text
            text = font.render("Game Over",1,(col[0],col[0],col[0]))
            gameDisplay.blit(text,(300,150))
            col[0]+=1
        elif not sequence and col[1]<=255: ## exit and menu buttons fade in
            gameDisplay.fill((col[1],col[1],col[1]),rect=[20,500,150,80])
            gameDisplay.fill((col[1],col[1],col[1]),rect=[630,500,150,80])  
            text=font.render("Exit",1,(0,0,0))
            text2=font.render("Menu",1,(0,0,0))
            gameDisplay.blit(text,(57,525))
            gameDisplay.blit(text2,(655,525))
            col[1]+=1     
        
    ##artificial delay
    pygame.time.delay(delay_duration)
    
    pygame.display.update()
    timer.tick()
#only updates specific area mentioned, but if no parameters its like flip,update is more versatile
#pygame.display.update()

#unitializing everything
pygame.quit()